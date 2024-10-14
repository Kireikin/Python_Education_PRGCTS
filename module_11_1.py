"""
"Обзор сторонних библиотек Python"
Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.
установлены через терминал командой pip install requests (pandas, numpy, matplotlib, pillow)
отчет об установленных библиотеках командой в консоли:
pip freeze > reqs.txt
certifi==2024.8.30
charset-normalizer==3.4.0
contourpy==1.3.0
cycler==0.12.1
fonttools==4.54.1
idna==3.10
kiwisolver==1.4.7
matplotlib==3.9.2
numpy==2.1.2
packaging==24.1
pandas==2.2.3
pillow==10.4.0
pyparsing==3.1.4
python-dateutil==2.9.0.post0
pytz==2024.2
requests==2.32.3
six==1.16.0
tzdata==2024.2
urllib3==2.2.3
"""
from pprint import pprint
# import requests
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
from pillow import Image


if __name__ == "__main__":

    # 1   # запросы к внешним сайтам и библиотека requests:

    # HTTP-запросы PUT, DELETE, HEAD и OPTIONS:
    # r = requests.put('https://httpbin.org/put', data={'key': 'value'})
    # r = requests.delete('https://httpbin.org/delete')
    # r = requests.head('https://httpbin.org/get')
    # r = requests.options('https://httpbin.org/get'

    # payload = {'key1': 'value1', 'key2': ['value2', 'value3']}  # контейнер с данными для считывания/выгрузки
    # r = requests.get('https://httpbin.org/get', params=payload)  # запрос-чтение с сайта данных
    # print(r.url)

    # r = requests.get('https://api.github.com/events') r.json() # перекодировка json()? запрос с записью в файл о
    # содержимом страницы? r = requests.get('https://yandex.ru', stream=True) with open('filename.txt', 'wb') as fd:
    # for chunk in r.iter_content(chunk_size=128): fd.write(chunk)
    #
    # 2   # библиотека numpy => np - математическая библиотека
    # для работы с матрицами и векторами! обращение почти как в matlab! обязательно попробую портировать свой алгоритм.

    # data = np.array([[1, 2], [3, 4]])
    # ones = np.array([[1, 1], [1, 1]])
    # pprint(data + ones)

    # 3   # библиотека matplotlib - для построения окон с графиками, возможно применение с библиотекой numpy:
    # в декартовых координатах по двум осям:

    # a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
    # x = np.linspace(0, 5, 20)
    # y = np.linspace(0, 10, 20)
    # plt.plot(x, y, 'purple')  # line
    # plt.plot(x, y, 'o')  # dots
    # plt.plot(a)
    # plt.show()

    # в декартовых координатах по трем осям:

    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # X = np.arange(-5, 5, 0.15)
    # Y = np.arange(-5, 5, 0.15)
    # X, Y = np.meshgrid(X, Y)
    # R = np.sqrt(X ** 2 + Y ** 2)
    # Z = np.sin(R)
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
    # plt.show()

    # Matplotlib - это комплексная библиотека для создания статических, анимированных и интерактивных визуализаций на
    # Python. В том числе построение графиков типа y=f(x), статистических диаграм, 3Д и просто обьёмные графики.

    # 4   # Библиотека pandas - отличный инструмент для обработки данных, в том числе чтения данных из файлов
    # имеет внутренние два класса данных - Series: одномерный помеченный массив, содержащий данные любого типа и
    # DataFrame: двумерная структура данных, которая хранит данные в виде двумерного массива или таблицы со строками
    # и столбцами. Также позволяет сортировать, делать выборку, исключать/заменять выбитые или ложные данные, объединять
    #  преобразовывать в други форматы  и тд. Работает совместно с numpy, matplotlib а самое главное работает с
    #  электронными таблицами CSV
    df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
    df.to_csv("foo.csv")
    pprint(pd.read_csv("foo.csv"))

    # в целом изучение библиотеки pandas не на один месяц

    # Библиотека pillow обеспечивает широкую поддержку форматов файлов, эффективное внутреннее представление и
    # довольно мощные возможности обработки изображений.
    Image.show('cat_jump.jpg')
