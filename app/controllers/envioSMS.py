from twilio.rest import Client
import random

def envio_SMS(tipo):

    senha =random.randint(0,999)
    numero = '11946318493'
    mensagem = "Sua senha é " + tipo + str(senha)
    #text = urllib.parse.quote(f"Olá {nome}! {mensagem}")


    account_sid = "AC7017f3e5ed5b6ac3c63075dedee79a1f"
    auth_token  = "14e31ad6a44a866b4c28b931c79a0cf2"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to='+5511946318493',
        from_="+15044144601",
        body="Olá! " + mensagem)

    print(message.sid)

#envio_SMS('C')
