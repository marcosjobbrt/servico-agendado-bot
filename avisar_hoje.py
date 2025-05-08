import os
from dotenv import load_dotenv
from datetime import datetime
import sqlite3

# Ativar/desativar modo simulado
modo_simulado = True

# Carrega variáveis do .env
load_dotenv()

# Função para enviar mensagem
def enviar_mensagem(cliente, telefone):
    mensagem = f"Olá {cliente}, estamos a caminho para realizar o serviço de dedetização conforme agendado para hoje. Até breve!"

    if modo_simulado:
        print(f"[SIMULADO] Mensagem para {telefone}: {mensagem}")
    else:
        from twilio.rest import Client
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_number = os.getenv('TWILIO_NUMBER')

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=mensagem,
            from_=twilio_number,
            to=telefone
        )

        print(f"Mensagem enviada para {telefone}")

# Função para avisar todos os clientes com serviço agendado para hoje
def avisar_clientes_hoje():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()

    # Calcular a data de hoje
    data_hoje = datetime.now().strftime('%Y-%m-%d')

    # Buscar os agendamentos para hoje
    cursor.execute('''
        SELECT nome, telefone
        FROM agendamentos
        WHERE data_servico = ?
    ''', (data_hoje,))

    # Obter todos os resultados de agendamentos
    agendamentos = cursor.fetchall()

    if agendamentos:
        for agendamento in agendamentos:
            cliente, telefone = agendamento
            # Enviar mensagem para o cliente
            enviar_mensagem(cliente, telefone)
    else:
        print(f"Não há agendamentos para hoje ({data_hoje}).")

    conn.close()

# Executa a função para avisar os clientes
if __name__ == '__main__':
    avisar_clientes_hoje()
