"""
Medium
    1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той,
        котоая была решена для запуска функции суммирования.
    2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться
        в качестве результата работы из объемлющей функции.
    3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте
        результат на экран. Что наблюдаете?
    4. Осуществите вызов функции суммирования из полученной переменной.
"""
from typing import Callable

'''
1.1 Функция принимает на вход любое количество аргументов и возвращает максимальное из них. Декоратор 
определяет является ли полученный результат четным числом.
'''

CNT_EVEN = 0


def find_max(*args):
    return max(args)


def decorator_findmax(func: Callable) -> Callable:
    def inner(*args):
        global CNT_EVEN
        inner_result = func(*args)
        CNT_EVEN += 1
        print('***')
        print(f'Функция поиска максимального числа запускалась {CNT_EVEN} раз.')
        print(f'В наборе {args} максимальным числом является {inner_result}')
        if inner_result % 2 == 0:
            print(f'{inner_result} является четным числом')
            return True
        else:
            print(f'{inner_result} является нечетным числом')
            return False

    return inner


result_is_even = decorator_findmax(find_max)
print('Задание 1.1:')
print(result_is_even(1, 3, 5))
print(result_is_even(-1, -3, -5))
print(result_is_even(-7, 7))
print(result_is_even(0, 7, 12, 36), '\n')

'''
1.1 Функция принимает на вход любое количество аргументов и возвращает их сумму. Декоратор 
определяет количество цифр в данном числе.
'''

CNT_LEN = 0


def summarize(*args):
    return sum(args)


def decorator_get_length(func: Callable) -> Callable:
    def inner(*args):
        global CNT_LEN
        inner_result = func(*args)
        CNT_LEN += 1
        print('***')
        print(f'Функция суммирования запускалась {CNT_LEN} раз.')
        print(f'Число {inner_result} является {len(str(inner_result))}-значным')
        return inner_result

    return inner


result_len = decorator_get_length(summarize)
print('Задание 1.2:')
print(result_len(1, 5, 9))
print(result_len(1, 2, 3))
print(result_len(100, 2, 3))
print(result_len(1000, 138, 39))

'''
1.3 Функция принимает на вход любое количество аргументов и возвращает их среднее. Декоратор 
вычисляет разницу между минимальным числом из данного набора и средним.
'''

CNT_AVG = 0


def get_average(*args):
    return round(sum(args) / len(args), 2)


def decorator_avg(func: Callable) -> Callable:
    def inner(*args):
        global CNT_AVG
        inner_result = get_average(*args)
        CNT_AVG += 1
        print('***')
        print(f'Функция нахождения среднего запускалась {CNT_AVG} раз.')
        print(f'Для набора {args} среднеарифметическим является {inner_result}')
        print(f'Минимальное число меньше среднеарифметического на {inner_result - min(args)}')
        return inner_result

    return inner


result_diff = decorator_avg(get_average)

print('Задание 1.3:')
print(result_diff(1, 3, 5))
print(result_diff(2, 3, 5))
print(result_diff(0, 5, 28))

"""
2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться
    в качестве результата работы из объемлющей функции.
"""


def foo():
    def summarize(*args):
        return sum(args)

    return summarize


"""
3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте
    результат на экран. Что наблюдаете?
"""

result_sum = foo()
print(result_sum)  # будет напечатан адрес объекта локальной функции summarize в памяти

"""
    4. Осуществите вызов функции суммирования из полученной переменной.
"""

print('Summa: ', result_sum(1, 5, 10))
