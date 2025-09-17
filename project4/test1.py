import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    result = {}
   

    for post in data:
        user_id = post["userId"]
        
        if user_id not in result:
            result[user_id] = 0
        result[user_id] += 1

    print(result)