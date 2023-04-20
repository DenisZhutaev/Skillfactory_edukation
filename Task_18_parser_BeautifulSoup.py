from bs4 import BeautifulSoup
import requests


def main():
    base = 'https://ru.stackoverflow.com'
    html = requests.get(base).content
    soup = BeautifulSoup(html, 'lxml')

    h3 = soup.find_all('h3', class_='s-post-summary--content-title')

    for elem in h3:
        a = elem.find('a', class_='s-link')
        print(a.getText(), base + a.get('href'))


if __name__ == '__main__':
    main()
