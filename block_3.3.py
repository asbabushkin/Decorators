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


def summarize(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


def clean_cache():
    global CACHE
    cache_local = dict()
    for ar in CACHE.keys():
        timedelta = datetime.now() - CACHE[ar]['time_calc']
        if timedelta.seconds <= 10:
            cache_local[ar] = CACHE[ar]
        else:
            print(
                f'Функция с аргументами {ar} вычислена более {timedelta.seconds} секунд назад. Данные устарели. Удаляем из кэша.')
    CACHE = cache_local
    return CACHE


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


arg_lst = [[1, 2], [2, 1], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12, 13], [14, 15, 16, 17], [1, 2], [3, 4], [1, 7, 9],
           [99, 199], [11, 22, 33], [44, 55, 66]]
summa = decor_func(summarize)

for ar in arg_lst:
    print(f'Аргументы: {ar}, сумма = {summa(*ar)}')

print(f'Кэш: {CACHE}')

"""
3.3 Параметризовать время кэширования в декораторе.
"""
