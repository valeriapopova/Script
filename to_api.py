
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
    url = f'http://{host}:5001/bitrix/new_product'
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
    """ Редактирует подборку с товарами.""""
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


# def append_values_into_sheets(res, auth_dict, host='localhost'):
#     """ Добавляет только значения в google sheets"""
#     res.update(auth_dict)
#     url_for_sheets = f'http://{host}:5001/sheets/append_values'
#     response = requests.post(url_for_sheets, json=res)
#     return response
#
#
# def append_into_sheets(res, auth_dict, host='localhost'):
#     """ Добавляет данные в таблицу google sheets """
#     res.update(auth_dict)
#     url_for_sheets = f'http://{host}:5001/sheets/append'
#     response = requests.post(url_for_sheets, json=res)
#     return response
#
#
# def clear_append_into_sheets(res, auth_dict, host='localhost'):
#     """ Перезаписывает данные в таблицу google sheets   """
#     res.update(auth_dict)
#     url_for_sheets = f'http://{host}:5001/sheets/clear_append'
#     response = requests.post(url_for_sheets, json=res)
#     return response
#
#
# def append_new_list(res, auth_dict, host='localhost'):
#     """ Добавляет данные в новый лист google sheets  """
#     res.update(auth_dict)
#     url_for_sheets = f'http://{host}:5001/sheets/append_list'
#     response = requests.post(url_for_sheets, json=res)
#     return response
#
# def append_into_excel(res, host='localhost'):
#     """ Добавляет данные в excel """
#     url_for_excel = f'http://{host}:5001/excel'
#     response = requests.post(url_for_excel, json=res)
#     return response
#
#
# def post_to_tg(res, chat_id, host='localhost'):
#     """ Отправляет новые лиды в телеграм чат
#     (принимает на вход chat_id, узнать его можно у бота @LeadsFromVk написав /start)
#     """
#     chat_id_data = {'chat_id': chat_id}
#     res.update(chat_id_data)
#     print(res)
#     url_for_tg = f'http://{host}:5001/telegram'
#     response = requests.post(url_for_tg, json=res)
#     return response
#
#
# def post_email(res, email, host='localhost'):
#     """ Отправляет новые лиды на указанную почту"""
#     data = {'to': email}
#     res.update(data)
#     url = f'http://{host}:5001/email/post'
#     response = requests.post(url, json=res)
#     return response
#
#
# def post_to_bitrix(res, url, host='localhost'):
#     """ Отправляет новые лиды на в Birix24 по url """
#     data = {'url': url}
#     res.update(data)
#     url = f'http://{host}:5001/bitrix/post'
#     response = requests.post(url, json=res)
#     return response