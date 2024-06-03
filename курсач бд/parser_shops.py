import requests
import json

#ASOS

url = "https://asos2.p.rapidapi.com/products/v2/list"
querystring = {
    "store": "US",
    "offset": "0",
    "categoryId": "4209",
    "limit": "10",
    "country": "US",
    "currency": "USD",
    "sizeSchema": "US",
    "lang": "en-US"
}
headers = {
    "X-RapidAPI-Key": "1cd43b303dmsh03776ef74d12bb2p19423bjsn6841ef679123",
    "X-RapidAPI-Host": "asos2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

with open('asos.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

#HM

url = "https://apidojo-hm-hennes-mauritz-v1.p.rapidapi.com/products/list"
querystring = {
    "currentpage": "1",
    "pagesize": "10",
    "categories": "ladies_all",
    "country": "us",
    "lang": "en"
}
headers = {
    "X-RapidAPI-Key": "1cd43b303dmsh03776ef74d12bb2p19423bjsn6841ef679123",
    "X-RapidAPI-Host": "apidojo-hm-hennes-mauritz-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

#KOHLS

url = "https://kohls.p.rapidapi.com/products/list"

querystring = {"limit":"24","offset":"1","dimensionValueID":"AgeAppropriate:Teens"}

headers = {
	"X-RapidAPI-Key": "1cd43b303dmsh03776ef74d12bb2p19423bjsn6841ef679123",
	"X-RapidAPI-Host": "kohls.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
    
with open('kohls.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)