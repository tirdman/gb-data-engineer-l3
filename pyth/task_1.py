"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def div_numbers(num1, num2):
    """
    Функция выполняет деление двух чисел
    :param num1: числитель
    :param num2: знаменатель
    :return: результат деления
    """
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')


while True:
    try:
        num_in1 = float(input('Введите первое число: '))
        num_in2 = float(input('Введите второе число: '))
    except ValueError:
        print("Вы ввели не цифру. Попробуйте заново.")
        continue
    else:
        break

div_result = div_numbers(num_in1, num_in2)
if div_result:
    print(div_result)
