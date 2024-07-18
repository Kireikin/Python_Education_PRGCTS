# исходные данные
# в алфафитном порядке
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# список как есть
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# вычисляем средний балл:
av_grade = (sum(grades[0])/len(grades[0]),
            sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]),
            sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4]))
# Преобразуем и сортируем список в алфавитном порядке
students = list(students)
students = sorted(students)
# собираем в список с вычисленым средним баллом
# average_list = {students[0]: av_grade[0],
#                 students[1]: av_grade[1],
#                 students[2]: av_grade[2],
#                 students[3]: av_grade[3],
#                 students[4]: av_grade[4]}
average_list = dict([[students[0], av_grade[0]],
                    [students[1], av_grade[1]],
                    [students[2], av_grade[2]],
                    [students[3], av_grade[3]],
                    [students[4], av_grade[4]]])
# результат
print(average_list)