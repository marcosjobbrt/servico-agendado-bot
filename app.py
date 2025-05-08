from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servico_agendado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'segredo'  # Necessário para o Flask-WTF
db = SQLAlchemy(app)

# Model de Empresa
class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    clientes = db.relationship('Cliente', backref='empresa', lazy=True)

# Model de Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    data_servico = db.Column(db.String(20), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)

# Formulário de adição de nova empresa
class EmpresaForm(FlaskForm):
    nome = StringField('Nome da Empresa', validators=[DataRequired()])
    submit = SubmitField('Adicionar Empresa')

# Formulário de adição de cliente
class ClienteForm(FlaskForm):
    nome = StringField('Nome do Cliente', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    data_servico = StringField('Data do Serviço', validators=[DataRequired()])
    submit = SubmitField('Cadastrar Cliente')

# Função para inicializar o banco de dados
def create_tables():
    with app.app_context():
        db.create_all()  # Cria todas as tabelas no banco de dados

# Inicializa o banco de dados (criação das tabelas)
create_tables()

# Rota da página inicial
@app.route('/')
def home():
    empresas = Empresa.query.all()  # Pega todas as empresas
    return render_template('index.html', empresas=empresas)

# Rota para listar todas as empresas
@app.route('/listar_empresas')
def listar_empresas():
    empresas = Empresa.query.all()  # Pega todas as empresas
    return render_template('listar_empresas.html', empresas=empresas)

# Rota para listar os clientes de uma empresa específica
@app.route('/listar_clientes_por_empresa/<int:empresa_id>')
def listar_clientes_por_empresa(empresa_id):
    empresa = Empresa.query.get_or_404(empresa_id)
    clientes = Cliente.query.filter_by(empresa_id=empresa.id).all()  # Pega todos os clientes dessa empresa
    return render_template('listar_clientes.html', empresa=empresa, clientes=clientes)

# Rota para adicionar uma nova empresa
@app.route('/adicionar_empresa', methods=['GET', 'POST'])
def adicionar_empresa():
    form = EmpresaForm()
    if form.validate_on_submit():
        empresa = Empresa(nome=form.nome.data)
        db.session.add(empresa)
        try:
            db.session.commit()  # Tenta adicionar a empresa
            flash('Empresa adicionada com sucesso!', 'success')  # Flash de sucesso
            return redirect(url_for('home'))  # Redireciona para a página inicial
        except Exception as e:
            db.session.rollback()  # Caso ocorra um erro, faz o rollback
            flash(f'Erro ao adicionar a empresa. Detalhes: {e}', 'danger')  # Flash de erro
            print(f"Erro ao adicionar empresa: {e}")  # Debugging
    return render_template('adicionar_empresa.html', form=form)

# Rota para cadastrar um cliente
@app.route('/cadastrar_cliente/<int:empresa_id>', methods=['GET', 'POST'])
def cadastrar_cliente(empresa_id):
    form = ClienteForm()
    empresa = Empresa.query.get_or_404(empresa_id)
    if form.validate_on_submit():
        cliente = Cliente(
            nome=form.nome.data,
            telefone=form.telefone.data,
            endereco=form.endereco.data,
            data_servico=form.data_servico.data,
            empresa_id=empresa_id  # Associando o cliente à empresa correta
        )
        db.session.add(cliente)
        try:
            db.session.commit()  # Tenta adicionar o cliente
            flash('Cliente cadastrado com sucesso!', 'success')  # Flash de sucesso
            return redirect(url_for('listar_clientes_por_empresa', empresa_id=empresa_id))  # Redireciona para a lista de clientes da empresa
        except Exception as e:
            db.session.rollback()  # Caso ocorra um erro, faz o rollback
            flash(f'Erro ao cadastrar o cliente. Detalhes: {e}', 'danger')  # Flash de erro
            print(f"Erro ao cadastrar cliente: {e}")  # Debugging
    return render_template('cadastrar_cliente.html', form=form, empresa=empresa)

if __name__ == '__main__':
    app.run(debug=True)
