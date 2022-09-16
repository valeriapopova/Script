import json

import requests


class VkEmail:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def get_leads_from_vk(self, host='api.ecomru.ru'):
        """ Забирает новые лиды из vk """
        vk_url = f'http://{host}:5000/vk/get_leads'
        r = requests.post(vk_url)
        self.data = r.json()
        return self.data

    def post_email(self, host='api.ecomru.ru'):
        """ Отправляет новые лиды на указанную почту"""
        self.data.update(json.loads(self.auth_to))
        url = f'http://{host}:49665/email/post'
        response = requests.post(url, json=self.data)
        return response
