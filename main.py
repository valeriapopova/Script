from pprint import pprint

from config import *
import requests as requests


url_for_vk = 'http://127.0.0.1:5000/vk/search_users'
data_for_vk = {'token': token, 'age_from': age_from, 'age_to': age_to, 'sex': sex, 'city': city, 'count': count}
r = requests.post(url_for_vk, data=data_for_vk)
res = r.json()
res.update(auth_dict)
pprint(res)

''' Добавляет только значения в google sheets'''
url_for_sheets = 'http://127.0.0.1:5001/sheets/append_values'
response = requests.post(url_for_sheets, json=res)
print(response)

''' Добавляет данные в таблицу google sheets '''
url_for_sheets = 'http://127.0.0.1:5001/sheets/append'
response = requests.post(url_for_sheets, json=res)
print(response)

''' Перезаписывает данные в таблицу google sheets   '''
url_for_sheets = 'http://127.0.0.1:5001/sheets/clear_append'
response = requests.post(url_for_sheets, json=res)
print(response)

''' Добавляет данные в новый лист google sheets  '''
url_for_sheets = 'http://127.0.0.1:5001/sheets/append_list'
response = requests.post(url_for_sheets, json=res)
print(response)

''' Добавляет данные в excel  '''
url_for_excel = 'http://127.0.0.1:5001/excel'
response = requests.post(url_for_excel, json=res)
print(response)