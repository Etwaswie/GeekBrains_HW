# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file = open('text 5.2', 'r')
strings = file.readlines()
number_of_string = 0

print(f'В файле {len(strings)} строк.')

for string in strings:
    counter = 0
    number_of_string += 1
    words = string.split(' ')

    for el in range(len(words)):
        if words[el] != '' and words[el] != '\n':
            counter += 1

    print(f'Количество слов в строке №{number_of_string}: {counter} .')



