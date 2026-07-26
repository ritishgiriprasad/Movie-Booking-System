import pymysql
from config import HOST, USER, PASSWORD, DATABASE


def get_connection():
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        cursorclass=pymysql.cursors.DictCursor
    )