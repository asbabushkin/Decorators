"""
Easy:
    Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск
    функции суммирования.
"""

CNT = 0


def summarize(*args):
    return sum(args)


def decorator_count(some_func):
    def inner(*args):
        global CNT
        summa = some_func(*args)
        CNT += 1
        print(f'Функция суммирования запускалась {CNT} раз')
        return f'Сумма аргументов {args} составляет: {summa}'

    return inner


result = decorator_count(summarize)

print(result(2, 3))
print(result(3, 4, 5))
print(result(5, 6, 7, 8, 9, 10))