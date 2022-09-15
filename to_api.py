
import requests


def append_values_into_sheets(res, auth_dict, host='localhost'):
    """ Добавляет только значения в google sheets"""
    res.update(auth_dict)
    url_for_sheets = f'http://{host}:5001/sheets/append_values'
    response = requests.post(url_for_sheets, json=res)
    return response


def append_into_sheets(res, auth_dict, host='localhost'):
    """ Добавляет данные в таблицу google sheets """
    res.update(auth_dict)
    url_for_sheets = f'http://{host}:5001/sheets/append'
    response = requests.post(url_for_sheets, json=res)
    return response


def clear_append_into_sheets(res, auth_dict, host='localhost'):
    """ Перезаписывает данные в таблицу google sheets   """
    res.update(auth_dict)
    url_for_sheets = f'http://{host}:5001/sheets/clear_append'
    response = requests.post(url_for_sheets, json=res)
    return response


def append_new_list(res, auth_dict, host='localhost'):
    """ Добавляет данные в новый лист google sheets  """
    res.update(auth_dict)
    url_for_sheets = f'http://{host}:5001/sheets/append_list'
    response = requests.post(url_for_sheets, json=res)
    return response

def append_into_excel(res, host='localhost'):
    """ Добавляет данные в excel """
    url_for_excel = f'http://{host}:5001/excel'
    response = requests.post(url_for_excel, json=res)
    return response


def post_to_tg(res, chat_id, host='localhost'):
    """ Отправляет новые лиды в телеграм чат
    (принимает на вход chat_id, узнать его можно у бота @LeadsFromVk написав /start)
    """
    chat_id_data = {'chat_id': chat_id}
    res.update(chat_id_data)
    print(res)
    url_for_tg = f'http://{host}:5001/telegram'
    response = requests.post(url_for_tg, json=res)
    return response


def post_email(res, email, host='localhost'):
    """ Отправляет новые лиды на указанную почту"""
    data = {'to': email}
    res.update(data)
    url = f'http://{host}:5001/email/post'
    response = requests.post(url, json=res)
    return response


def post_to_bitrix(res, url, host='localhost'):
    """ Отправляет новые лиды на в Birix24 по url """
    data = {'url': url}
    res.update(data)
    url = f'http://{host}:5001/bitrix/post'
    response = requests.post(url, json=res)
    return response