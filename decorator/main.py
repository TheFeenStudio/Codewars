def decorator(func):
    import time

    def wrapper(list):
        t = time.time()
        a = func(list)
        print(f'[*] Время выполнения кода - {t}')
        print(f'Результат - {a}')

    return wrapper


@decorator
def sum(list):
    count = 0
    for i in list:
        count += i
    return count


sum([1, 2, 3, 4, 5, 6, 7])
