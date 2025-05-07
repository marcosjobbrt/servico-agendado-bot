import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Adicionar a coluna 'ultimo_followup' se não existir
try:
    cursor.execute('ALTER TABLE agendamentos ADD COLUMN ultimo_followup TEXT')
    print("Coluna 'ultimo_followup' adicionada com sucesso.")
except sqlite3.OperationalError:
    print("A coluna 'ultimo_followup' já existe na tabela.")

# Commit e fechar a conexão
conn.commit()
conn.close()
