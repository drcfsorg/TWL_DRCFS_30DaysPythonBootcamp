import requests

response = requests.get('https://www.google.com/')
print(response.text)