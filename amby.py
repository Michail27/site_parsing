import requests
from bs4 import BeautifulSoup

response = requests.get('http://amdy.su/')
html_data = BeautifulSoup(response.text)
# print(html_data)
quotes = html_data.find_all(class_='read-more')

# print(quotes)
for quote in quotes:
    q = quote.find('a')
    # print(q['href'])
    response2 = requests.get(q['href'])
    html_data2 = BeautifulSoup(response2.text)
    # print(html_data2)
    quotes2 = html_data2.find_all('div', class_='entry-content')
    for quote2 in quotes2:
        q = quote2.get_text()
        print(q)
        print()