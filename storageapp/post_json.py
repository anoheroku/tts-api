# Для тестирования View
import requests
import json

url = "http://127.0.0.1:8000/"
data = {'key1': 'Приходят', 'key2': 'завтра'}
headers = {'content-type': 'application/json'}
r = requests.get(url, data=json.dumps(data), headers=headers)
print(r.text)
