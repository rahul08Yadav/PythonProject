import pandas as pd
import requests
from bs4 import BeautifulSoup
links = pd.read_csv(r'/home/rahul/Documents/Zomato_place_links.csv',index_col=0)
links.rename(columns={'0':'restuarant_links'},inplace=True)
url=links['restuarant_links'].tolist()
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
def scrape(url_link,header):
    ul = url_link + '/order'
    print(ul)
    box = list()
    try:
        page = requests.get(ul,headers = header)
        soup = BeautifulSoup(page.text,'html.parser')
        a = soup.find('main')
        restuarant_name = a.find('h1').text
        cuisine_name = a.find_all('h4',class_='sc-1s0saks-11 cDXzZl')
        price = a.find_all('span',class_='sc-17hyc2s-1 fnhnBd')
        for k in range(len(cuisine_name)):
            price1 = price[k].text
            cuisine_name1 = cuisine_name[k].text
            box.append([restuarant_name,cuisine_name1,price1])
    except:
        print('page not found')

    return box
all_menu = list()
for i in url:
    res_menu = scrape(i,header)
    all_menu.append(res_menu)
combining = list()
for i in all_menu:
    for values in i:
        combining.append(values)
column_names = ['res_name','Cuisine_name', 'price']
df = pd.DataFrame(combining, columns=column_names)
print(df.shape)
df.to_csv('Zomato_menu_list.csv')