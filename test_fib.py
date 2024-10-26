from main import my_genn
from main import FibonacciLst


def test_fib_1():
    gen = my_genn()
    assert gen.send(3) == ["3:", 0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"


def test_fib_2():
    gen = my_genn()
    assert gen.send(5) == ["5:", 0, 1, 1, 2, 3], "Пять первых членов ряда"

def test_fib_lst_1():
    assert list(FibonacciLst(range(30))) == [1, 2, 3, 5, 8, 13, 21], "Числа Фибоначчи в списке чисел от 0 до 30"

def test_fib_lst_r():
    assert list(FibonacciLst(range(30, 0, -1))) == [21, 13, 8, 5, 3, 2, 1], "Числа Фибоначчи в списке чисел от 30 до 0"
    