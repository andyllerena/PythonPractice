import requests

url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    result = {}

    for post in data:
        post_id = post["postId"]
        email = post["email"]

        if post_id not in result:
            result[post_id] = set()

        result[post_id].add(email)

    print(result)
else:
    print("Error:", response.status_code)
