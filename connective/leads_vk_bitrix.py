import requests


class VkBitrix:

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

    def post_to_bitrix(self, host='localhost'):
        """ Отправляет новые лиды на в Birix24 по url """
        data = {'url': self.auth_to['url']}
        self.data.update(data)
        url = f'http://{host}:5001/bitrix/post'
        response = requests.post(url, json=self.data)
        return response