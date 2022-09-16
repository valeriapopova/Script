import json

import requests


class VkSheets:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def get_leads_from_vk(self, host='localhost'):
        """ Забирает новые лиды из vk """
        vk_url = f'http://{host}:5000/vk/get_leads'
        r = requests.post(vk_url)
        self.data = r.json()
        return self.data

    def append_values_into_sheets(self, host='localhost'):
        """ Добавляет только значения в google sheets"""
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5001/sheets/append_values'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def append_into_sheets(self, host='localhost'):
        """ Добавляет данные в таблицу google sheets """
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5001/sheets/append'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def clear_append_into_sheets(self, host='localhost'):
        """ Перезаписывает данные в таблицу google sheets   """
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5001/sheets/clear_append'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def append_new_list(self, host='localhost'):
        """ Добавляет данные в новый лист google sheets  """
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5001/sheets/append_list'
        response = requests.post(url_for_sheets, json=self.data)
        return response
