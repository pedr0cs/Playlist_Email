from dotenv import load_dotenv #esconder as chaves
import os
load_dotenv()
import requests #importando a biblioteca
import sys #parar o programa com try e except ja que nao tem um for

chave_api = os.getenv('CHAVE_CLIMA')
url = f'https://api.openweathermap.org/data/2.5/weather?q=Austin&appid={chave_api}&units=metric&lang=pt'
try:
    resposta = requests.get(url)#puxando a biblioteca 
    dados = resposta.json()#reposta da api
    #puxando as playlists
    playlists = {
       'frio': 'https://open.spotify.com/playlist/37i9dQZF1EIdweJIvlLS4r?si=eb52257f29754a98',
        'perfeito': 'https://open.spotify.com/playlist/37i9dQZF1EIfvipBGiKzgO?si=afe1574300e4471b',
        'sol': 'https://open.spotify.com/playlist/37i9dQZF1EVJSvZp5AOML2?si=e8af44981c884b25',
        'random' : 'https://open.spotify.com/playlist/37i9dQZF1EIeEGqN5vooFV?si=7669605d24e1473b',
        'quente' : 'https://open.spotify.com/playlist/37i9dQZF1EVCu9jtlIEnHS?si=bb3b97ee02e848ae',
    }
    temperatura = dados['main']['temp'] #puxando so a descricao do clima
    descricao = dados['weather'][0]['description']
except:
    print('Erro na API. Analise a sua chave. Caso seja nova, aguarde ate 2(DUAS)horas para que seja ativa.')
    sys.exit()
#transfoma a temperatura nas playlists
def estilo_musical(temperatura):
    if temperatura < 15:
        return 'frio'
    elif 15 <= temperatura <= 20:
        return 'perfeito'
    elif 21 <= temperatura <= 30:
        return 'sol'
    elif temperatura > 37:
        return 'quente'
    else:
        return 'random'

estilo = estilo_musical(temperatura)
link = playlists[estilo]
mensagem = f'Bom dia, Pedroca! Vamos comecar o dia!\nHoje a temperatura esta {temperatura}°C\nPelo visto hoje teremos {descricao}.\nCom esse clima, a playlist do dia é:\n{link}'

import smtplib
from email.mime.text import MIMEText

remetente = 'taving04@gmail.com'
destinatario = 'pedrguerra4@gmail.com'
senha_app = os.getenv('SENHA_EMAIL')

assunto = 'Bom dia! Playlist do dia chegando...'

email = MIMEText(mensagem)
email['Subject'] = assunto
email['From'] = remetente
email['To'] = destinatario

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(remetente, senha_app)
        servidor.sendmail(remetente, destinatario, email.as_string())
        print('Email enviado com sucesso')
except:
        print('Erro no envio do email. Verificar emails, internet, chaves e variaveis')
        sys.exit()