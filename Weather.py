import requests
import os
os.environ["http_proxy"] = "http://ID:Pass@Proxy:port"

url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
query_params = {'city': '130010'}
data = requests.get(url, params=query_params).json()
location = data['location']
print(location['city'])
#print(location['name'])
for weather in data['forecasts']:
        print(weather['dateLabel'] + 'の天気：' + weather['telop'])
