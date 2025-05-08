import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Criar tabela para empresas de DDT (caso não exista)
cursor.execute('''
CREATE TABLE IF NOT EXISTS empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

# Criar tabela para agendamentos (caso não exista)
cursor.execute('''
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    endereco TEXT NOT NULL,
    data_servico TEXT NOT NULL,
    empresa TEXT NOT NULL
)
''')

# Commit e fechar a conexão
conn.commit()
conn.close()

print("Estrutura do banco verificada e tabelas criadas (se necessário).")
