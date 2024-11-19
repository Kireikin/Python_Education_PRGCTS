import sqlite3

connection = sqlite3.connect('not_telegram.db')  # setup DataBase
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")


# выше указанное - это настройка БД (setup), ниже  - это работа с базой данных


def read_baze():  # читает всю базу каждый раз когда нам нужно
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()  # записываем базу или результат вышеуказанной операции в переменную
    for user in users:  # выводим в консоль
        print(user)


#  Добавление записи в БД:
for i in range(10):  # этот код генерирует пользователей согласно заданию выполняем 1 раз:
    cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i + 1}", f"example{i + 1}@gmail.com", (i + 1) * 10, 1000)
                   )
print("Сгенерированные записи в БД:")
read_baze()  # смотрим
# Обновите balance у каждой 2ой записи начиная с 1ой на 500
id = 1
while id <= int(10):
    cursor.execute("UPDATE Users SET balance = ? WHERE id =? ",
                   (500, id)
                   )
    id += 2
print("Обновленный balance у каждой 2ой записи начиная с 1ой на 500 в БД:")
read_baze()  # смотрим

# Удалите каждую 3ую запись в таблице начиная с 1ой:
id = 1
while id <= int(10):
    cursor.execute(" DELETE FROM Users WHERE id =? ",
                   (id,))
    id += 3

print("Удалили каждую 3ую запись в таблице начиная с 1ой:")
read_baze()  # смотрим

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
print("возраст не равен 60:")
users = cursor.fetchall()  # записываем базу или результат вышеуказанной операции в переменную
for user in users:  # выводим в консоль
    print(f"Имя:{user[0]}| Почта:{user[1]}| Возраст: {user[2]}| Баланс: {user[3]} ")


# cursor.execute("DELETE FROM Users")  # чистим базу ;) из-за лени коментить каждый раз код
# print("Записи удалены, база не должна содержать данные")
# read_baze()

connection.commit()
connection.close()
