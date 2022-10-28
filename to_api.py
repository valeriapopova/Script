import json

import requests

#bitrix

def new_company_to_bitrix(self, host='localhost'):
    """Создает новую компанию"""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5001/bitrix/new_company'
    response = requests.post(url, json=self.data)
    return response


def new_product_to_bitrix(self, host='localhost'):
    """Создает новый товар."""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5001/bitrix/new_product'
    response = requests.post(url, json=self.data)
    return response


def update_product_bitrix(self, host='localhost'):
    """Обновляет товар"""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5001/bitrix/update_product'
    response = requests.post(url, json=self.data)
    return response


def new_element_to_bitrix(self, host='localhost'):
    """Метод создаёт элемент списка."""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5001/bitrix/new_element'
    response = requests.post(url, json=self.data)
    return response


def update_element_bitrix(self, host='localhost'):
    """Обновляет элемент списка'"""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5001/bitrix/update_element'
    response = requests.post(url, json=self.data)
    return response


def update_deal_bitrix(self, host='localhost'):
    """Обновляет сделку"""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5001/bitrix/update_deal'
    response = requests.post(url, json=self.data)
    return response


def tel_hide_bitrix(self, host='localhost'):
    """Метод скрывает карточку звонка у пользователя."""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5001/bitrix/tel_hide'
    response = requests.post(url, json=self.data)
    return response


def tel_attach_record_bitrix(self, host='localhost'):
    """Метод прикрепляет запись к завершенному звонку и к Делу звонка. (Должен вызываться после
    tel_finish, если запись на момент вызова finish еще не готова.) """
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5001/bitrix/tel_attach_record'
    response = requests.post(url, json=self.data)
    return response

#vk_market


def market_edit_order(self, host='localhost'):
    """ Редактирует заказ. """
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5000/vk/market_edit_order'
    response = requests.post(url, json=self.data)
    return response


def market_add(self, host='localhost'):
    """ Добавляет новый товар."""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5000/vk/market_add'
    response = requests.post(url, json=self.data)
    return response


def market_edit(self, host='localhost'):
    """Редактирует товар. """
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5000/vk/market_edit'
    response = requests.post(url, json=self.data)
    return response


def market_create_comment(self, host='localhost'):
    """ Создаёт новый комментарий к товару """
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5000/vk/market_create_comment'
    response = requests.post(url, json=self.data)
    return response


def market_add_album(self, host='localhost'):
    """ Добавляет новую подборку с товарами """
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5000/vk/market_add_album'
    response = requests.post(url, json=self.data)
    return response


def market_edit_album(self, host='localhost'):
    """ Редактирует подборку с товарами."""
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5000/vk/market_edit_album'
    response = requests.post(url, json=self.data)
    return response


def market_add_to_album(self, host='localhost'):
    """ Добавляет товар в одну или несколько выбранных подборок. """
    self.data.update(json.loads(self.auth_to))
    url = f'http://{host}:5000/vk/market_add_to_album'
    response = requests.post(url, json=self.data)
    return response

# sheets

def update_row_sheets(self, host='localhost'):
    """Обновляет/создает строку"""
    self.data.update(json.loads(self.auth_to))
    url_for_sheets = f'http://{host}:5001/google_sheets/update_row'
    response = requests.post(url_for_sheets, json=self.data)
    return response


def update_row_list_sheets(self, host='localhost'):
    """ Обновляет строки(массив)"""
    self.data.update(json.loads(self.auth_to))
    url_for_sheets = f'http://{host}:5001/google_sheets/update_row_list'
    response = requests.post(url_for_sheets, json=self.data)
    return response


def delete_row_sheets(self, host='localhost'):
    """ Удаляет строку """
    self.data.update(json.loads(self.auth_to))
    url_for_sheets = f'http://{host}:5001/google_sheets/delete_row'
    response = requests.post(url_for_sheets, json=self.data)
    return response


#yandex_market

def post_expences(self, host='localhost'):
    """Загрузка расходов на рекламу"""
    self.data.update(json.loads(self.auth_to))
    url_for_sheets = f'http://{host}:52763/yandex/metrica/post_expences'
    response = requests.post(url_for_sheets, json=self.data)
    return response


def create_client(self, host='localhost'):
    """Новая информация о клиентах добавляется(обновляется) к ранее загруженной."""
    self.data.update(json.loads(self.auth_to))
    url_for_sheets = f'http://{host}:52763/yandex/metrica/create_client'
    response = requests.post(url_for_sheets, json=self.data)
    return response


def create_order(self, host='localhost'):
    """Новая информация о заказах добавляется(обновляется) к ранее загруженной."""
    self.data.update(json.loads(self.auth_to))
    url_for_sheets = f'http://{host}:52763/yandex/metrica/create_order'
    response = requests.post(url_for_sheets, json=self.data)
    return response


def post_calls(self, host='localhost'):
    """Загрузка звонков"""
    self.data.update(json.loads(self.auth_to))
    url_for_sheets = f'http://{host}:52763/yandex/metrica/post_calls'
    response = requests.post(url_for_sheets, json=self.data)
    return response


def status_orders(self, host='localhost'):
    """Сопоставление статусов заказов"""
    self.data.update(json.loads(self.auth_to))
    url_for_sheets = f'http://{host}:52763/yandex/metrica/status_orders'
    response = requests.post(url_for_sheets, json=self.data)
    return response