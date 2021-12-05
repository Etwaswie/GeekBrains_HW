# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division(first_num, second_num):
    if second_num == 0:
        return f"Не могу делить на {second_num}!"
    div = first_num / second_num
    return f"Результат деления: {div}"


print(division(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
