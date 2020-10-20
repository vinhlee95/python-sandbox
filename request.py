"""
Using external Request library to handle API requests
"""
import requests
import pathlib

# 🛠 GET request
# response = requests.get('https://api.github.com/events')
# print(response.status_code)
# print(response.json())

# 🛠 POST request
url = 'https://httpbin.org/post'
# payload = {"foo": "bar", "hello": 1}
# r = requests.post(url, data=payload)
# print(r.status_code, r.json()["form"])

# 🛠 POST a multip-part encoded file
current_path = pathlib.Path(__file__).parent.absolute()
files = {"file": open(f"{current_path}/file/data.json", 'rb')}
# r = requests.post(url, files = files)
# print(r.status_code, r.json()['files'], r.json()['headers']['Content-Type'])