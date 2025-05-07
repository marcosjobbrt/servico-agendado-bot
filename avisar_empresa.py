import sqlite3
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta  # Corrigido: importação do timedelta

# Carrega as variáveis de ambiente do .env
load_dotenv()

# Modo simulado: True = teste no terminal / False = envio real com Twilio
modo_simulado = True

def enviar_mensagem_empresa(mensagem):
    if modo_simulado:
        print(f"[SIMULADO] Envio para empresa: {mensagem}")
    else:
        # Aqui você pode incluir a lógica real de envio para a empresa, por exemplo, via e-mail ou Twilio
        print(f"Mensagem real para empresa: {mensagem}")

def obter_agendamentos_amanha():
    # Conecta ao banco de dados
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()

    # Data de amanhã
    data_amanha = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    data_amanha_str = data_amanha.strftime('%Y-%m-%d')

    print(f"Procurando agendamentos para a data: {data_amanha_str}")  # Verificação da data
   
    # Consulta para obter todos os agendamentos para amanhã
    cursor.execute("SELECT nome, telefone, endereco, data FROM agendamentos WHERE data = ?", (data_amanha_str,))
    
    # Recupera todos os resultados
    agendamentos = cursor.fetchall()

    # Cria a mensagem para a empresa
    if agendamentos:
        mensagem = f"Resumo dos agendamentos para amanhã ({data_amanha_str}):\n"
        for agendamento in agendamentos:
            nome, telefone, endereco, data_servico = agendamento
            mensagem += f"\nCliente: {nome}, Telefone: {telefone}, Endereço: {endereco or 'Não informado'}, Data do serviço: {data_servico}"
    else:
        mensagem = "Não há agendamentos para amanhã."

    conn.close()

    # Envia a mensagem para a empresa
    enviar_mensagem_empresa(mensagem)

# Chama a função para obter os agendamentos de amanhã e enviar o resumo
obter_agendamentos_amanha
