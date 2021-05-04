"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
import math


def reverse(x):
    next_digit = x % 10
    if x < 10:
        return next_digit
    else:
        exp = int(math.log10(x))  # беру логарифм по основанию 10, чтобы узнать количество разрядов минус 1
        return next_digit * (10 ** exp) + reverse(x // 10)  # умножаю первые числа на 10 в степени exp


num = int(input('введите натуральное число: '))
print(reverse(num))