import json
from pprint import pprint
from config import *
import requests as requests

age_from = 18
age_to = 20
sex = 1
city = 'москва'
count = 20

url_for_vk = 'http://127.0.0.1:5000/vk/search_users'
data_for_vk = {'token': token, 'age_from': age_from, 'age_to': age_to, 'sex': sex, 'city': city, 'count': count}
r = requests.post(url_for_vk, data=data_for_vk)
res = r.json()
res.update(auth_dict)
# pprint(res)
headers = {"Content-Type": "application/json"}
# url_for_sheets = 'http://127.0.0.1:5001/sheets/json'
# response = requests.post(url_for_sheets, headers=headers, data=res)
# print(response)

with open('example.json', 'w') as file:
    json.dump(res, file, ensure_ascii=False, indent=3)


# url_for_excel = 'http://127.0.0.1:5001/excel'
# response = requests.post(url_for_excel, data='example.json')
# print(response)