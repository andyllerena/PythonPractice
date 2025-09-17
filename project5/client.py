import requests

url = "http://127.0.0.1:5001/add"
payload = {"a" : 5, "b" : 7}
response = requests.post(url,json=payload)
print(response.json())