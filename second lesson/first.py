# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

new_list = ['Машина', False, 5, 10.34, [1, 2, 3], (1, 2, 3), {1, 2, 3}, 5 + 6j, {'name': 'John', 'color': 'green'}]

for el in new_list:
    print(type(el))