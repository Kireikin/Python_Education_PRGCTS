def pair_sum(number):
    pair = []
    for i in range(1, number+1):
        for j in range(1, i):
            if number % (i + j) == 0:
                pair.append([j, i])
                #  pair.append(i)
    #  pair.sort()
    return pair


for n in range(3, 20+1):
    result = pair_sum(n)
    print(n, ':', *result)
