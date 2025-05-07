import sqlite3
from datetime import datetime, timedelta

# Data de amanhã
data_amanha = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
data_amanha_str = data_amanha.strftime('%Y-%m-%d')

conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Dados do novo agendamento
nome = 'Maria'
telefone = '+5511999999999'
endereco = 'Rua Exemplo, 123'

# Verifica se já existe um agendamento igual
cursor.execute('''
    SELECT COUNT(*) FROM agendamentos 
    WHERE data = ? AND nome = ? AND telefone = ?
''', (data_amanha_str, nome, telefone))

existe = cursor.fetchone()[0]

if existe == 0:
    cursor.execute('''
        INSERT INTO agendamentos (data, nome, telefone, endereco)
        VALUES (?, ?, ?, ?)
    ''', (data_amanha_str, nome, telefone, endereco))
    print(f"✅ Agendamento inserido para {nome} em {data_amanha_str}")
else:
    print(f"⚠️ Agendamento já existe para {nome} em {data_amanha_str}, nada foi inserido.")

conn.commit()
conn.close()
