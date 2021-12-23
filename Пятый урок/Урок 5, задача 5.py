# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

sum = 0
numbers = []
file = open('5.5.txt', 'w+')

for _ in range(4):
    file.write(str(random.randint(0, 200)) + ' ')

file.seek(0)
line = file.read()

numbers = line.split(' ')
for el in range(len(numbers) - 1):
    number = int(numbers[el])
    sum += number

print('Сумма числел равна: ', sum)
