import os
from dotenv import load_dotenv

# Ativar/desativar modo simulado
modo_simulado = True

# Carrega variáveis do .env
load_dotenv()

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

# Exemplo de chamada
enviar_mensagem("Marcos", "+5562992059790")
