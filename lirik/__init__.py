import requests as r
from bs4 import BeautifulSoup as bs

class search:
    def __init__(self, search):
        self.search = ''
        self.res = []
        url= f'https://www.lyricsfreak.com/search.php?q={search}'
        req = r.get(url)
        soup = bs(req.text, 'html.parser')
        for search in soup.find_all('div', class_="lf-list__cell lf-list__meta"):
            for page in search.find_all('a', class_="song"):
                self.res.append(page['href'])

    def result(self):
        result = {}
        try:
            req=r.get(f'https://www.lyricsfreak.com{self.res[0]}')
            soup = bs(req.text, 'html.parser')
            for lirik in soup.find_all('div', class_='maincont lyrics-content'):
                for hasil in lirik.find_all('div', class_='lyrictxt js-lyrics js-share-text-content'):
                    result['result'] = hasil.text
            return result['result']

        except IndexError:
            print('Lirik Tidak Ditemukan')