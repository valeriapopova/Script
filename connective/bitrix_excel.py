import json
from pprint import pprint

import requests


class BitrixExcel:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def get_leads_bitrix(self, host='localhost'):
        """ Забирает все лиды из Birix24  """
        url = f'http://{host}:5001/bitrix/get_leads'
        r = requests.post(url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def append_into_excel(self, host='api.ecomru.ru'):
        """ Добавляет данные в excel """
        url_for_excel = f'http://{host}:63880/excel/post'
        response = requests.post(url_for_excel, json=self.data)
        return response