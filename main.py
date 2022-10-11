
import json
import os
import threading
import time
from pprint import pprint

import now as now
import psycopg2

from connective.bitrix_excel import BitrixExcel
from connective.bitrix_sheets import BitrixSheets
from connective.leads_vk_bitrix import VkBitrix
from connective.leads_vk_email import VkEmail
from connective.leads_vk_excel import VkExcel
from connective.leads_vk_sheets import VkSheets
from connective.leads_vk_tg import VkTelegram
from db import *


def get_fromto():
    """ Получаем связки пользователей """
    try:
        select_ = "SELECT * FROM account_connective WHERE account_connective.id=9"
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

            elif fromto_id == 9:
                new = BitrixSheets(auth_from, auth_to)
                new.get_leads_bitrix()
                new.append_values_into_sheets_b()

            elif fromto_id == 10:
                new = BitrixSheets(auth_from, auth_to)
                new.get_leads_bitrix()
                new.append_into_sheets_b()

            elif fromto_id == 11:
                new = BitrixSheets(auth_from, auth_to)
                new.get_leads_bitrix()
                new.clear_append_into_sheets_b()

            elif fromto_id == 12:
                new = BitrixSheets(auth_from, auth_to)
                new.get_leads_bitrix()
                new.append_new_list_b()

            elif fromto_id == 13:
                new = BitrixExcel(auth_from, auth_to)
                new.get_leads_bitrix()
                new.append_into_excel()

            elif fromto_id == 14:
                new = VkExcel(auth_from, auth_to)
                new.get_targeting()
                new.append_into_excel()

            elif fromto_id == 15:
                new = VkSheets(auth_from, auth_to)
                new.get_targeting()
                new.append_values_into_sheets()

            elif fromto_id == 16:
                new = VkSheets(auth_from, auth_to)
                new.get_targeting()
                new.append_into_sheets()

            elif fromto_id == 17:
                new = VkSheets(auth_from, auth_to)
                new.get_targeting()
                new.clear_append_into_sheets()

            elif fromto_id == 18:
                new = VkSheets(auth_from, auth_to)
                new.get_targeting()
                new.append_new_list()

            elif fromto_id == 19:
                new = VkExcel(auth_from, auth_to)
                new.get_flood_stats()
                new.append_into_excel()

            elif fromto_id == 20:
                new = VkSheets(auth_from, auth_to)
                new.get_flood_stats()
                new.append_values_into_sheets()

            elif fromto_id == 21:
                new = VkSheets(auth_from, auth_to)
                new.get_flood_stats()
                new.append_into_sheets()

            elif fromto_id == 22:
                new = VkSheets(auth_from, auth_to)
                new.get_flood_stats()
                new.clear_append_into_sheets()

            elif fromto_id == 23:
                new = VkSheets(auth_from, auth_to)
                new.get_flood_stats()
                new.append_new_list()

            elif fromto_id == 24:
                new = VkBitrix(auth_from, auth_to)
                new.get_leads_from_vk()
                new.post_new_contact_to_bitrix()

            elif fromto_id == 25:
                new = VkBitrix(auth_from, auth_to)
                new.get_leads_from_vk()
                new.new_feed_mess_to_bitrix()
            else:
                print('Tакой связки нет')

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
#     try: WHERE account_connective.id=6
#         select_ = f"""SELECT fromto_id FROM account_connective
#         WHERE account_connective.id={account_id};"""
#         result = execute_read_query(connection_psql(), select_)
#         return result
#     except ConnectionError as e:
#         print(f"The error '{e}' occurred")


# connective = get_account_fromto(1)
# print(connective)