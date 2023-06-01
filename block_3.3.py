"""
3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена
    с теми параметрами с которыми она уже запускалась - брать результат из кэша и не производить
    повторное выполнение функции.

"""
from datetime import datetime
from typing import Callable

cache = dict()


def summarize(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


def decor_func(func: Callable) -> Callable:
    def inner(*args):
        global cache
        args_tpl = tuple(sorted(args))
        if args_tpl in cache:
            return f'Получено из кэша: {cache[args_tpl]["result"]}'
        else:
            res = func(*args)
            cache[args_tpl] = {
                'result': res,
                'time_calc': datetime.now()
                }
        return res

    return inner


summa = decor_func(summarize)
print(summa(2, 3))
print(summa(4, 5))
print(summa(6, 7))
print(summa(2, 3))
print(summa(8, 9))

print(cache)

"""
3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм 
    автоматической очистки кэша в процессе выполнения функций.     
"""

"""
3.3 Параметризовать время кэширования в декораторе.
"""
