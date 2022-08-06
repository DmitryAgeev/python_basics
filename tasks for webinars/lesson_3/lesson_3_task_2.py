"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(first_name, last_name, year_of_birth, city, email, phone):
    return f'{last_name} {first_name}, year of birth: {year_of_birth}, location: {city}. ' \
           f'Contacts: {email} , {phone} .'


print(user_data(
    first_name=input('Enter your name: '),
    last_name=input('Enter your last name: '),
    year_of_birth=input('Enter the year of birth: '),
    city=input('Enter city of residence: '),
    email=input('Enter your email: '),
    phone=input('Enter phone number: '),
))
