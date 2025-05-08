import sqlite3

# Função para criar o banco de dados e as tabelas
def criar_banco():
    # Conectar ao banco de dados (ele será criado se não existir)
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()

    # Criar tabela para empresas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

    # Criar tabela para clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa TEXT NOT NULL,
            nome TEXT NOT NULL,
            telefone TEXT,
            endereco TEXT,
            data_servico DATE
        )
    ''')

    # Confirmar e fechar a conexão com o banco
    conn.commit()
    conn.close()

# Chamar a função para criar as tabelas
if __name__ == '__main__':
    criar_banco()
    print("Banco de dados configurado com sucesso!")
