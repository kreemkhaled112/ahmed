import requests

url = 'https://raw.githubusercontent.com/kreemkhaled112/add/main/AddMeFast%20v2.py'
response = requests.get(url)

with open('AddMeFast v2.py', 'wb') as f:
    f.write(response.content)