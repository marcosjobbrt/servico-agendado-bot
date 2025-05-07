import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Exibe todas as entradas no banco para verificar se os dados estão lá
cursor.execute('SELECT * FROM agendamentos')
agendamentos = cursor.fetchall()

# Exibe todos os agendamentos encontrados no banco
print("Todos os agendamentos no banco:", agendamentos)

conn.close()
