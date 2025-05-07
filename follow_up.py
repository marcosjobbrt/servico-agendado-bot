import sqlite3
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Carrega as variáveis de ambiente do .env
load_dotenv()

# Modo simulado: True = teste no terminal / False = envio real com Twilio
modo_simulado = True

def enviar_mensagem(cliente, telefone):
    # Nova mensagem com a garantia de serviço
    mensagem = f"Olá {cliente}, a garantia do seu serviço de dedetização acabou. Vamos agendar o próximo serviço?"

    if modo_simulado:
        print(f"[SIMULADO] Mensagem para {telefone}: {mensagem}")
    else:
        # Aqui você incluiria o envio real via Twilio, conforme já discutido
        print(f"Mensagem real para {telefone}: {mensagem}")

def verificar_servicos_90_dias():
    # Conecta ao banco de dados
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()

    # Data atual
    data_atual = datetime.now()

    # 90 dias atrás
    data_limite = data_atual - timedelta(days=90)
    data_limite_str = data_limite.strftime('%Y-%m-%d')

    # Consulta para buscar agendamentos feitos há mais de 90 dias
    cursor.execute("SELECT nome, telefone, data FROM agendamentos WHERE data <= ?", (data_limite_str,))
    
    # Recupera todos os resultados
    agendamentos = cursor.fetchall()

    # Para cada agendamento, envia o follow-up
    for agendamento in agendamentos:
        nome, telefone, data_servico = agendamento
        print(f"Enviando follow-up para {nome} ({telefone}), serviço realizado em: {data_servico}")
        enviar_mensagem(nome, telefone)

    conn.close()

# Chama a função para verificar os serviços e enviar o follow-up
verificar_servicos_90_dias()
