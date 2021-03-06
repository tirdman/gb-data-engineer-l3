"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

QUIT_SYMBOL = 'q'


def sum_num_line(nums_string):
    """
    Функция суммирует числа в строке, которые разделяет пробел
    Если встречаются не цифры, то они игнорируются
    Если в строке встречается символ "q", то суммируются числа до этого символа
    :param nums_string: строка чисел (допускаются строки, символ "q" является признаком завершения суммирования),
    разделенные через запятую.
    :return: возвращается кортеж из двух элементов:
    1) Сумма чисел
    2) Признак присутствия в строке отдельного символа "q"
    """
    next_nums = []
    find_quit = False

    for next_word in nums_string.split(' '):
        if next_word == QUIT_SYMBOL:
            find_quit = True
            break
        try:
            next_nums.append(float(next_word))
        except ValueError:
            continue

    return sum(next_nums), find_quit


nums_sum = 0
print('Для выхода введите символ "q"')
while True:
    in_str = input('Введите строку чисел, разделенную пробелами: ')
    next_line_sum, is_exit = sum_num_line(in_str)
    nums_sum += next_line_sum

    print(f'Сумма чисел: {nums_sum}')

    if is_exit:
        break
