import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import sqlite3

# Ativar/desativar modo simulado
modo_simulado = True

# Carrega variáveis do .env
load_dotenv()

# Função para enviar mensagem
def enviar_mensagem(cliente, telefone, data_servico):
    mensagem = f"Olá {cliente}, lembramos que seu serviço de dedetização está agendado para amanhã ({data_servico}). Qualquer dúvida, estamos à disposição!"

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

# Função para enviar mensagens para todos os clientes agendados para amanhã
def avisar_clientes():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()

    # Calcular a data de amanhã
    data_amanha = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    data_amanha_str = data_amanha.strftime('%Y-%m-%d')

    # Buscar os agendamentos para amanhã
    cursor.execute('''
        SELECT nome, telefone, data_servico
        FROM agendamentos
        WHERE data_servico = ?
    ''', (data_amanha_str,))

    # Obter todos os resultados de agendamentos
    agendamentos = cursor.fetchall()

    if agendamentos:
        for agendamento in agendamentos:
            cliente, telefone, data_servico = agendamento
            # Enviar mensagem para o cliente
            enviar_mensagem(cliente, telefone, data_servico)
    else:
        print(f"Não há agendamentos para amanhã ({data_amanha_str}).")

    conn.close()

# Executa a função para avisar os clientes
if __name__ == '__main__':
    avisar_clientes()
