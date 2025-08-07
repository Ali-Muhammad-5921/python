import requests
import json

query = input('What type of news you are interested in ?')
url = f'https://newsapi.org/v2/everything?q={query}&from=2025-08-07&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226s94865f7a7'# api key goes here
r = requests.get(url)

news = json.loads(r.text)
# print(news, type(news))

for atricle in news['articles']:
    print(news['title'])
    print(news['description'])
    print('---------------------------------------'.center(50))