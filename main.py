from pprint import pprint

from config import *
import requests


def get_data_from_vk(token, age_from, age_to, sex, city , count):
    """ Забирает данные из vk по критериям поиска """
    url_for_vk = 'http://127.0.0.1:5000/vk/search_users'
    data_for_vk = {'token': token, 'age_from': age_from, 'age_to': age_to, 'sex': sex, 'city': city, 'count': count}
    r = requests.post(url_for_vk, data=data_for_vk)
    res = r.json()
    #res.update(auth_dict)
    return res


def get_leads_from_vk():
    """ Забирает новые лиды из vk """
    vk_url = 'http://127.0.0.1:5000/vk/756630756e645f336173313372545444'
    r = requests.post(vk_url)
    res = r.json()
    #res.update(auth_dict)
    return res


def append_values_into_sheets(res):
    """ Добавляет только значения в google sheets"""
    url_for_sheets = 'http://127.0.0.1:5001/sheets/append_values'
    response = requests.post(url_for_sheets, json=res)
    return response


def append_into_sheets(res):
    """ Добавляет данные в таблицу google sheets """
    url_for_sheets = 'http://127.0.0.1:5001/sheets/append'
    response = requests.post(url_for_sheets, json=res)
    return response


def clear_append_into_sheets(res):
    """ Перезаписывает данные в таблицу google sheets   """
    url_for_sheets = 'http://127.0.0.1:5001/sheets/clear_append'
    response = requests.post(url_for_sheets, json=res)
    return response


def append_new_list(res):
    """ Добавляет данные в новый лист google sheets  """
    url_for_sheets = 'http://127.0.0.1:5001/sheets/append_list'
    response = requests.post(url_for_sheets, json=res)
    return response


def append_into_excel(res):
    """ Добавляет данные в excel """
    url_for_excel = 'http://127.0.0.1:5001/excel'
    response = requests.post(url_for_excel, json=res)
    return response


def post_to_tg(res, chat_id):
    """ Отправляет новые лиды в телеграм чат
    (принимает на вход chat_id, узнать его можно у бота @LeadsFromVk написав /start)
    """
    chat_id_data = {'chat_id': chat_id}
    res.update(chat_id_data)
    url_for_tg = 'http://127.0.0.1:5001/telegram'
    response = requests.post(url_for_tg, json=res)
    return response


def post_email(res, email):
    """ Отправляет новые лиды на указанную почту"""
    data = {'to': email}
    res.update(data)
    url = 'http://127.0.0.1:5001/email/post'
    response = requests.post(url, json=res)
    return response


def post_to_bitrix(res, url):
    """ Отправляет новые лиды на в Birix24 по url """
    data = {'url': url}
    res.update(data)
    url = 'http://127.0.0.1:5001/bitrix/post'
    response = requests.post(url, json=res)
    return response



# res = get_leads_from_vk()
# post_to_tg(res, 390939831)
