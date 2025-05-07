import os
from dotenv import load_dotenv

# Modo simulado: True = teste no terminal / False = envio real com Twilio
modo_simulado = True

# Carrega as variáveis de ambiente do .env
load_dotenv()

def enviar_mensagem(cliente, telefone):
    mensagem = f"Olá {cliente}, gostaríamos de confirmar o seu serviço de dedetização agendado. Por favor, confirme a presença."

    if modo_simulado:
        print(f"[SIMULADO] Mensagem para {telefone}: {mensagem}")
    else:
        from twilio.rest import Client
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_number = os.getenv('TWILIO_NUMBER')  # Adicione esta variável no seu .env

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=mensagem,
            from_=twilio_number,
            to=telefone
        )

        print(f"Mensagem enviada para {telefone}")
enviar_mensagem("Marcos", "+5511999999999")