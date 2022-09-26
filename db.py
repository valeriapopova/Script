
import psycopg2

from config import *

from psycopg2 import OperationalError


def connection_psql():
    connection_ = psycopg2.connect(
           dbname='integration_db',
           user=DB_USER,
           password=DB_PASSWORD,
           target_session_attrs='read-write',
           sslmode='verify-full'
           )
    return connection_


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


# account_id = 1
# select_ = f""" SELECT tg_chat_id FROM account
#         WHERE account.id={account_id}; """
# p = execute_read_query(connection_psql(), select_)
# for pair in p:
#     for t in pair:
#         print(t)