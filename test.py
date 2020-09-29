import requests

BASE= "http://127.0.0.1:5000/"

data = [{"name": "Important", "likes": 10, "views": 3},
{"name": "Hahaa", "likes": 100, "views": 31},
 {"name": "Hehee", "likes": 200, "views": 30}]


for i in range(len(data)):
    response = requests.put(BASE + "video/{}".format(i), data[i])
    print(response.json())    

response = requests.delete(BASE + "video/0")
print(response)

input()
response = requests.get(BASE + "video/2")

print(response.json())