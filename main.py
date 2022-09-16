
import json
import os
import threading
import time
from pprint import pprint

import now as now
import psycopg2

from connective.leads_vk_bitrix import VkBitrix
from connective.leads_vk_email import VkEmail
from connective.leads_vk_excel import VkExcel
from connective.leads_vk_sheets import VkSheets
from connective.leads_vk_tg import VkTelegram
from db import *


def get_fromto():
    """ Получаем связки пользователей """
    try:
        select_ = "SELECT * FROM account_connective"
        result = execute_read_query(connection_psql(), select_)
        for res in result:
            res = list(res)
            fromto_id = res[1]
            auth_to = res[2]
            auth_from = res[3]
            if fromto_id == 1:
                new = VkExcel(auth_from, auth_to)
                new.get_leads_from_vk()
                new.append_into_excel()
            elif fromto_id == 2:
                new = VkSheets(auth_from, auth_to)
                new.get_leads_from_vk()
                new.append_values_into_sheets()
            elif fromto_id == 3:
                new = VkSheets(auth_from, auth_to)
                new.get_leads_from_vk()
                new.append_into_sheets()
            elif fromto_id == 4:
                new = VkSheets(auth_from, auth_to)
                new.get_leads_from_vk()
                new.clear_append_into_sheets()
            elif fromto_id == 5:
                new = VkSheets(auth_from, auth_to)
                new.get_leads_from_vk()
                new.append_new_list()
            elif fromto_id == 6:
                new = VkTelegram(auth_from, auth_to)
                new.get_leads_from_vk()
                new.post_to_tg()
            elif fromto_id == 7:
                new = VkEmail(auth_from, auth_to)
                new.get_leads_from_vk()
                new.post_email()
            elif fromto_id == 8:
                new = VkBitrix(auth_from, auth_to)
                new.get_leads_from_vk()
                new.post_to_bitrix()

    except ConnectionError as e:
        print(f"The error '{e}' occurred")


if __name__ == "__main__":
    start = time.time()
    threading.Thread(target=get_fromto).start()
    # get_fromto()
    end = (time.time() - start)
    print(end)













# def get_account_fromto(account_id):
#     """ Получаем связки пользователя """
#     try:
#         select_ = f"""SELECT fromto_id FROM account_connective
#         WHERE account_connective.id={account_id};"""
#         result = execute_read_query(connection_psql(), select_)
#         return result
#     except ConnectionError as e:
#         print(f"The error '{e}' occurred")


# connective = get_account_fromto(1)
# print(connective)