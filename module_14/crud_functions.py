import sqlite3


def initiate_db():
    connection1 = sqlite3.connect('databaze.db')  # setup DataBase
    cursor1 = connection1.cursor()
    cursor1.execute('''
    CREATE TABLE IF NOT EXISTS Products(
                                    id          INTEGER PRIMARY KEY,
                                    title       TEXT NOT NULL,
                                    description TEXT,
                                    price       FLOAT
                                        )
                ''')
    # Добавляем в БД вторую таблицу если не создана
    cursor1.execute('''
    CREATE TABLE IF NOT EXISTS Users(
                                    id INTEGER PRIMARY KEY,
                                    username TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    age INTEGER,
                                    balance REAL
                                    )
                    ''')
    cursor1.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
    connection1.commit()
    connection1.close()


def get_all_products():  # возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
    # :return: databaze.db Products - id: INT, title TEXT, description TEXT, price FLOAT
    connection2 = sqlite3.connect('databaze.db')
    cursor2 = connection2.cursor()
    cursor2.execute("SELECT * FROM Products")
    products = cursor2.fetchall()
    connection2.close()
    return products


def add_user(username, email, age):
    connection_add = sqlite3.connect('databaze.db')  # setup DataBase
    cursor_add = connection_add.cursor()
    cursor_add.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                       (f"{username}", f"{email}", age, 1000)
                       )
    connection_add.commit()
    connection_add.close()


def is_included(username):
    connection_add = sqlite3.connect('databaze.db')  # setup DataBase
    cursor_add = connection_add.cursor()
    check_user = cursor_add.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_user.fetchone() is None:
        connection_add.commit()
        connection_add.close()
        return False  # имя пользователя не обнаружено
    else:
        return True  # обнаружен пользователь в записях


if __name__ == '__main__':
    connection = sqlite3.connect('databaze.db')  # setup DataBase
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
                                    id          INTEGER PRIMARY KEY,
                                    title       TEXT NOT NULL,
                                    description TEXT,
                                    price       FLOAT
                                        )
                ''')
    for i in range(4):  # этот код генерирует записи продуктов, выполняем 1 раз в этом коде:
        cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f"Продукт {i + 1}", f"Описание {i + 1}", (i + 1) * 100)
                       )
    prods = get_all_products()
    for prod in prods:
        print(prod)

    connection.commit()
    connection.close()
