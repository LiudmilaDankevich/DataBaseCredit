import mysql.connector as mysql
#from framework.db.common_db_steps import BaseDBSteps 84.201.152.11
from sqlalchemy import text
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#подключение не получилось
engine = create_engine("postgresql+psycopg2://netology:NetoSQL2019@localhost84.201.152.11/sqlfree-1")
engine.connect()
print(engine)

# connection = psycopg2.connect(user="postgres", password="1111")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# #
# cursor = connection.cursor()
# sql_create_database = cursor.execute('create database sqlalchemy_tuts')

# cursor.close()
# connection.close()