import requests

url = "https://api.quotable.io/random"

response = requests.get(url)
data = response.json()

print("Quote:")
print(data["content"])
print("- " + data["author"])
