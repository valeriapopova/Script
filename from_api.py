import json

from config import *
import requests
#
#
# def get_search_data_from_vk(token, age_from, age_to, sex, city , count, host='localhost'):
#     """ Забирает данные из vk по критериям поиска """
#     url_for_vk = f'http://{host}:5000/vk/search_users'
#     data_for_vk = {'token': token, 'age_from': age_from, 'age_to': age_to, 'sex': sex, 'city': city, 'count': count}
#     r = requests.post(url_for_vk, data=data_for_vk)
#     res = r.json()
#     return res


# def get_leads_from_vk(host='localhost'):
#     """ Забирает новые лиды из vk """
#     vk_url = f'http://{host}:5000/vk/get_leads'
#     r = requests.post(vk_url)
#     res = r.json()
#     return res
#
# def get_leads_bitrix(self, host='localhost'):
#     """ Забирает новые лиды из Birix24  """
#     url = f'http://{host}:5001/bitrix/get_leads'
#     r = requests.post(url, json=json.loads(auth_from))
#     res = r.json()
#     return res


def get_all_rows_from_google_sheets(self, host='localhost'):
    """Получить все строки из таблицы google sheets"""
    url = f'http://{host}:5000/google_sheets/get_all_rows'
    r = requests.post(url, json=json.loads(self.auth_from))
    res = r.json()
    return res


def google_sheets_search_row(self, host='localhost'):
    """Найти строку в таблице google sheets"""
    url = f'http://{host}:5000/google_sheets/search_row'
    r = requests.post(url, json=json.loads(self.auth_from))
    res = r.json()
    return res


def google_sheets_search_rows(self, host='localhost'):
    """Найти несколько строк в таблице google sheets"""
    url = f'http://{host}:5000/google_sheets/search_rows'
    r = requests.post(url, json=json.loads(self.auth_from))
    res = r.json()
    return res




#VkAds Этот метод можно вызвать с ключом доступа пользователя.
#Требуются права доступа: ads.


def get_demographics(host='localhost'):
    """Возвращает демографическую статистику по рекламным объявлениям или кампаниям."""
    url = f'http://{host}:5000/vk/ads_get_demographics'
    r = requests.post(url, json=json.loads(auth_from))
    res = r.json()
    return res


def get_targeting(host='localhost'):
    """Возвращает параметры таргетинга рекламных объявлений"""
    url = f'http://{host}:5000/vk/ads_get_targeting'
    r = requests.post(url, json=json.loads(auth_from))
    res = r.json()
    return res


def get_targeting_stats(host='localhost'):
    """Возвращает размер целевой аудитории таргетинга, а также рекомендованные
       значения CPC и CPM."""
    url = f'http://{host}:5000/vk/ads_get_targeting_stats'
    r = requests.post(url, json=json.loads(auth_from))
    res = r.json()
    return res


def get_posts_reach(host='localhost'):
    """Возвращает подробную статистику по охвату рекламных записей из объявлений и кампаний для
        продвижения записей сообщества."""
    url = f'http://{host}:5000/vk/ads_get_posts_reach'
    r = requests.post(url, json=json.loads(auth_from))
    res = r.json()
    return res


def get_flood_stats(host='localhost'):
    """Возвращает подробную статистику по охвату рекламных записей из объявлений и кампаний для
        продвижения записей сообщества."""
    url = f'http://{host}:5000/vk/ads_get_flood_stats'
    r = requests.post(url, json=json.loads(auth_from))
    res = r.json()
    return res

#vk_market

def market_get_product_by_id(self, host='localhost'):
    """ Возвращает информацию о товарах по идентификаторам. """
    vk_url = f'http://{host}:5000/vk/market_get_product_by_id'
    r = requests.post(vk_url, json=self.auth_from)
    self.data = r.json()
    return self.data


def market_get_order_by_id(self, host='localhost'):
    """ Возвращает заказ по идентификатору."""
    vk_url = f'http://{host}:5000/vk/market_get_order_by_id'
    r = requests.post(vk_url, json=self.auth_from)
    self.data = r.json()
    return self.data


#JivoChat

