import sqlite3
# from random import randrange

connection = sqlite3.connect('databaze.db')  # setup DataBase
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# выше указанное - это настройка БД (setup), ниже  - это работа с базой данных
#  Добавление записи в БД:
# cursor.execute(" INSERT INTO Users (username, email, age) VALUES (?, ?, ?)",
#                ("new_user", "ex@gmail.com", "28")
#                )
# for i in range(30): # этот код генерирует пользователей со случайным возрастом:
#     cursor.execute(" INSERT INTO Users (username, email, age) VALUES (?, ?, ?)",
#                    (f"new_user{i}", f"{i}ex@gmail.com", str(randrange(28, 60)))
#                    )
#  Редактирование записи в БД:
# cursor.execute("UPDATE Users SET age = ? WHERE username = ?",
#                (29, "new_user")
#                )
#  Удаление записи в БД:
# cursor.execute("DELETE FROM Users WHERE username=?",
#                ("new_user",)
#                )
# Чтение элементов с БД:
# cursor.execute("SELECT * FROM Users")  # читает всю базу
# SELECT - позволяет получать данные username из (FROM) Users с условием (WHERE) age > ?
# cursor.execute("SELECT username, age FROM Users WHERE age > ?", (50,))
# выбрать (SELECT) age среднее по возрасту из Users сортировать? (GROUP BY) по AGE
# cursor.execute("SELECT age, AVG(age) FROM Users GROUP BY AGE")
# cursor.execute("SELECT username, age, AVG(age) FROM Users GROUP BY AGE")
# cursor.execute("SELECT username, age, AVG(age) FROM Users ORDER BY AGE")
cursor.execute("SELECT username, age FROM Users ORDER BY AGE")   # ORDER BY - аналогично GROUP BY

users = cursor.fetchall()  # записываем базу или результат вышеуказанной операции в переменную
for user in users:  # выводим в консоль
    print(user)

# Подсчитать общее количество записей:
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(f'Общее количество пользователей в базе:{total_users}')



connection.commit()
connection.close()
