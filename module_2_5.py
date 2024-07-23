def get_matrix(n, m, value):
    matrix = []
    for i in range(0,n):
        matrix.append(['']*m)
        for j in range(m):
            matrix[i][j] = value
    # строки 2-6 можно заменить "генератором матрицы" стр. 8
    #matrix = [[value for j in range(m)] for i in range(n)]
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
