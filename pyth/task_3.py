"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func1(num1, num2, num3):
    """
    Функция возвращает сумму 2-х максимальных позиционных аргументов
    Реализация использует функцию sorted
    :param num1: число1
    :param num2: число2
    :param num3: число3
    :return: Сумма 2-х максимальных аргументов
    """

    """
    Реализация не соответствует заданию, так как используется функция sorted, а не sort
    В случае sort код был бы длинее, так как она сортирует список на месте:
    num_list = [num1, num2, num3]
    num_list.sort()
    return sum(sorted(num_list)[-2:])
    """
    return sum(sorted([num1, num2, num3])[-2:])



def my_func2(num1, num2, num3):
    """
    Функция возвращает сумму 2-х максимальных позиционных аргументов
    Реализация не использует функцию sort
    :param num1: число1
    :param num2: число2
    :param num3: число3
    :return: Сумма 2-х максимальных аргументов
    """
    list_nums = [num1, num2, num3]
    max_int1 = max(list_nums)
    list_nums.remove(max_int1)
    max_int2 = max(list_nums)
    return max_int1 + max_int2


while True:
    try:
        num_in1 = float(input('Введите первое число: '))
        num_in2 = float(input('Введите второе число: '))
        num_in3 = float(input('Введите третье число: '))
    except ValueError:
        print("Вы ввели не цифру. Попробуйте заново.")
        continue
    else:
        break

print(f'Способ 1: {my_func1(num_in1, num_in2, num_in3)}')
print(f'Способ 2: {my_func2(num_in1, num_in2, num_in3)}')
