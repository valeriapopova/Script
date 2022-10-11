import json

import requests


class BitrixTelegram:

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

    def post_to_tg(self, host='api.ecomru.ru'):
        """ Отправляет новые лиды в телеграм чат
        (принимает на вход chat_id, узнать его можно у бота @LeadsFromVk написав /start)
        """
        self.data.update(json.loads(self.auth_to))
        url_for_tg = f'http://{host}:49601/telegram/post'
        response = requests.post(url_for_tg, json=self.data)
        return response