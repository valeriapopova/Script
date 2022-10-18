
import json
from pprint import pprint

import requests


class BitrixEmail:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def webhook_bitrix(self, host='localhost'):
        """ Callback """
        key = self.auth_from['key']
        url = f'http://{host}:5001/bitrix/webhook/{key}'
        r = requests.post(url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def get_leads_bitrix(self, host='localhost'):
        """ Забирает все лиды из Birix24  """
        url = f'http://{host}:5001/bitrix/get_leads'
        r = requests.post(url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def get_contacts_list_bitrix(self, host='localhost'):
        """ Забирает все контакты из Birix24  """
        url = f'http://{host}:5001/bitrix/get_contact_list'
        r = requests.post(url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def post_email(self, host='api.ecomru.ru'):
        """ Отправляет новые лиды на указанную почту"""
        self.data.update(json.loads(self.auth_to))
        url = f'http://{host}:49665/email/post'
        response = requests.post(url, json=self.data)
        return response