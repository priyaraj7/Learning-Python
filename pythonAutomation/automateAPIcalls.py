import requests
import json

baseUrl = "https://api.upcitemdb.com/prod/trial/lookup"
# dictionary with key = upc, value= 0012993441012
parameters = {"upc": "0012993441012"}

response = requests.get(baseUrl, params=parameters)
print(response.url)
content = response.content

# convert json to dictionary
info = json.loads(content)
print(type(info)) # <class 'dict'>
# print(info)
item = info["items"]
itemInfo = item[0]
title = itemInfo["title"]
brand = itemInfo["brand"]
print(title)
print(brand)

