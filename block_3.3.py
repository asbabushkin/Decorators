"""
3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена
    с теми параметрами с которыми она уже запускалась - брать результат из кэша и не производить
    повторное выполнение функции.
3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм
    автоматической очистки кэша в процессе выполнения функций.
"""

from datetime import datetime
from time import sleep
from typing import Callable

CACHE = dict()
arg_lst = [[1, 2], [2, 1], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12, 13], [14, 15, 16, 17], [1, 2], [3, 4], [1, 7, 9],
           [99, 199], [11, 22, 33], [44, 55, 66]]
arg_lst_sugar = [[1, 2, 3], [4, 5, 6], [11, 22, 33], [44, 55, 66]]
arg_lst_sugar_param = [[7, 8, 9], [10, 11, 12], [99, 199], [1, 2], [99, 199], [1, 2]]


def summarize(*args):
    return sum(args)


def clean_cache():
    global CACHE
    cache_local = dict()
    for ar in CACHE.keys():
        timedelta = datetime.now() - CACHE[ar]['time_calc']
        if timedelta.seconds <= 10:
            cache_local[ar] = CACHE[ar]
        else:
            print(f'Функция с аргументами {ar} вычислена {timedelta.seconds} секунд назад. Данные устарели. Удаляем.')
    CACHE = cache_local
    return CACHE


# функциональный декоратор без параметров
def decor_func(func: Callable) -> Callable:
    def inner(*args):
        global CACHE
        args_tpl = tuple(sorted(args))

        sleep(1)
        clean_cache()
        if args_tpl in CACHE.keys():
            return f'{CACHE[args_tpl]["result"]} получено из кэша'
        else:
            res = func(*args)
            CACHE[args_tpl] = {
                'result': res,
                'time_calc': datetime.now()
            }
        return res

    return inner


summa = decor_func(summarize)
print('***\nРаботает функциональный декоратор без параметров!\n***')
[print(f'Аргументы: {ar}, сумма = {summa(*ar)}') for ar in arg_lst]
print(f'Кэш: {CACHE}')


# сахарный декоратор без параметров:

def sugar_decorator(func: Callable) -> Callable:
    def inner(*args):
        global CACHE
        args_tpl = tuple(sorted(args))

        sleep(1)
        clean_cache()
        if args_tpl in CACHE.keys():
            return f'{CACHE[args_tpl]["result"]} получено из кэша'
        else:
            res = func(*args)
            CACHE[args_tpl] = {
                'result': res,
                'time_calc': datetime.now()
            }
        return res

    return inner


@sugar_decorator
def summarize_sugar(*args):
    return sum(args)


print('***\nРаботает сахарный декоратор без параметров!\n***')
[print(f'Аргументы: {ar}, сумма = {summarize_sugar(*ar)}') for ar in arg_lst_sugar]
print(f'Кэш: {CACHE}')

"""
3.3 Параметризовать время кэширования в декораторе.
"""


# сахарный декоратор параметризованный
def clean_cache_param(cache_time: int) -> dict:
    global CACHE
    cache_local = dict()
    for ar in CACHE.keys():
        timedelta = datetime.now() - CACHE[ar]['time_calc']
        if timedelta.seconds <= cache_time:
            cache_local[ar] = CACHE[ar]
        else:
            print(f'Функция с аргументами {ar} вычислена {timedelta.seconds} секунд назад. Данные устарели. Удаляем.')
    CACHE = cache_local
    return CACHE


def sugar_decor_param(cache_time: int) -> Callable:
    def outer(func: Callable) -> Callable:
        def inner(*args):
            global CACHE
            args_tpl = tuple(sorted(args))

            sleep(1)
            clean_cache_param(cache_time)
            if args_tpl in CACHE.keys():
                return f'{CACHE[args_tpl]["result"]} получено из кэша'
            else:
                res = func(*args)
                CACHE[args_tpl] = {
                    'result': res,
                    'time_calc': datetime.now()
                }
            return res

        return inner

    return outer


@sugar_decor_param(5)
def summarize_sugar_param(*args):
    return sum(args)


print('***\nРаботает сахарный декоратор параметризованый!\n***')
[print(f'Аргументы: {ar}, сумма = {summarize_sugar_param(*ar)}') for ar in arg_lst_sugar_param]
print(f'Кэш: {CACHE}')


# функциональный декоратор параметризованный
def func_decor_param(func: Callable, cache_time: int) -> Callable:
    def inner(*args):
        global CACHE
        args_tpl = tuple(sorted(args))

        sleep(1)
        clean_cache_param(cache_time)
        if args_tpl in CACHE.keys():
            return f'{CACHE[args_tpl]["result"]} получено из кэша'
        else:
            res = func(*args)
            CACHE[args_tpl] = {
                'result': res,
                'time_calc': datetime.now()
            }
        return res

    return inner


result = func_decor_param(summarize, 10)
print('***\nРаботает функциональный декоратор параметризованый!\n***')
[print(f'Аргументы: {ar}, сумма = {result(*ar)}') for ar in arg_lst]
print(CACHE)
