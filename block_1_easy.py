"""
Easy
    1. Написать простую функцию, которая на вход принимает строку ('test') и целое число (3),
        а возвращает строку вида 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.
    2. Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
    3. Вызвать функцию суммирования через переменную, в которую вы только что её записали.

"""


# Шаг 1
def easy_func_1(string, num):
    new_string = string
    for n in range(num - 1):
        if new_string[-1].isupper():
            new_string += string.lower()
        else:
            new_string += string.upper()
    return new_string


print(easy_func_1('TEST', 6))

# Шаг 2. Видим адрес объекта функции в памяти
func_perem = easy_func_1
print(f'func_perem: {func_perem}')

# Шаг 3. Вызов функции суммирования строк через переменную.
print(f'Вызов func_perem: {func_perem("test", 5)}')
