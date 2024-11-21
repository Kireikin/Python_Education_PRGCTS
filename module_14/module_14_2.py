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


def read_baze(*arg):  # читает всю базу каждый раз когда и как нам нужно
    cursor.execute(*arg)
    users = cursor.fetchall()  # записываем базу или результат вышеуказанной операции в переменную
    for user in users:  # выводим в консоль
        print(user)
    print()


# Код с задания модуля 14_1:
#  Добавление записи в БД:
for i in range(10):  # этот код генерирует пользователей согласно заданию выполняем 1 раз:
    cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i + 1}", f"example{i + 1}@gmail.com", (i + 1) * 10, 1000)
                   )

# Обновите balance у каждой 2ой записи начиная с 1ой на 500
id = 1
while id <= int(10):
    cursor.execute("UPDATE Users SET balance = ? WHERE id =? ",
                   (500, id)
                   )
    id += 2


# Удалите каждую 3ую запись в таблице начиная с 1ой:
id = 1
while id <= int(10):
    cursor.execute(" DELETE FROM Users WHERE id =? ",
                   (id,))
    id += 3

# Начало выполнения задания модуля 14_2
# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.
read_baze("SELECT * FROM Users")  # показываем записи
# Удалите 6-ую запись в таблице:
cursor.execute(" DELETE FROM Users WHERE id =? ", (6,))
print('Удаление записи №6')
read_baze("SELECT * FROM Users")  # показываем что удаление произошло

# Подсчитать общее количество записей:
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(f'Общее количество пользователей в базе:{total_users}')

# Посчитать сумму всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(f'Сумма на балансе пользователей в базе:{all_balances}')

# Вывести в консоль средний баланс всех пользователей
print(all_balances / total_users)

cursor.execute("DELETE FROM Users")  # чистим базу ;) из-за лени коментить каждый раз код
print("Записи удалены, база не должна содержать данные")
read_baze("SELECT * FROM Users")

connection.commit()
connection.close()
