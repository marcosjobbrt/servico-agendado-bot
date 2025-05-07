import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Verificar se a tabela 'agendamentos' existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='agendamentos';")
tabela_existe = cursor.fetchone()

if tabela_existe:
    # Executar um comando para mostrar as colunas da tabela agendamentos
    cursor.execute("PRAGMA table_info(agendamentos);")
    colunas = cursor.fetchall()

    # Exibir as colunas
    print("Colunas da tabela 'agendamentos':")
    for coluna in colunas:
        print(coluna)
else:
    print("A tabela 'agendamentos' não existe no banco de dados.")

# Fechar a conexão
conn.close()