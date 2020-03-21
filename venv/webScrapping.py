import pandas as pd
from bs4 import BeautifulSoup
import requests

header = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}

url = r'https://www.zomato.com/bangalore/restaurants?page='

def bee(url, number,header):
    count = 1
    output = list()

    query = url + str(number)
    print(query)

    page = requests.get(query,headers = header)

    soup = BeautifulSoup(page.text, 'lxml')

    matches = soup.find_all('article',class_ = 'search-result')

    for match in matches:

        tag = match.find('div',class_ = 'row').text.strip().split(' ')[0].split('\n')[0]

        try :

            type_sub = match.find('a',class_ = 'zdark ttupper fontsize6').text

            name = match.find('a',class_ = 'result-title hover_feedback zred bold ln24 fontsize0').text.strip()

            location = match.find('a',class_ = 'ln24 search-page-text mr10 zblack search_result_subzone left').text

            address = match.find('div',class_ = 'col-m-16 search-result-address grey-text nowrap ln22').text

            rating_votes = match.find_all('div',class_ = 'ta-right floating search_result_rating col-s-4 clearfix')

            for values1 in rating_votes:
                rating = values1.find('div').text.strip()
                votes = values1.find('span').text.strip()


            bottom_detail = match.find('div',class_ = 'search-page-text clearfix row')

            cuisine_container = list()
            cuisines = bottom_detail.find_all('a')
            for values2 in cuisines:
                cuisine = values2.text
                cuisine_container.append(cuisine)

            cost_for_two = match.find_all('span',class_ = 'col-s-11 col-m-12 pl0')
            for values3 in cost_for_two:
                rupee = values3.text

            time = match.find_all('div',class_='res-timing clearfix')
            for values4 in time:
                timing = values4.text.strip()



            featured = match.find_all('div', 'col-s-11 col-m-12 pl0 search-grid-right-text')

            featuredPlace_container = list()


            for values5 in featured:
                featuredPlace = values5.text.strip()
                featuredPlace_container.append(featuredPlace)

            output.append([name,tag,type_sub,location,address,rating,votes,cuisine_container,rupee,timing,featuredPlace_container])
            count += 1
        except:
            print("Error data not fetched")
    return output


my_list_of_details = list()

for i in range(935):
    reception = bee(url,i,header)
    my_list_of_details.append(reception)


combining = list()

for i in my_list_of_details:
    for values in i:
        combining.append(values)

column_names = ['Name', 'Tag', 'Type', 'Location', 'Address', 'Rating',
                'Votes', 'Cuisines', 'Cost for 2','Timing','Features']
df = pd.DataFrame(combining,columns=column_names)
df.to_excel('Zomato_data.xlsx')