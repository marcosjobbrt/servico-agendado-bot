import sqlite3
from datetime import datetime, timedelta

# Data de amanhã
data_amanha = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
data_amanha_str = data_amanha.strftime('%Y-%m-%d')

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Inserir um agendamento para amanhã
cursor.execute('''
    INSERT INTO agendamentos (data, nome, telefone, endereco)
    VALUES (?, ?, ?, ?)
''', (data_amanha_str, 'Maria', '+5511999999999', 'Rua Exemplo, 123'))

# Confirmar a transação e fechar a conexão
conn.commit()
conn.close()

print(f"Agendamento inserido para amanhã ({data_amanha_str})")