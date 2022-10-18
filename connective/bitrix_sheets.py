import json
from pprint import pprint

import requests


class BitrixSheets:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def get_leads_bitrix(self, host='localhost'):
        """ Забирает новые лиды из Birix24  """
        url = f'http://{host}:5001/bitrix/get_leads'
        r = requests.post(url, json=json.loads(self.auth_from))
        self.data = r.json()
        print(self.data)
        return self.data

    def get_contacts_list_bitrix(self, host='localhost'):
        """ Забирает все контакты из Birix24  """
        url = f'http://{host}:5001/bitrix/get_contact_list'
        r = requests.post(url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def append_values_into_sheets_b(self, host='api.ecomru.ru'):
        """ Добавляет только значения в google sheets"""
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5000/google_sheets/append_values'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def append_into_sheets_b(self, host='api.ecomru.ru'):
        """ Добавляет данные в таблицу google sheets """
        self.data.update(json.loads(self.auth_to))
        pprint(self.data)
        url_for_sheets = f'http://{host}:5000/google_sheets/append'
        response = requests.post(url_for_sheets, json=self.data)

        return response

    def clear_append_into_sheets_b(self, host='api.ecomru.ru'):
        """ Перезаписывает данные в таблицу google sheets   """
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5000/google_sheets/clear_append'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def append_new_list_b(self, host='api.ecomru.ru'):
        """ Добавляет данные в новый лист google sheets  """
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5000/google_sheets/append_list'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def update_row(self, host='api.ecomru.ru'):
        """ Обновляет строку """
        self.data.update(self.auth_to)
        url_for_sheets = f'http://{host}:5001/google_sheets/update_row'
        response = requests.post(url_for_sheets, json=self.data)
        return response
