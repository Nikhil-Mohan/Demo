import requests

response = requests.get("https://github.com/Nikhil-Mohan/Demo/")
print(response.status_code)
print(response.json())
