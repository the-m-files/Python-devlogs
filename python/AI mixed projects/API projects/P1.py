import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print("Header:", response.headers.get("date"))