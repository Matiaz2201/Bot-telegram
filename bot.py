import requests
import json
import time

TOKEN = 'INSIRA O TOKE DO BOT AQUI' # Token gerado para o bot
chat_id = 'INSIRA ID DO CHAT AQUI' # id do chat que o bot vai responder

respostas = {
    'Oi' : 'Oiii',
    'Olá' : 'Olá bb',
    'E aew' : 'salve !',
    'Tudo bem ?' : 'Melhor agora e você ?',
    'Qual seu nome ?' : 'Bot do Matias',
} # Dicionario de respostas, ainda não está no codigo em produção

class bot:

    @staticmethod
    def verificar_msgs():
        id_msg = 0
        while True:
            url = 'https://api.telegram.org/bot{}/getUpdates'.format(TOKEN) # Preparando URL com token
            response = requests.get(url) # Coletando msg atraves de um GET na API do telegram

            msgs = json.loads(response.text)['result'] # Transformando o texto do reponse em JSON e pegando o result do GET
            mensagem = msgs[len(msgs)-1]['message']['text'] # Coletando o texto da ultima msg enviada

            print(mensagem)
            if id_msg == 0:
                msg = 'Bot iniciado'
                url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)# Preparando URL com token
                data = {'chat_id':chat_id, 'text': msg}# preparando a data do POST

                requests.post(url, data=data)# Enviando msg atraves de um POST na API do telegram
                id_msg = msgs[len(msgs)-1]['update_id']
                time.sleep(1)
            elif mensagem == '/status' and id_msg != msgs[len(msgs)-1]['update_id']: # Verificando se a msg recebida e a esperada '/staus' e verificando se essa msg já não foi respondida
                msg = 'Bot em execução'
                url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)# Preparando URL com token
                data = {'chat_id':chat_id, 'text': msg}# preparando a data do POST

                requests.post(url, data=data)# Enviando msg atraves de um POST na API do telegram
                id_msg = msgs[len(msgs)-1]['update_id']
                time.sleep(1)


bot.verificar_msgs()
