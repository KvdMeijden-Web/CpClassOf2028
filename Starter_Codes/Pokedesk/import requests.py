import requests
#import json

#Variables URl and response
url = "https://v2.jokeapi.dev/joke/Programming?type=single&safe-mode"
response = requests.get(url)
#respone is Json format: needs converting to .py 
data = response.json()

print(data["joke"])
print()