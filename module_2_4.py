numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False
for i in range(len(numbers)):
    for j in (2,3,5,7):
        if (numbers[i] % j == 0) and (numbers[i] != j):
            is_prime = False
            break
        else:
            is_prime = True
            continue
    # Исключаю единицу
    if numbers[i] == 1:
        ()
    elif is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
# Результат:
print(primes)
print(not_primes)
