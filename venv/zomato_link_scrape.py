import pandas as pd
from bs4 import BeautifulSoup
import requests

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
places = ['yelahanka', 'whitefield', 'marathahalli', 'yeshwantpur', 'malleshwaram']
pages = [24, 69, 73, 32, 54]
res_links = list()
c = 0
for z in places:
    url_half = r'https://www.zomato.com/bangalore/delivery-in-' + z + '?page='
    for y in range(1, pages[c]):
        url = url_half + str(y)

        page = requests.get(url, headers=header)
        soup = BeautifulSoup(page.text, 'html.parser')
        h = soup.find('section')
        i = h.find_all('div', class_="col-l-16")[1]

        j = i.find('div', class_='row')
        k = j.find_all('div', class_='card search-snippet-card search-card')
        for aa in k:
            ki = aa.find('div', class_='col-s-12')
            l = ki.find('a', class_='result-title hover_feedback zred bold ln24 fontsize0')
            link = l.attrs['href']
            res_links.append(link)

    c += 1

data = pd.DataFrame(res_links)
data.to_csv('Zomato_place_links.csv')