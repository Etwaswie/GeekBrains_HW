# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number_n = int(input('Введите число: '))

n = number_n
count = 0
result = 0

while n != 0:
    count += 1
    n = n // 10

for i in range(0, 3):
    result = result + (3 - i) * (number_n * 10 ** (count * i))

print(f'Результат вычисления: {result}')




