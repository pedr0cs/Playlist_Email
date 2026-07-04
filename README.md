#Playlist Email
Script em Python que busca o clima em tempo real e envia um email personalizado toda manhã com uma playlist do Spotify de acordo com a temperatura — porque sua música deve refletir o seu dia.

##Como funciona
1. Busca o clima atual da cidade de cada usuário via OpenWeather API
2. Define playlist baseado na temperatura
3. Busca uma frase motivacional aleatória via ZenQuotes API
4. Envia um email HTML personalizado com a playlist do Spotify e a frase do dia

##Tecnologias
- Python 3
- requests — consumo de APIs externas
- smtplib — envio de emails
- python-dotenv — proteção de chaves e dados sensíveis
- OpenWeather API — dados de clima em tempo real
- ZenQuotes API — frases motivacionais

## Como rodar
1. Clone o repositório
2. Instale as dependências:
```bash
pip install requests python-dotenv
```
3. Crie um arquivo `.env` com suas credenciais:
4. 4. Rode o script:
```bash
python Emails.py
```

## Dificuldades reais que tive

- Entender que indentação em Python não é só estética — ela define o que está dentro ou fora de um bloco, e errar isso faz o código se comportar de formas inesperadas.
- Aprendi na prática que nunca se deve subir senhas e chaves de API pro GitHub, e como usar `.env` e `.gitignore` pra proteger dados sensíveis.
- Tive meu primeiro contato real com consumo de APIs externas, navegando dentro de JSONs aninhados pra extrair exatamente o dado que precisava.

## Status
Projeto concluído — parte de uma série semanal de estudo em Python.
