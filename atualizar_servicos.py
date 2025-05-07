import sqlite3
from datetime import datetime

# Conecta ao banco de dados
conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Data de hoje
data_hoje = datetime.now().strftime('%Y-%m-%d')

# Atualiza os campos de data de serviço para os agendamentos com data de serviço faltando
cursor.execute('''
    UPDATE agendamentos
    SET data_servico = ?
    WHERE data_servico IS NULL
''', (data_hoje,))

conn.commit()
conn.close()

print(f"Data de serviço atualizada para hoje ({data_hoje}) nos agendamentos com data de serviço faltando.")