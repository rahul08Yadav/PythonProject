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
        res_type = restuarant.find('div', class_='_3Plw0 JMACF').text
        res_name = restuarant.find('div', class_='OEfxz').text
        location = restuarant.find('div', class_='Gf2NS _2Y6HW').text
        # print(res_name)

        matches = soup.find('div', class_='_1hM1R znxoh')
        rating_data = list()
        rating = restuarant.find('div', class_='_2l3H5').text
        rating_data.append(rating + '*')
        total_rating = restuarant.find('span', class_='_1iYuU').text
        rating_data.append(total_rating)

        cost_2 = restuarant.find_all('div', class_='_2l3H5')
        r = 0
        for z in cost_2:
            if (r == 2):
                cost_for_2 = z.text
            r += 1
        offer = restuarant.find('div', class_='_3lvLZ').text

                    # print(name,'\nRs=',price)
        output.append([res_name, res_type[1:], rating_data, cost_for_2, location, offer])
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
column_names = ['res_name', 'res_type', 'rating_data', 'cost_for_2', 'Location', 'Offer']
df = pd.DataFrame(combining, columns=column_names)
print(df.shape)
df.to_csv('Swiggy_restuarant_data.csv')
