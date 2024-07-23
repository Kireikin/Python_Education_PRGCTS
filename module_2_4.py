numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 1, 2, 3, 4]
# обьявляю пустые списки
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    # Исключаю единицу в значениях - пропускаю её проверку
    if numbers[i] != 1:
        # организую цикл проверки деления на 2 с шагом 1 до числа в numbers[i] - 1
        for j in range(2,numbers[i]-1):
            # если найден один из множителей
            if (numbers[i] % j == 0):
                is_prime = False
                break
            else:
                is_prime = True
        # заполняем списки по флагу is_prime
        if  is_prime:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
# Результат:
print(primes)
print(not_primes)
