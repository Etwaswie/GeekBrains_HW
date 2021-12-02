# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите строку из нескольких слов: ')
user_string_split = user_string.split(' ')
if user_string.count(' ') == 0:
    print('В этой строке только одно слово!')
else:
    for el in user_string_split:
        count = user_string_split.index(el) + 1
        if len(el) > 10:
            el = el[:10]
        print(count, el)



