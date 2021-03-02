import requests
from bs4 import BeautifulSoup


def pars_country():
    response = requests.get('https://www.officeholidays.com/countries')
    html_data = BeautifulSoup(response.text)
    quotes = html_data.find_all('div', class_='four omega columns')
    list_country = []
    for colums in quotes:
        for colum in colums.find_all('a'):
            list_country.append(colum.text[2:])
    print(len(list_country))
    save_file(list_country)


def save_file(list_writer):
    with open('cantry.txt', 'w', encoding='utf-8') as f:
        for country in list_writer:
            f.write(country + '\n')


pars_country()