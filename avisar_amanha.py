import twilio
from twilio.rest import Client
import os

def avisar_servico_amanha(cliente, telefone):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    mensagem = f"Olá {cliente}, lembrando que amanhã temos o serviço agendado de dedetização. Estamos te aguardando!"

    message = client.messages.create(
        body=mensagem,
        from_='+1415XXXXXXX',  # Substitua pelo número do Twilio
        to=telefone
    )

    print(f"Mensagem enviada para {telefone}")