immutable_var = ('Кортеж', 12345, True, [1, 2, True], [4, 'Text'], [7, False])
print(immutable_var)
# immutable_var[0] = 1  - TypeError: 'tuple' object does not support item assignment
mutable_list = immutable_var[3:]
mutable_list[1][1] = "Modified"
print(mutable_list)
