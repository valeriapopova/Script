from config import *
import requests


def get_search_data_from_vk(token, age_from, age_to, sex, city , count, host='localhost'):
    """ Забирает данные из vk по критериям поиска """
    url_for_vk = f'http://{host}:5000/vk/search_users'
    data_for_vk = {'token': token, 'age_from': age_from, 'age_to': age_to, 'sex': sex, 'city': city, 'count': count}
    r = requests.post(url_for_vk, data=data_for_vk)
    res = r.json()
    return res


def get_leads_from_vk(host='localhost'):
    """ Забирает новые лиды из vk """
    vk_url = f'http://{host}:5000/vk/get_leads'
    r = requests.post(vk_url)
    res = r.json()
    return res
