"""
1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов
    будет показывать в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.

"""
from typing import Callable


def summirize(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


# Функциональный декоратор без параметров
def decor_func(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print('Функциональный декоратор без параметров: Покупайте наших котиков!')
        summa = func(*args, **kwargs)
        return summa

    return inner


result = decor_func(summirize)
print(f'Функциональный декоратор без параметров. Сумма = {result(1, 2, 3, 4)}\n***')


# Сахарный декоратор без параметров

def decor_sugar(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print('Сахарный декоратор без параметров: Покупайте наших котиков!')
        summa = func(*args, **kwargs)
        return summa

    return inner


@decor_sugar
def summirize_sugar(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(f'Сахарный декоратор без параметров. Сумма = {summirize_sugar(1, 3, 5)}\n***')

"""
1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции
    можно было задавать как параметр во время декорирования.
"""

message = input('Пожалуйста, введите сообщение для функционального декоратора с параметром: ')
sugar_message = input('Пожалуйста, введите сообщение для "сахарного" декоратора с параметром: ')


# Функциональный декоратор с параметром
def decor_func_param(func: Callable, message: str) -> Callable:
    def inner(*args, **kwargs):
        print('***\n' + message)
        summa = func(*args, **kwargs)
        return summa

    return inner


result = decor_func_param(summirize, message)
print(f'Функциональный декоратор с параметром. Цена = {result(1, 2, 3, 4)}\n***')


# Сахарный декоратор с параметром
def decor_sugar_param(message: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner(*args, **kwargs) -> Callable:
            print(sugar_message)
            result = func(*args, **kwargs)
            return result

        return inner

    return wrapper


@decor_sugar_param(sugar_message)
def stringifier(*args, **kwargs):
    return ''.join(map(str, [*args, *kwargs.values()]))


print(f'Функциональный декоратор с параметром. Цена = {stringifier(1, 5, 9)}')
