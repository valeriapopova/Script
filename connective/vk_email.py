import json

import requests


class VkEmail:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def webhook_vk(self, host='api.ecomru.ru'):
        """Callback запросы"""
        key = self.auth_from['key']
        vk_url = f'http://{host}:5000/vk/online_notification/{key}'
        r = requests.post(vk_url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def post_email(self, host='api.ecomru.ru'):
        """ Отправляет новые лиды на указанную почту"""
        self.data.update(json.loads(self.auth_to))
        url = f'http://{host}:49665/email/post'
        response = requests.post(url, json=self.data)
        return response
