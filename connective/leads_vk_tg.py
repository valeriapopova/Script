import json

import requests


class VkTelegram:

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

    def post_to_tg(self, host='api.ecomru.ru'):
        """ Отправляет новые лиды в телеграм чат
        (принимает на вход chat_id, узнать его можно у бота @LeadsFromVk написав /start)
        """
        self.data.update(json.loads(self.auth_to))
        url_for_tg = f'http://{host}:49601/telegram/post'
        response = requests.post(url_for_tg, json=self.data)
        return response


# new = VkTelegram(auth_from=None, auth_to={'chat_id': 390939831})
# new.get_leads_from_vk()
# new.post_to_tg()