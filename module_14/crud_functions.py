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
