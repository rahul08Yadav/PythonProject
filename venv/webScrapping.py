from bs4 import BeautifulSoup as soup
from urllib.request import urlopen  as R
url = "https://app.cpcbccr.com/AQI_India/"
client = R(url)
page_html = client.read()
client.close()
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"_3liAhj"})
#print(len(containers))container = containers[0]