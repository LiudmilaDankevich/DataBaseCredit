import mysql.connector as mysql

db = mysql.connect(host="localhost",

                   user="root",

                   password="",

                   database='job')
cursor = db.cursor()
# cursor.execute("CREATE DATABASE job")
# print(cursor.fetchall())
# query = "CREATE TABLE users_job " \
#     "(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
#     "name VARCHAR(255), " \
#     "user_name VARCHAR(255), " \
#     "address VARCHAR(255))"
# cursor.execute(query)
# print(cursor.fetchall())
# query = "INSERT INTO users_job (name, user_name, address) VALUES (%s, %s, %s)"
# values = [
#     ("Peter", "Ben", "Minsk"),
#     ("Ami", "Linas", "Brest"),
#     ("Michel", "Onla", "New York"),
#     ("Milla", "Dan", "Mayami")
# ]
# cursor.executemany(query, values)
# db.commit()
# print(cursor.fetchall())
cursor.execute("DESC users_job")
print(cursor.fetchall())
cursor.execute("Select * FROM users_job WHERE id=3")
print(cursor.fetchall())
cursor.execute("Select * FROM users_job ORDER BY id DESC")
print(cursor.fetchall())
cursor.execute("Select * FROM users_job WHERE id=4")
print(cursor.fetchall())
# cursor.execute("SHOW TABLES")
# print(cursor.fetchall())
# cursor.execute("status")
# print(cursor.fetchall())