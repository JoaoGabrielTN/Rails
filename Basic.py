#! /usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re

pages = set()

def getLinks(pageUrl):
    global pages
    try:
        html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    except HTTPError as e:
        print('Page not found! Stopping')
        return None

    bs = BeautifulSoup(html, 'html.parser')

    # Pode ser que não haja nenhuma tag a ou nenhuma tag a com href=regex
    # preciso adicionar um tratamneto de erro aqui.

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')
