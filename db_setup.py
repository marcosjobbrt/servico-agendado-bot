import sqlite3

# Cria ou conecta ao banco de dados
conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Criação da tabela de agendamentos, incluindo a coluna 'data_servico'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        nome TEXT,
        telefone TEXT,
        endereco TEXT,
        data_servico TEXT  -- Coluna para registrar a data do serviço
    )
''')

# Exemplo de inserção de dados
cursor.execute('''
    INSERT INTO agendamentos (data, nome, telefone, endereco, data_servico) 
    VALUES ('2024-08-15', 'Ana', '+5511988888888', 'Rua das Flores, 100', '2024-05-15')
''')

# Salva as mudanças e fecha a conexão
conn.commit()
conn.close()

print("Banco de dados configurado com sucesso!")
