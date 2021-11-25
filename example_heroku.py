from requests import post as p

username = input('Enter a username: ')

while True:
    query = input(f'{username}: ')
    r = p(f'https://mychatbotapp.herokuapp.com/?query={query}')
    print('Bot:', r.json()['response']['bot'])
