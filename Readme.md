# Sistema de Agendamento e Automação para Serviços de Dedetização

Este projeto automatiza o agendamento e a comunicação com os clientes da **Ecopest** (ou outras empresas de dedetização). Ele utiliza o **Twilio** para enviar mensagens via WhatsApp, e é configurado para executar automaticamente usando **GitHub Actions**.

## Funcionalidades

1. **Confirmação de serviços**: Envia mensagens de confirmação para os clientes antes da dedetização.
2. **Agendamento de serviços**: Organiza a lista de serviços a serem realizados e envia lembretes para os clientes.
3. **Automação diária**: Utiliza GitHub Actions para agendar e rodar os scripts de automação todos os dias.

## Tecnologias

- **Python**: Linguagem de programação utilizada para os scripts.
- **Twilio**: Serviço de envio de mensagens via WhatsApp.
- **GitHub Actions**: Para agendar e automatizar a execução dos scripts.
- **SQLite**: Banco de dados para armazenar informações sobre os clientes e serviços.

## Requisitos

Para rodar este projeto, você precisa do seguinte:

1. **Python 3.x** instalado.
2. **Twilio** (crie uma conta em [Twilio](https://www.twilio.com/)) para obter as credenciais de envio de mensagens.
3. **GitHub Actions** configurado para agendar a execução do script.

## Como configurar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/servico-agendado-bot.git
   cd servico-agendado-bot
