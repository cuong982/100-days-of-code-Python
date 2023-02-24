# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
Use time.time()
Use timeit.default_timer()
Use timeit from the command line
Use timeit in code
Use timeit in Jupyer Notebook Cells
Use a decorator
"""

import timeit
from timeit import default_timer as timer


def timer_func(func):
    def wrapper(*args, **kwargs):
        t1 = timer()
        result = func(*args, **kwargs)
        t2 = timer()
        print(f'{func.__name__}() executed in {(t2-t1):.6f}s')
        return result
    return wrapper


@timer_func
def do_something():
    for i in range(1000000): i * i


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(timeit.timeit(lambda: "-".join(map(str, range(100))), number=1000))
    do_something()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
