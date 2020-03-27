import pandas as pd
from bs4 import BeautifulSoup
import requests

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}

url_half = r'https://www.zomato.com/bangalore/'

df = pd.read_excel(r'/home/rahul/PythonProject/venv/Zomato_data.xlsx', index_col=0)
df_nodup = df.drop_duplicates(keep='first', inplace=False)

name_list = df_nodup.loc[:, 'Name'].drop_duplicates(keep='first', inplace=False).tolist()

# for k in res_location:
#     k = k.split(', ',1)
#     try:
#         k = k[1]
#     except:
#         k=k[0]
#     rah.append(k)
import numpy as np

data = df_nodup.drop(df_nodup.index[np.where(df_nodup.index > 1)[0]])

my_list_of_details = list()
combining = list()


def bee(url, header, restuarant):
    output = list()

    query = url
    print(query)
    page = requests.get(query, headers=header)
    soup = BeautifulSoup(page.text, 'lxml')
    # print(page.status_code)
    if (page.status_code == 200):
        print(200)
        matches = soup.find('div',class_='sc-1mo3ldo-0 sc-hMrMfs jbPPsX')
        print(matches)
        # sections = matches.find('section',class_='sc-drlKqa bWNevV')
        # print(sections)
        # x=sections.find('section',class_='sc-sPYgB fqXAxF')
        # print(x)
       # x =sections.find('section',class_='sc-LAuEU gVORAB')
        #print(x)
        #for match in x:
           # print('a')
            #name = match.find_all('h4', class_="sc-1s0saks-11 cDXzZl").text
            # for j in name:
            #     output.append([restuarant, j, 'a'])
        # price = match.find('span',class_ = "sc-17hyc2s-1 fnhnBd")

        return output
    else:
        print("Page not scraped")


for i in name_list:
    restuarant = data[data['Name'] == i]
    restuarant.set_index('Name', inplace=True)
    res_location = restuarant.loc[:, 'Location'].tolist()
    r = i.lower().replace("'", "").replace(' - ', ' ').replace(' ', '-')
    for j in res_location:
        y = j.lower().replace(' ', '-')
        url = url_half + r + '-' + y
        page1 = requests.get(url, headers=header)
        if (page1.status_code == 404):
            url = url + '-bangalore'
        else:
            pass
        reception = bee(url, header, restuarant)
        my_list_of_details.append(reception)

for i in my_list_of_details:
    for values in i:
        combining.append(values)
column_names = ['Restuarant-Name', 'Cuisine', 'Price']
df = pd.DataFrame(combining, columns=column_names)
df.to_csv('zomato_menu.csv')