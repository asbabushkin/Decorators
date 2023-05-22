"""
Easy:
    Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск
    функции суммирования.
"""

cnt = 0

def summarize(*args):
    return sum(args)

def decorator_count(some_func):
    def inner(*args):
        global cnt
        summa = some_func(*args)
        cnt += 1
        print(f'Функция суммирования запускалась {cnt} раз')
        return f'Сумма аргументов {args} составляет: {summa}'
    return inner

result = decorator_count(summarize)
print(result(2, 3))
print(result(3, 4, 5))
print(result(5, 6, 7, 8, 9, 10))


