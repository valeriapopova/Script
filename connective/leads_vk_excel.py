import json

import requests


class VkExcel:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def get_targeting(self, host='localhost'):
        """Возвращает параметры таргетинга рекламных объявлений"""
        url = f'http://{host}:5000/vk/ads_get_targeting'
        r = requests.post(url, json=json.loads(self.auth_from))
        res = r.json()
        return res

    def get_flood_stats(self, host='localhost'):
        """Возвращает подробную статистику по охвату рекламных записей из объявлений и кампаний для
            продвижения записей сообщества."""
        url = f'http://{host}:5000/vk/ads_get_flood_stats'
        r = requests.post(url, json=json.loads(self.auth_from))
        res = r.json()
        return res

    def get_leads_from_vk(self, host='localhost'):
        """ Забирает новые лиды из vk """
        vk_url = f'http://{host}:5000/vk/get_leads'
        response = requests.post(vk_url, json=self.auth_from)
        self.data = response.json()
        print(self.data)
        return self.data

    def append_into_excel(self, host='api.ecomru.ru'):
        """ Добавляет данные в excel """
        url_for_excel = f'http://{host}:63880/excel/post'
        response = requests.post(url_for_excel, json=self.data)
        return response



# new = VkExcel(auth_from=None, auth_to=None)
# new.get_leads_from_vk()
# new.append_into_excel()