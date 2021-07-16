import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.weather.go.kr/weather/observation/currentweather.jsp")
soup = BeautifulSoup(response.content, 'html.parser')


table = soup.find('table', {'class': 'table_develop3'})
data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))

    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([point, temperature, humidity])


for a, b, c in data:
    print("지역 : {}, 기온 : {}, 습도 : {}".format(f'{a:^5}', f'{b:^5}', f'{c:^5}'))
