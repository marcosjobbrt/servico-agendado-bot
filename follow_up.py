import sqlite3
from datetime import datetime, timedelta

# Conecta ao banco de dados
conn = sqlite3.connect('agendamentos.db')
cursor = conn.cursor()

# Data de hoje
hoje = datetime.now().date()

# Seleciona todos os agendamentos
cursor.execute("""
    SELECT id, nome, telefone, data_servico, ultimo_followup, empresa
    FROM agendamentos
""")
agendamentos = cursor.fetchall()

# Loop para enviar follow-up para os clientes que precisam
for id_, nome, telefone, data_servico, ultimo_followup, empresa in agendamentos:
    # Verifica se o agendamento já tem a data do serviço
    if data_servico:
        data_servico = datetime.strptime(data_servico, "%Y-%m-%d").date()
        dias_passados = (hoje - data_servico).days
        
        # Envia follow-up se passaram 90 dias ou mais
        if dias_passados >= 90 and (not ultimo_followup or ultimo_followup != str(hoje)):
            mensagem = f"Olá {nome}, aqui é da {empresa}. A garantia do seu serviço de dedetização acabou. Vamos agendar o próximo serviço?"
            
            # Aqui você pode implementar o envio real via Twilio ou outro serviço
            # Exemplo de envio de mensagem (simulado para testes)
            print(f"[SIMULADO] Enviando mensagem para {telefone}: {mensagem}")
            
            # Atualiza o campo 'ultimo_followup' com a data de hoje
            cursor.execute("UPDATE agendamentos SET ultimo_followup = ? WHERE id = ?", (str(hoje), id_))

# Confirma a transação e fecha a conexão
conn.commit()
conn.close()

print(f"Follow-up enviado para {len(agendamentos)} clientes.")
