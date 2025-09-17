import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    result = {}

    for user in data:
        name = user["name"]
        age = user.get("age")

        if age is not None:
            if name not in result:
                result[name] = []
            result[name].append(age)

    print(result)
else:
    print("Error:", response.status_code)
