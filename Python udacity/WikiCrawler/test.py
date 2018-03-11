import requests

response = requests.get('https://en.wikipedia.org/wiki/Kreayshawn')

print(response.text.encode("utf-8"))
print(type(response.text))
