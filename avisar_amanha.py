import os
from dotenv import load_dotenv

# Ativar/desativar modo simulado
modo_simulado = True

# Carrega variáveis do .env
load_dotenv()

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

# Exemplo de chamada
enviar_mensagem("Marcos", "+5562999999999", "07/05/2025")
