import time
import math

cache1 = {"count": 0, "time": 0, "info": 'Recursion computation'}
cache2 = {"count": 0, "time": 0, "info": 'Closed-form expression'}
cache3 = {"count": 0, "time": 0, "info": 'Space optimization'}
cache4 = {"count": 0, "time": 0, "info": 'Cash optimization'}


def profiling_decorator(function):
    def wrapper(func):
        def inner(*args, **kwargs):
            globals()[function]['count'] += 1
            if globals()[function]['count'] == 1:
                star_time = time.time()
                func_ans = func(*args, **kwargs)
                end_time = time.time() - star_time
                globals()[function]['time'] += end_time
            else:
                func_ans = func(*args, **kwargs)

            return func_ans
        return inner
    return wrapper


@profiling_decorator('cache1')
def fibonacci_function_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_function_1(n-1) + fibonacci_function_1(n-2)


@profiling_decorator('cache2')
def fibonacci_function_2(n):
    sqrt5 = math.sqrt(5)
    phi = (sqrt5 + 1) / 2
    return int(phi ** n / sqrt5 + 0.5)


@profiling_decorator('cache3')
def fibonacci_function_3(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


cache = {}


@profiling_decorator('cache4')
def fibonacci_function_4(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fibonacci_function_4(n - 1) + fibonacci_function_4(n - 2)
    return cache[n]


def find_best(cache1, cache2, cache3, cache4):
    result = [cache1, cache2, cache3, cache4]
    best_time = result[0]['time']
    best_count = result[0]['count']
    for i in result:
        if best_time > i['time']:
            best_time = i['time']
        if best_count > i['count']:
            best_count = i['count']
    print(f"Best time: {best_time}")
    print(f"Best iterations: {best_count}")


fibonacci_function_1(30)
print('global1: ', cache1)

fibonacci_function_2(30)
print('global2: ', cache2)

fibonacci_function_3(30)
print('global3: ', cache3)

fibonacci_function_4(30)
print('global4: ', cache4)

find_best(cache1, cache2, cache3, cache4)

