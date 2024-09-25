"""
"Итераторы"
Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__. Закрепить навык создания
и выбрасывания исключений.
"""


class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step if step >= 0 else StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self.pointer

    def __next__(self):

