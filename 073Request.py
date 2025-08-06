import requests
# from bs4 import BeautifulSoup
# request module allows us to use get, post, put and delete methods and also bs4
#  bs4 is called beautiful soup method 

url = '' 
 
respone = requests.get(url)

# print(respone.text) it will display the contents of response

# soup = BeautifulSoup(response.text , 'html.parse')
#print(soup.prettify())

