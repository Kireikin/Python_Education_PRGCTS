def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


#  test example
result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(252525)
print(result)
result = get_multiplied_digits(22)
print(result)
result = get_multiplied_digits(0)
print(result)
result = get_multiplied_digits(21)
print(result)
