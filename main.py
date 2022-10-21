
import json
import os
import threading
import time
from pprint import pprint

import now as now
import psycopg2

from connective.bitrix_excel import BitrixExcel
from connective.bitrix_sheets import BitrixSheets
from connective.vk_bitrix import VkBitrix
from connective.vk_email import VkEmail
from connective.vk_excel import VkExcel
from connective.vk_sheets import VkSheets
from connective.vk_tg import VkTelegram
from connective.bitrix_tg import BitrixTelegram
from connective.bitrix_email import BitrixEmail
from connective.jivo_sheets import JivoSheets
from connective.jivo_excel import JivoExcel
from db import *


def get_fromto():
    """ Получаем связки пользователей """
    try:
        select_ = "SELECT * FROM account_api_data"
        result = execute_read_query(connection_psql(), select_)
        for res in result:
            res = list(res)
            model_id = res[2]
            auth_to = res[4]
            auth_from = res[3]

            if model_id == 1:
                new = VkSheets(auth_from, auth_to)
                new.get_leads_from_vk()
                new.append_values_into_sheets()

            elif model_id == 2:
                new = VkSheets(auth_from, auth_to)
                new.get_leads_from_vk()
                new.append_into_sheets()

            elif model_id == 3:
                new = VkSheets(auth_from, auth_to)
                new.get_leads_from_vk()
                new.append_new_list()

            elif model_id == 4:
                new = VkSheets(auth_from, auth_to)
                new.get_leads_from_vk()
                new.clear_append_into_sheets()

            elif model_id == 5:
                new = VkBitrix(auth_from, auth_to)
                new.get_leads_from_vk()
                new.post_leads_to_bitrix()

            elif model_id == 6:
                new = VkBitrix(auth_from, auth_to)
                new.get_leads_from_vk()
                new.post_new_contact_to_bitrix()

            elif model_id == 7:
                new = VkExcel(auth_from, auth_to)
                new.get_leads_from_vk()
                new.append_into_excel()

            elif model_id == 8.26:
                new = VkBitrix(auth_from, auth_to)
                new.webhook_vk()
                new.new_feed_mess_to_bitrix()

            elif model_id == 9:
                new = BitrixSheets(auth_from, auth_to)
                new.get_leads_bitrix()
                new.append_values_into_sheets_b()

            elif model_id == 10:
                new = BitrixSheets(auth_from, auth_to)
                new.get_leads_bitrix()
                new.append_into_sheets_b()

            elif model_id == 11:
                new = BitrixSheets(auth_from, auth_to)
                new.get_leads_bitrix()
                new.append_new_list_b()

            elif model_id == 12:
                new = BitrixSheets(auth_from, auth_to)
                new.get_leads_bitrix()
                new.clear_append_into_sheets_b()

            elif model_id == 13:
                new = BitrixExcel(auth_from, auth_to)
                new.get_leads_bitrix()
                new.append_into_excel()

            elif model_id == 14.48:
                new = BitrixTelegram(auth_from, auth_to)
                new.webhook_bitrix()
                new.post_to_tg()

            elif model_id == 15.46:
                new = BitrixEmail(auth_from, auth_to)
                new.webhook_bitrix()
                new.post_email()

            elif model_id == 16:
                new = VkSheets(auth_from, auth_to)
                new.get_statistic_current_day()
                new.append_values_into_sheets()

            elif model_id == 17:
                new = VkSheets(auth_from, auth_to)
                new.get_statistic_current_day()
                new.append_into_sheets()

            elif model_id == 18:
                new = VkSheets(auth_from, auth_to)
                new.get_statistic_current_day()
                new.append_new_list()

            elif model_id == 19:
                new = VkSheets(auth_from, auth_to)
                new.get_statistic_current_day()
                new.clear_append_into_sheets()

            elif model_id == 20:
                new = VkExcel(auth_from, auth_to)
                new.get_statistic_current_day()
                new.append_into_excel()

            elif model_id == 21:
                new = VkSheets(auth_from, auth_to)
                new.get_statistic_yesterday()
                new.append_values_into_sheets()

            elif model_id == 22:
                new = VkSheets(auth_from, auth_to)
                new.get_flood_stats()
                new.append_into_sheets()

            elif model_id == 23:
                new = VkSheets(auth_from, auth_to)
                new.get_flood_stats()
                new.append_new_list()

            elif model_id == 24:
                new = VkSheets(auth_from, auth_to)
                new.get_flood_stats()
                new.clear_append_into_sheets()

            elif model_id == 25:
                new = VkExcel(auth_from, auth_to)
                new.get_statistic_yesterday()
                new.append_into_excel()

            elif model_id == 26:
                new = VkBitrix(auth_from, auth_to)
                new.webhook_vk()
                new.new_feed_mess_to_bitrix()

            elif model_id == 27:
                new = VkBitrix(auth_from, auth_to)
                new.webhook_vk()
                new.new_deal_to_bitrix()

            elif model_id == 28:
                new = VkSheets(auth_from, auth_to)
                new.webhook_vk()
                new.append_values_into_sheets()

            elif model_id == 29:
                new = VkSheets(auth_from, auth_to)
                new.webhook_vk()
                new.append_into_sheets()

            elif model_id == 30:
                new = VkSheets(auth_from, auth_to)
                new.webhook_vk()
                new.append_new_list()

            elif model_id == 31:
                new = VkSheets(auth_from, auth_to)
                new.webhook_vk()
                new.clear_append_into_sheets()

            elif model_id == 32:
                new = VkTelegram(auth_from, auth_to)
                new.webhook_vk()
                new.post_to_tg()

            elif model_id == 33:
                new = VkEmail(auth_from, auth_to)
                new.webhook_vk()
                new.post_email()

            elif model_id == 34:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_call_event()
                new.append_values_into_sheets()

            elif model_id == 35:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_accepted()
                new.append_values_into_sheets()

            elif model_id == 36:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_assigned()
                new.append_values_into_sheets()

            elif model_id == 37:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_finished()
                new.append_values_into_sheets()

            elif model_id == 38:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_updated()
                new.append_values_into_sheets()

            elif model_id == 39:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_offline()
                new.append_values_into_sheets()

            elif model_id == 40:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_call_event()
                new.append_into_sheets()

            elif model_id == 41:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_accepted()
                new.append_into_sheets()

            elif model_id == 42:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_assigned()
                new.append_into_sheets()

            elif model_id == 43:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_finished()
                new.append_into_sheets()

            elif model_id == 44:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_updated()
                new.append_into_sheets()

            elif model_id == 45:
                new = JivoSheets(auth_from, auth_to)
                new.webhook_offline()
                new.append_into_sheets()

            elif model_id == 46:
                new = BitrixEmail(auth_from, auth_to)
                new.webhook_bitrix()
                new.post_email()

            elif model_id == 47:
                new = BitrixTelegram(auth_from, auth_to)
                new.webhook_bitrix()
                new.post_to_tg()

            elif model_id == 48:
                new = VkBitrix(auth_from, auth_to)
                new.webhook_vk()
                new.post_message_bitrix()

            elif model_id == 49:
                new = VkSheets(auth_from, auth_to)
                new.get_month_statistic()
                new.append_values_into_sheets()

            elif model_id == 50:
                new = VkSheets(auth_from, auth_to)
                new.get_month_statistic()
                new.append_into_sheets()

            elif model_id == 51:
                new = VkSheets(auth_from, auth_to)
                new.get_month_statistic()
                new.append_new_list()

            elif model_id == 52:
                new = VkSheets(auth_from, auth_to)
                new.get_month_statistic()
                new.clear_append_into_sheets()

            elif model_id == 53:
                new = VkExcel(auth_from, auth_to)
                new.get_month_statistic()
                new.append_into_excel()

            elif model_id == 54:
                new = VkSheets(auth_from, auth_to)
                new.webhook_vk()
                new.update_row()

            elif model_id == 55:
                new = VkSheets(auth_from, auth_to)
                new.get_budget()
                new.update_row()

            elif model_id == 56:
                new = VkSheets(auth_from, auth_to)
                new.get_statistic_current_day()
                new.update_row()

            elif model_id == 57:
                new = VkSheets(auth_from, auth_to)
                new.get_statistic_yesterday()
                new.update_row()

            elif model_id == 58:
                new = VkSheets(auth_from, auth_to)
                new.get_budget()
                new.append_values_into_sheets()

            elif model_id == 59:
                new = VkSheets(auth_from, auth_to)
                new.get_budget()
                new.append_into_sheets()

            elif model_id == 60:
                new = VkSheets(auth_from, auth_to)
                new.get_budget()
                new.append_new_list()

            elif model_id == 61:
                new = VkSheets(auth_from, auth_to)
                new.get_budget()
                new.clear_append_into_sheets()

            elif model_id == 62:
                new = VkExcel(auth_from, auth_to)
                new.get_budget()
                new.append_into_excel()

            elif model_id == 63:
                new = BitrixSheets(auth_from, auth_to)
                new.get_contacts_list_bitrix()
                new.append_values_into_sheets_b()

            elif model_id == 64:
                new = BitrixSheets(auth_from, auth_to)
                new.get_contacts_list_bitrix()
                new.append_into_sheets_b()

            elif model_id == 65:
                new = BitrixSheets(auth_from, auth_to)
                new.get_contacts_list_bitrix()
                new.append_new_list_b()

            elif model_id == 66:
                new = BitrixSheets(auth_from, auth_to)
                new.get_contacts_list_bitrix()
                new.clear_append_into_sheets_b()

            elif model_id == 67:
                new = BitrixExcel(auth_from, auth_to)
                new.get_contacts_list_bitrix()
                new.append_into_excel()

            elif model_id == 68:
                new = BitrixEmail(auth_from, auth_to)
                new.get_contacts_list_bitrix()
                new.post_email()

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


