from dotenv import load_dotenv #esconder as chaves
import os
load_dotenv()
import smtplib
from email.mime.text import MIMEText
import requests #importando a biblioteca
import sys #parar o programa com try e except ja que nao tem um for

chave_api = os.getenv('CHAVE_CLIMA')
link_quote = 'https://zenquotes.io/api/random'
quotes = requests.get(link_quote)
dados_quote = quotes.json()
frase = dados_quote[0]['q']
autor = dados_quote[0]['a']
email1 = os.getenv('EMAIL_1')
email2 = os.getenv('EMAIL_2')
playlists = {
       'frio': 'https://open.spotify.com/playlist/37i9dQZF1EIdweJIvlLS4r?si=eb52257f29754a98',
        'perfeito': 'https://open.spotify.com/playlist/37i9dQZF1EIfvipBGiKzgO?si=afe1574300e4471b',
        'sol': 'https://open.spotify.com/playlist/37i9dQZF1EVJSvZp5AOML2?si=e8af44981c884b25',
        'random' : 'https://open.spotify.com/playlist/37i9dQZF1EIeEGqN5vooFV?si=7669605d24e1473b',
        'quente' : 'https://open.spotify.com/playlist/37i9dQZF1EVCu9jtlIEnHS?si=bb3b97ee02e848ae',
    }

usuarios = [
    {
        'nome': 'Pedroca',
        'email': email1,
        'cidade': 'Austin',
    },
    {
        'nome': 'Jojoca',
        'email': email2,
        'cidade': 'Macae',
    }
]





for pessoa in usuarios:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={pessoa["cidade"]}&appid={chave_api}&units=metric&lang=pt'
        try:
            resposta = requests.get(url)#puxando a biblioteca 
            dados = resposta.json()#reposta da api
            temperatura = dados['main']['temp'] #puxando so a descricao do clima
            descricao = dados['weather'][0]['description']
        except:
            print('Erro na API. Analise a sua chave. Caso seja nova, aguarde ate 2(DUAS)horas para que seja ativa.')
            sys.exit()
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


        mensagem = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
                <div style="background-color: white; padding: 30px; border-radius: 10px; max-width: 500px; margin: auto;">
                <h2 style="color: #1DB954;"> Bom dia, {pessoa['nome']}!</h2>
                <p>Hoje em {pessoa['cidade']} a temperatura está <strong>{temperatura}°C</strong></p>
                <p>Clima: <em>{descricao}</em></p>
                <p>Com esse clima, sua playlist do dia é:</p>
                <a href="{link}" style="background-color: #1DB954; color: white; padding: 12px 24px; text-decoration: none; border-radius: 25px; display: inline-block;">
                ▶ Abrir Playlist no Spotify
                </a>
                <p style="color: #888; font-size: 12px; margin-top: 30px;">{frase} — {autor}</p>
                </div>
            </body>
        </html>
        """

        #enviando o email

        remetente = 'taving04@gmail.com'
        destinatario = pessoa['email']
        senha_app = os.getenv('SENHA_EMAIL')

        assunto = 'Bom dia! Playlist do dia chegando...'


        email = MIMEText(mensagem, 'html')
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