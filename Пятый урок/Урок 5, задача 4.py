# 4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.

# numbers = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#
# with open('5.4.txt', encoding="utf-8") as file:
#     new_file = open('5.4.1.txt', 'a', encoding="utf-8")
#
#     for line in file:
#         for el in range(len(line)):
#             if line[el].isdigit():
#                 new_file.write(numbers[int(line[el])])
#             else:
#                 new_file.write(line[el])
#
#     new_file.close()
# ------------------------------------------------------- сделала сначала не то, ну и ладно

numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('5.4.txt', encoding="utf-8") as file:
    new_file = open('5.4.1.txt', 'a', encoding="utf-8")

    for line in file:
        words = line.split(' ')
        new_file.write(f'{numbers[words[0]]} {words[1]} {words[2]}')

        print(words)

    new_file.close()
