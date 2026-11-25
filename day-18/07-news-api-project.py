# News Api Prject 2 in python


import requests
import json

query = input("What type of news are you interested in?")

url = f"Here i was using my api"


r = requests.get(url)
news = json.loads(r.text)

# print(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
