import requests

BASE= "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"name": "Fyr", "likes": 10, "views": 3})

print(response.json())

input()

response = requests.delete(BASE + "video/3")
input()

response = requests.get(BASE + "video/6")
print(response.json())