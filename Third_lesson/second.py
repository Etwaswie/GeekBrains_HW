# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_info(name: str, surname: str, birthday, city: str, email, phone):
    return print(f'Имя: {name}, фамилия: {surname}, год рождения: {birthday}, город: {city}, email: {email},телефон: {phone}.')



user_info(
    name = input('Имя: '),
    surname = input('Фамилия: '),
    birthday = input('Год Рождения: '),
    city = input('Город: '),
    email = input('Почта: '),
    phone = input('Телефон: '),
)

