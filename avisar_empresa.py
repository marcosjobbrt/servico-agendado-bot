import sqlite3
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from datetime import datetime, timedelta

# Configurações do Twilio para WhatsApp
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_WHATSAPP_NUMBER = os.getenv('FROM_WHATSAPP_NUMBER')  # Número de envio via WhatsApp

# Configurações de E-mail (Gmail como exemplo)
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Função para enviar mensagem via WhatsApp
def enviar_whatsapp(para, mensagem):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=mensagem,
        from_='whatsapp:' + FROM_WHATSAPP_NUMBER,  # Enviar via WhatsApp
        to='whatsapp:' + para  # Enviar para número de WhatsApp
    )
    print(f"Mensagem enviada via WhatsApp para {para}: {mensagem}")

# Função para enviar e-mail
def enviar_email(para, assunto, mensagem):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = para
    msg['Subject'] = assunto

    # Corpo da mensagem
    msg.attach(MIMEText(mensagem, 'plain'))

    # Conectar ao servidor SMTP e enviar e-mail
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, para, text)
        server.quit()
        print(f"E-mail enviado para {para}: {mensagem}")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {para}: {e}")

# Função para buscar agendamentos e enviar a lista para a empresa
def avisar_empresas():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()

    # Calcular a data de amanhã
    data_amanha = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    data_amanha_str = data_amanha.strftime('%Y-%m-%d')

    # Buscar todos os agendamentos para amanhã, agrupados por empresa
    cursor.execute('''
        SELECT empresa, GROUP_CONCAT(nome || " (" || telefone || ") - " || endereco || " - " || data_servico, "\n") 
        FROM agendamentos
        WHERE data_servico = ?
        GROUP BY empresa
    ''', (data_amanha_str,))

    # Obter os resultados
    empresas_agendamentos = cursor.fetchall()

    # Verificar se há agendamentos para as empresas
    if empresas_agendamentos:
        for empresa_agendamento in empresas_agendamentos:
            empresa, lista_servicos = empresa_agendamento

            # Criar a mensagem para a empresa com os detalhes dos agendamentos
            mensagem = f"Olá {empresa},\n\nVocê tem os seguintes serviços agendados para amanhã ({data_amanha_str}):\n\n{lista_servicos}"

            # Obter o telefone de contato da empresa para WhatsApp (Aqui você pode adaptar para pegar de um banco de dados ou variável de ambiente)
            telefone_empresa = '+5511988888888'  # Exemplo de telefone de contato da empresa para WhatsApp

            # Enviar mensagem para a empresa com a lista de serviços via WhatsApp
            enviar_whatsapp(telefone_empresa, mensagem)

            # Obter o e-mail de contato da empresa (Aqui você pode adaptar para pegar de um banco de dados ou variável de ambiente)
            email_empresa = 'empresa@example.com'  # Exemplo de e-mail da empresa

            # Enviar e-mail para a empresa com a lista de serviços
            enviar_email(email_empresa, f"Serviços agendados para amanhã ({data_amanha_str})", mensagem)

            print(f"Serviços para a empresa {empresa}:")
            print(lista_servicos)

    else:
        print("Não há agendamentos para amanhã.")

    conn.close()

if __name__ == '__main__':
    avisar_empresas()
