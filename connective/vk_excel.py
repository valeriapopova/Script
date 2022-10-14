import json

import requests


class VkExcel:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def get_budget(self, host='api.ecomru.ru'):
        """Возвращает текущий бюджет рекламного кабинета."""
        vk_url = f'http://{host}:5000/vk/ads_get_budget'
        r = requests.post(vk_url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def get_targeting(self, host='localhost'):
        """Возвращает параметры таргетинга рекламных объявлений"""
        url = f'http://{host}:5000/vk/ads_get_targeting'
        r = requests.post(url, json=self.auth_from)
        self.data = r.json()
        return self.data

    def get_flood_stats(self, host='localhost'):
        """Возвращает подробную статистику по охвату рекламных записей из объявлений и кампаний для
            продвижения записей сообщества."""
        url = f'http://{host}:5000/vk/ads_get_flood_stats'
        r = requests.post(url, json=self.auth_from)
        self.data = r.json()
        print(self.data)
        return self.data

    def webhook_vk(self, host='api.ecomru.ru'):
        """Callback запросы"""
        key = self.auth_from['key']
        vk_url = f'http://{host}:5000/vk/online_notification/{key}'
        r = requests.post(vk_url, json=json.loads(self.auth_from))
        self.data = r.json()
        return self.data

    def get_month_statistic(self, host='localhost'):
        """Выгружается информация по расходам, просмотрам и кликам за последние 30 дней."""
        url = f'http://{host}:5000/vk/ads_get_month_statistic'
        r = requests.post(url, json=json.loads(self.auth_from))
        res = r.json()
        return res

    def get_statistic_current_day(self, host='localhost'):
        """Выгружается информация по расходам, просмотрам и кликам за текущий день."""
        url = f'http://{host}:5000/vk/ads_get_statistic_current_day'
        r = requests.post(url, json=json.loads(self.auth_from))
        res = r.json()
        return res

    def get_statistic_yesterday(self, host='localhost'):
        """Выгружается информация по расходам, просмотрам и кликам за вчерашний день. """
        url = f'http://{host}:5000/vk/ads_get_statistic_yesterday'
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

    def append_into_excel(self, host='localhost'):
        """ Добавляет данные в excel """
        url_for_excel = f'http://{host}:63880/excel/post'
        response = requests.post(url_for_excel, json=self.data)
        return response



# new = VkExcel(auth_from=None, auth_to=None)
# new.get_leads_from_vk()
# new.append_into_excel()