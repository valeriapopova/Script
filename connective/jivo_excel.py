import json

import requests


class JivoExcel:

    def __init__(self, auth_from, auth_to):
        self.auth_from = auth_from
        self.auth_to = auth_to
        self.data = None

    def webhook_call_event(self, host='lk.ecomru.ru'):
        """Событие отправляется когда операторы получают новый звонок или изменяется статус текущего звонка."""
        # wh_url = auth_from['url']
        wh_url = f'http://{host}:53462/jivo/call_event'
        r = requests.post(wh_url, json=json.loads(self.auth_from))
        data = r.json()
        return data

    def webhook_accepted(self, host='lk.ecomru.ru'):
        """Оператор принял запрос диалога от клиента (нажал в программе кнопку Ответить)"""
        #wh_url = auth_from['url']
        wh_url = f'http://{host}:53462/jivo/chat_accepted'
        r = requests.post(wh_url, json=json.loads(self.auth_from))
        data = r.json()
        return data

    def webhook_assigned(self, host='lk.ecomru.ru'):
        """Диалог был прикреплен к карточке в CRM"""
        # wh_url = auth_from['url']
        wh_url = f'http://{host}:53462/jivo/chat_assigned'
        r = requests.post(wh_url, json=json.loads(self.auth_from))
        data = r.json()
        return data

    def webhook_finished(self, host='lk.ecomru.ru'):
        """Диалог завершился (был закрыт в программе либо нажатием на крестик рядом с именем клиента, либо автоматически после того, как клиент покинул сайт)"""
        # wh_url = auth_from['url']
        wh_url = f'http://{host}:53462/jivo/chat_finished'
        r = requests.post(wh_url, json=json.loads(self.auth_from))
        data = r.json()
        return data

    def webhook_updated(self, host='lk.ecomru.ru'):
        """ Обновились контактные данные о клиенте (либо клиент представился, либо оператор сам внёс контакты в программе)"""
        # wh_url = auth_from['url']
        wh_url = f'http://{host}:53462/jivo/chat_updated'
        r = requests.post(wh_url, json=json.loads(self.auth_from))
        data = r.json()
        return data

    def webhook_offline(self, host='lk.ecomru.ru'):
        """Было отправлено оффлайн-сообщение, когда не было операторов онлайн."""
        # wh_url = auth_from['url']
        wh_url = f'http://{host}:53462/jivo/offline_message'
        r = requests.post(wh_url, json=json.loads(self.auth_from))
        data = r.json()
        return data

    def append_into_excel(self, host='api.ecomru.ru'):
        """ Добавляет данные в excel """
        url_for_excel = f'http://{host}:63880/excel/post'
        response = requests.post(url_for_excel, json=self.data)
        return response