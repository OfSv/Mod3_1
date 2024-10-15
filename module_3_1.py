calls = 0
#string = ''


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    sp = []
    count_calls()
    sp.append(len(string))
    sp.append(string.upper())
    sp.append(string.lower())
    return tuple(sp)


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if type(list_to_search[i]) == str:
            list_to_search[i] = list_to_search[i].lower()   
            continue
    if string.lower() in list_to_search:
        return True
    else:
        return False


print(string_info('Привет'))
print(is_contains('Привет', [1, 5.2, 3]))
print(is_contains('Привет', [1, 5.2, 'привеТ']))
print(string_info(('Пока')))
print(is_contains('Пока', ["Кот", "ПОКА", True]))
print(is_contains('Провека', [8.3, 12]))
print(string_info(('Проверка')))

print('Количество вызванных функций" ', calls)