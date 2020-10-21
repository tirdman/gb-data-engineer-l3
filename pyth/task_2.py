"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def show_user_data(name, family, bday, city, email, phone):
    """
    Функция выводит информацию о пользователе
    :param name: имя
    :param family: фамилия
    :param bday: год рожения
    :param city: город проживания
    :param email: адрес электронной почты
    :param phone: номер телефона
    :return: Функция выводит на экран информацию о пользователе и также возвращает строку с информаией
    """
    return f'{name} {family} {bday} года рождения, проживает в городе {city}, email: {email}, телефон: {phone}'


in_name = input('Введите имя: ')
in_family = input('Введите фамилию: ')
in_bday = input('Введите год рождения: ')
in_city = input('Введите город проживания: ')
in_email = input('Введите email: ')
in_phone = input('Введите номер телефона: ')

print(show_user_data(name=in_name, family=in_family, bday=in_bday, city=in_city, email=in_email, phone=in_phone))
