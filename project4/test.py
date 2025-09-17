import requests
url = "https://official-joke-api.appspot.com/types"
response = requests.get(url)
types = response.json()
print(types)

for t in types:
    print('-',t)