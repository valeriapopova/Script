import json
import os
from pprint import pprint

import psycopg2
from db import *
from config import *
import requests
from from_api import get_leads_from_vk
from to_api import *


def get_account_fromto(account_id):
    """ Получаем связки пользователя """
    try:
        select_ = f"""SELECT fromto_id FROM account
        WHERE account.id={account_id};"""
        result = execute_read_query(connection_psql(), select_)
        return result
    except ConnectionError as e:
        print(f"The error '{e}' occurred")


# connective = get_account_fromto(1)
# print(connective)

def vkleads_excel():
    """ Связка vk - excel """
    data = get_leads_from_vk()
    append_into_excel(data)


def vkleads_tg(account_id):
    """ Связка vk - telegram bot """
    select_ = f""" SELECT tg_chat_id FROM account
        WHERE account.id={account_id}; """
    result = execute_read_query(connection_psql(), select_)
    for pair in result:
        for res in pair:
            chat_id = res
    data = get_leads_from_vk()
    post_to_tg(data, chat_id)


def vkleads_email(account_id):
    """ Связка vk - email рассылка """
    select_ = f""" SELECT email FROM account
           WHERE account.id={account_id}; """
    result = execute_read_query(connection_psql(), select_)
    for pair in result:
        for res in pair:
            email = res
    data = get_leads_from_vk()
    post_email(data, email)


def vkleads_bitrix(account_id):
    """ Связка vk - bitrix лиды """
    select_ = f""" SELECT bitrix_url FROM account
               WHERE account.id={account_id}; """
    result = execute_read_query(connection_psql(), select_)
    for pair in result:
        for res in pair:
            url = res
    data = get_leads_from_vk()
    post_to_bitrix(data, url)


def vkleads_sheets_newlist(account_id):
    """ Связка vk - google sheets(добавление на новый лист) """
    select_ = f""" SELECT spreadsheetid, auth FROM account
               WHERE account.id={account_id}; """
    result = execute_read_query(connection_psql(), select_)
    auth = json.dumps(result)
    data = get_leads_from_vk()
    append_new_list(data, auth)


def vkleads_sheets_appendvalues(account_id):
    """ Связка vk - google sheets (добавление только значений) """
    select_ = f""" SELECT spreadsheetid, auth FROM account
               WHERE account.id={account_id}; """
    result = execute_read_query(connection_psql(), select_)
    auth = json.dumps(result)
    data = get_leads_from_vk()
    append_values_into_sheets(data, auth)


def vkleads_sheets_append(account_id):
    """ Связка vk - google sheets  """
    select_ = f""" SELECT spreadsheetid, auth FROM account
               WHERE account.id={account_id}; """
    result = execute_read_query(connection_psql(), select_)
    auth = json.dumps(result)
    data = get_leads_from_vk()
    append_into_sheets(data, auth)


def vkleads_sheets_clearappend(account_id):
    """ Связка vk - google sheets (перезапись) """
    select_ = f""" SELECT spreadsheetid, auth FROM account
               WHERE account.id={account_id}; """
    result = execute_read_query(connection_psql(), select_)
    auth = json.dumps(result)
    data = get_leads_from_vk()
    clear_append_into_sheets(data, auth)



vkleads_tg(1)