def webhook_call_event(host='lk.ecomru.ru'):
    """Событие отправляется когда операторы получают новый звонок или изменяется статус текущего звонка."""
    wh_url = f'http://{host}:53462/jivo/call_event'
    r = requests.post(wh_url, json=json.loads(auth_from))
    data = r.json()
    return data


def webhook_accepted(host='lk.ecomru.ru'):
    """Событие возникает в момент приема запроса диалога оператором."""
    wh_url = f'http://{host}:53462/jivo/сhat_accepted'
    r = requests.post(wh_url, json=json.loads(auth_from))
    data = r.json()
    return data


def webhook_assigned(host='lk.ecomru.ru'):
    """Событие отправляется когда чат прикрепляется к карточке в CRM, используя параметр
        "crm_link" из ответа на событие chat_accepted. """
    wh_url = f'http://{host}:53462/jivo/chat_assigned'
    r = requests.post(wh_url, json=json.loads(auth_from))
    data = r.json()
    return data


def webhook_finished(host='lk.ecomru.ru'):
    """Событие отправляется при закрытии чата в приложении оператора."""
    wh_url = f'http://{host}:53462/jivo/chat_finished'
    r = requests.post(wh_url, json=json.loads(auth_from))
    data = r.json()
    return data


def webhook_updated(host='lk.ecomru.ru'):
    """Событие будет отправлено в случае, если информация о посетителе была обновлена . """
    wh_url = f'http://{host}:53462/jivo/chat_updated'
    r = requests.post(wh_url, json=json.loads(auth_from))
    data = r.json()
    return data


def webhook_offline(host='lk.ecomru.ru'):
    """Событие будет отправлено в момент отправки сообщения через оффлайн-форму. """
    wh_url = f'http://{host}:53462/jivo/offline_message'
    r = requests.post(wh_url, json=json.loads(auth_from))
    data = r.json()
    return data


#bitrix
def search_user_by_id(self, host='localhost'):
    """ Поиск сотрудника по id """
    url = f'http://{host}:5001/bitrix/search_user_id'
    r = requests.post(url, json=json.loads(self.auth_from))
    self.data = r.json()
    return self.data


def search_user_by_email(self, host='localhost'):
    """ Поиск сотрудника по email """
    url = f'http://{host}:5001/bitrix/search_user_email'
    r = requests.post(url, json=json.loads(self.auth_from))
    self.data = r.json()
    return self.data

def search_contact_by_id(self, host='localhost'):
    """Возвращает контакт по идентификатору."""
    url = f'http://{host}:5001/bitrix/search_contact_id'
    r = requests.post(url, json=json.loads(self.auth_from))
    self.data = r.json()
    return self.data


def search_deal_by_id(self, host='localhost'):
    """Возвращает сделку по идентификатору."""
    url = f'http://{host}:5001/bitrix/search_deal_id'
    r = requests.post(url, json=json.loads(self.auth_from))
    self.data = r.json()
    return self.data


def search_invoice_by_id(self, host='localhost'):
    """Возвращает счет по идентификатору."""
    url = f'http://{host}:5001/bitrix/search_invoice_id'
    r = requests.post(url, json=json.loads(self.auth_from))
    self.data = r.json()
    return self.data


def search_product_by_id(self, host='localhost'):
    """Возвращает счет по идентификатору."""
    url = f'http://{host}:5001/bitrix/search_product_id'
    r = requests.post(url, json=json.loads(self.auth_from))
    self.data = r.json()
    return self.data


def search_company_by_id(self, host='localhost'):
    """Возвращает компанию по идентификатору."""
    url = f'http://{host}:5001/bitrix/search_company_id'
    r = requests.post(url, json=json.loads(self.auth_from))
    self.data = r.json()
    return self.data

def tel_reqister(self, host='localhost'):
    """Метод регистрирует звонок в Битрикс24, для чего ищет в CRM соответствующий номеру объект"""
    self.data.update(json.loads(self.auth_from))
    url = f'http://{host}:5001/bitrix/tel_reqister'
    response = requests.post(url, json=self.data)
    return response


def tel_finish(self, host='localhost'):
    """Метод завершает звонок, фиксирует его в статистике, скрывает у пользователя карточку звонка."""
    self.data.update(json.loads(self.auth_from))
    url = f'http://{host}:5001/bitrix/tel_finish'
    response = requests.post(url, json=self.data)
    return response


