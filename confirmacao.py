import twilio
from twilio.rest import Client
import os

def enviar_mensagem(cliente, telefone):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    mensagem = f"Olá {cliente}, gostaríamos de confirmar o seu serviço de dedetização agendado. Por favor, confirme a presença."

    message = client.messages.create(
        body=mensagem,
        from_='+1415XXXXXXX',  # Substitua pelo número do Twilio
        to=telefone
    )

    print(f"Mensagem enviada para {telefone}")
