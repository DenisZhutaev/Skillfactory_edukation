from os import name

import requests
import re
from bs4 import BeautifulSoup


def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])
    return links


def main():
    url = "https://coffeestate.ru/"

    links = get_links(url)
    print(links)


if name == 'main':
    main()
