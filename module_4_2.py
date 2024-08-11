def test_function():
    def inner_function(message):
        global flag
        print(message)

        def inner_function2():
            print("Я в области видимости функции inner_function2")
            message2 = "Я вызван в области видимости функции inner_function2"
            inner_function(message2)
            return
        if flag:  # заглушка от зацикливания
            flag = False
            inner_function2()

    inner_function("Я в области видимости функции test_function")
    return


flag = True
test_function()
# inner_function()  # NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# Вывод: вызов функций, как и значений в области "сверху" не возможен, вызов функций в областях "снизу в верх"
# допускается, измение значений при обьявлении глобальными. Как сделать защиту значений от изменений снизу?
