from math import sqrt


def add_numbers(first, second):
    return first + second


def CalculateSquareRoot(Number):
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return

    return f"Мы вычислили квадратный корень из введённого вами числа. \
Это будет: {CalculateSquareRoot(your_number)}"


first = 10
second = 5

print('Сумма чисел: ', add_numbers(first, second))

print(calc(25.5))
print(6)
