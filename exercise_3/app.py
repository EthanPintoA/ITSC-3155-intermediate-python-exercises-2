import requests

r = requests.get("https://www.charlotte.edu/")

print(r.text)
