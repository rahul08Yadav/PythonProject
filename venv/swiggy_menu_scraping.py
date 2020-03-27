import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import  urlopen as uReq
import requests
bangalore_links = pd.read_csv(r'/home/rahul/PythonProject/venv/bangalore_links.csv')
a = bangalore_links['links'].tolist()
#print(len(a))
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
def bee(url, header):
    try:
        query = url
        page = requests.get(query, headers=header)
        output = list()
        print(query)

        soup = BeautifulSoup(page.text, 'html.parser')
        restuarant = soup.find('div', class_='_1637z')

        res_name = restuarant.find('div', class_='OEfxz').text

        # print(res_name)

        matches = soup.find('div', class_='_1hM1R znxoh')
        heading = matches.find_all('div', class_='_2dS-v')
        for j in heading:

            items = j.find_all('div', class_='_2wg_t')
            try:
                types = j.find('h2', class_='M_o7R _27PKo').text
            except:
                types = j.find('h2', class_='M_o7R').text

            # print(types,".....\n")
            for k in items:
                try:
                    name = k.find('div', class_='jTy8b').text
                except:
                    print('hi11')
                try:
                    price = k.find('div', class_='_12lpv MwITc').text
                    price = '₹' + price
                except:
                    print('hi2')
                    # print(name,'\nRs=',price)
                output.append([res_name, types, name, price])
                # print(output)
    except:
        print("page not found")
    return output


combining = list()
my_list_of_details = list()
for url in a:
    reception = bee(url, header)
    # print(reception)
    my_list_of_details.append(reception)
for i in my_list_of_details:
    for values in i:
        combining.append(values)

# print(my_list_of_details)
column_names = ['res_name','Food_types','Cuisine_name', 'price']
df = pd.DataFrame(combining, columns=column_names)
print(df.shape)
df.to_csv('Swiggy_menu_data.csv')
