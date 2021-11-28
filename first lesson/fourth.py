# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
max_num = 0

number_n = int(input('Введите число: '))

while number_n > 0:
    if number_n % 10 > max_num:
        max_num = number_n % 10
    number_n = number_n // 10

print(f"Максимальная цифра числа: {max_num}")
