import mysql.connector as mysql

db = mysql.connect(host="localhost",

                   user="root",

                   password="",

                   database='credit')
cursor = db.cursor()
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.execute("DESC credit_home")
print(cursor.fetchall())
# query = "INSERT INTO credit_home VALUES(%s, %s, %s, %s, %s, %s, %s)"
# values = [
#      (5, "home_new", "belarusbank", 48000, 20, 240, 995)
# ]
# cursor.executemany(query, values)
# db.commit()

# вывести значения всех полей(столбцов) таблицы
cursor.execute("SELECT * FROM credit_home")
print(cursor.fetchall())

   # вывести все значения 1 строки
# cursor.execute("SELECT * FROM credit_home LIMIT 1")
# print(cursor.fetchall())

   # вывести значение поля(столбца) без дублирования
# cursor.execute("SELECT DISTINCT bank FROM credit_home")
# print(cursor.fetchall())

# вывести значение поля(столбца)
# cursor.execute("SELECT bank FROM credit_home")
# print(cursor.fetchall())

 # вывести значение поля под псевдонимом
# cursor.execute("SELECT bank AS bank_new FROM credit_home")
# print(cursor.fetchall())

   # вывести значение поля name таблицы credit_home если поле sum=40000
# cursor.execute("SELECT name FROM credit_home WHERE sum=40000")
# print(cursor.fetchall())
#
# # вывести значение поля name таблицы credit_home если поле sum=40000 и time=60
# cursor.execute("SELECT name FROM credit_home WHERE sum=40000 AND time=60")
# print(cursor.fetchall())

#    # вывести значение поля name таблицы credit_home если поле percent>17
# cursor.execute("SELECT bank FROM credit_home WHERE percent>17")
# print(cursor.fetchall())
#
#    # вывести значение поля name таблицы credit_home если поле sum=40000 или time=60
# cursor.execute("SELECT name FROM credit_home WHERE sum=40000 OR time=60")
# print(cursor.fetchall())

#  # вывести значение всех полей таблицы credit_home если в поле sum последняя цифра 0
# cursor.execute("SELECT * FROM credit_home WHERE sum like '%0'")
# print(cursor.fetchall())
#
# # вывести значение всех полей таблицы credit_home если в поле bank первая буква р,
# а последняя к
# cursor.execute("SELECT * FROM credit_home WHERE bank like 'p%%%%%%%k'")
# print(cursor.fetchall())

# вывести значение всех полей таблицы credit_home если в поле bank последняя
# буква к а перед ней 7 символов
# cursor.execute("SELECT * FROM credit_home WHERE bank like '________k'")
# print(cursor.fetchall())

# &&&&поиск в диапазоне(разобраться)
# cursor.execute("SELECT name FROM credit_home WHERE id BETWEN 2 AND 4")
# print(cursor.fetchall())