import json

import requests


class VkBitrix:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def get_leads_from_vk(self, host='localhost'):
        """ Забирает новые лиды из vk """
        vk_url = f'http://{host}:5000/vk/get_leads'
        r = requests.post(vk_url, json=self.auth_from)
        self.data = r.json()
        return self.data

    def webhook_vk(self, host='api.ecomru.ru'):
        """Callback запросы"""
        key = self.auth_from['key']
        vk_url = f'http://{host}:5000/vk/online_notification/{key}'
        r = requests.post(vk_url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def post_to_bitrix(self, host='localhost'):
        """ Отправляет новые лиды в Birix24 по url """
        self.data.update(json.loads(self.auth_to))
        url = f'http://{host}:5001/bitrix/post'
        response = requests.post(url, json=self.data)
        return response

    def post_new_contact_to_bitrix(self, host='localhost'):
        """ Отправляет новые контакты в Birix24 по url """
        self.data.update(json.loads(self.auth_to))
        url = f'http://{host}:5001/bitrix/new_contact'
        response = requests.post(url, json=self.data)
        return response

    def new_feed_mess_to_bitrix(self, host='localhost'):
        """ Отправляет сообщение в ленту в Birix24 по url """
        self.data.update(json.loads(self.auth_to))
        url = f'http://{host}:5001/bitrix/feed_message'
        response = requests.post(url, json=self.data)
        return response

    def new_deal_to_bitrix(self, host='localhost'):
        """Создает новую сделку"""
        self.data.update(json.loads(self.auth_to))
        url = f'http://{host}:5001/bitrix/new_deal'
        response = requests.post(url, json=self.data)
        return response