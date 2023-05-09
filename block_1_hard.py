"""
Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы,
первые 2 аргумента из дополнительных позиционных аргументов и любой аргумент из дополнительных аргументов
(если они есть), переданных по ключу (если они есть).
"""
import random


def summarize_upd(num_1, num_2, num_3, num_4, *args, **kwargs):
    if len(kwargs) > 0:
        print(args)
        print(args[0:2])
        return num_1 + num_2 + num_3 + num_4 + sum(args[0:2]) + random.choice(list(kwargs.values()))
    else:
        return num_1 + num_2 + num_3 + num_4 + sum(args[0:2])

print(summarize_upd(1, 2, 3, 4, 5, 6, 7, 8, num_10=10, num_11=100, num_12=1000))