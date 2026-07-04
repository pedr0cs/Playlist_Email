import requests #importando a biblioteca

url = 'https://api.openweathermap.org/data/2.5/weather?q=Austin&appid=af0c2a7052e7bc31cc40265834537c3c&units=metric&lang=pt' #api de clima
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

def estilo_musical(temperatura):
    if temperatura < 15:
        return 'frio'
    elif 15 <= temperatura <= 20:
        return 'perfeito'
    elif 21 >= temperatura <= 30:
        return 'sol'
    elif temperatura > 37:
        return 'quente'
    else:
        return 'random'

estilo = estilo_musical(temperatura)

link = playlists[estilo]
print(link)