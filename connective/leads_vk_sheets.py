import json

import requests


class VkSheets:

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

    def append_values_into_sheets(self, host='api.ecomru.ru'):
        """ Добавляет только значения в google sheets"""
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5001/google_sheets/append_values'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def append_into_sheets(self, host='api.ecomru.ru'):
        """ Добавляет данные в таблицу google sheets """
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5001/google_sheets/append'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def clear_append_into_sheets(self, host='api.ecomru.ru'):
        """ Перезаписывает данные в таблицу google sheets   """
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5001/google_sheets/clear_append'
        response = requests.post(url_for_sheets, json=self.data)
        return response

    def append_new_list(self, host='api.ecomru.ru'):
        """ Добавляет данные в новый лист google sheets  """
        self.data.update(json.loads(self.auth_to))
        url_for_sheets = f'http://{host}:5001/google_sheets/append_list'
        response = requests.post(url_for_sheets, json=self.data)
        return response
