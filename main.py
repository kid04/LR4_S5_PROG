import functools


class FibonacciLst:

    def __init__(self, instance):
        self.instance = instance
        self.idx = 0
        self.lst = [1, 1]

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx]

            except IndexError:
                raise StopIteration
            while res > self.lst[-1]:
                self.lst.append(self.lst[-2]+self.lst[-1])
            if res in self.lst:
                self.idx += 1
                return res

            self.idx += 1





def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res




def my_genn():
    """Сопрограмма"""
    while True:
        number_of_fib_elem = yield
        print(number_of_fib_elem)
        l = [str(number_of_fib_elem) + ":"]
        a = 0
        b = 1
        for i in range(number_of_fib_elem):
            l.append(a)
            res = a + b
            a = b
            b = res
        yield l


def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen

    return inner

my_genn = fib_coroutine(my_genn)


