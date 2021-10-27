import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#themecast > div.theme_cont > div:nth-child(2) > div > ul > li:nth-child(2) > a.theme_info > strong').get_text()
    print(title)
    #print(title.get_text())
else : 
    print(response.status_code)