import requests


class VkExcel:

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

    def append_into_excel(self, host='localhost'):
        """ Добавляет данные в excel """
        url_for_excel = f'http://{host}:63880/excel'
        response = requests.post(url_for_excel, json=self.data)
        return response



# new = VkExcel(auth_from=None, auth_to=None)
# new.get_leads_from_vk()
# new.append_into_excel()