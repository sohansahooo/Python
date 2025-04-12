import requests  # pip install requests

query = input("What type of news are you interested in today? ")
api = "dbe57b028aeb41e285a226a94865f7a7"

url = ""

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
