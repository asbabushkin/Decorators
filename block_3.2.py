"""
2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы
    в случае успешного выполнения. В случае возникновения ошибки во время выполнения функции
    нужно сделать так, чтобы выполнение функции было повторено ещё раз с теми же самыми аргументами,
    но не более 10 раз. Если после последней попытки функцию так и не удастся выполнить успешно,
    то бросать исключение.

"""
from typing import Callable


def divider(dividend, divider):
    return dividend / divider


# функциональный декоратор без параметров
def decor_func(func: Callable) -> Callable:
    def inner(a, b):
        attempt = 1
        while attempt < 11:
            try:
                quotient = func(a, b)
                return quotient
            except Exception as err:
                print(f'Функциональный декоратор без параметров: Попытка № {attempt}, перехвачена ошибка: {err}')
                attempt += 1
        raise Exception('Функциональный декоратор без параметров: Делитель не может быть равным 0!')

    return inner


result_func = decor_func(divider)


print(f'Функциональный декоратор без параметров: Частное = {result_func(10, 2)}')
print(f'Функциональный декоратор без параметров: Частное = {result_func(10, 0)}')


# сахарный декоратор без параметров:
def decor_sugar(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        attempt = 1
        while attempt < 11:
            try:
                quotient = func(*args, **kwargs)
                return quotient
            except Exception as err:
                print(f'Сахарный декоратор без параметров: Попытка № {attempt}, перехвачена ошибка: {err}')
                attempt += 1
        raise Exception('Сахарный декоратор без параметров: Делитель не может быть равным 0!')

    return inner


@decor_sugar
def divider_sugar(dividend, divider):
    return dividend / divider


# print(f'Сахарный декоратор без параметров: Частное = {divider_sugar(5, 2)}')
# print(f'Сахарный декоратор без параметров: Частное = {divider_sugar(5, 0)}')

"""
    2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции 
    можно было задавать как параметр во время декорирования.
"""


# Функциональный декоратор с параметром:
def decor_func_param(func: Callable, attempts: int) -> Callable:
    def inner(a, b):
        att = 1
        while att <= attempts:
            try:
                quotient = func(a, b)
                return quotient
            except Exception as err:
                print(f'Функциональный декоратор с параметром: Попытка № {att}, перехвачена ошибка: {err}')
                att += 1
        raise Exception('Функциональный декоратор с параметром: Делитель не может быть равным 0!')

    return inner


result_func_param = decor_func_param(divider, 5)


# print(f'Функциональный декоратор с параметром: частное = {result_func_param(9, 2)}')
# print(f'Функциональный декоратор с параметром: частное = {result_func_param(9, 0)}')


# Сахарный декоратор с параметром:
def decor_sugar_param(attempts: int) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner(a: int, b: int) -> Callable:
            att = 1
            while att <= attempts:
                try:
                    quotient = func(a, b)
                    return quotient
                except Exception as err:
                    print(f'Сахарный декоратор с параметром: Попытка № {att}, перехвачена ошибка: {err}')
                    att += 1
            raise Exception('Сахарный декоратор с параметром: Делитель не может быть равным 0!')

        return inner

    return wrapper


@decor_sugar_param(7)
def divider_sugar_param(dividend, divider):
    return dividend / divider

# print(f'Сахарный декоратор с параметром: частное = {divider_sugar_param(9, 1)}')
# print(f'Сахарный декоратор с параметром: частное = {divider_sugar_param(9, 0)}')
