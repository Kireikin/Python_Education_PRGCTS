def count_calls():
    global calls
    calls = calls + 1
    return


def string_info(string):
    count_calls()
    return [len(string), string.upper(), string.lower()]


def is_contains(string, contains):
    count_calls()
    for i in contains:
        if string.casefold() in i.casefold():
            return True
    return False


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
