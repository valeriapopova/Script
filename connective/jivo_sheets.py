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