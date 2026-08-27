#The exam01 is 

import requests

url = 'https://api.github.com/users/torvalds'

response = requests.get(url)

data = response.json()

print(type(data))
print(data)
print(data['followers'])