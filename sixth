# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. 
# Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит 
# из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()

def big_start(text: str) -> str:
    return text.title()


def my_big_start(text: str) -> str:
    list_of_text = list(text)
    list_of_text[0] = list_of_text[0].upper()
    return ''.join(list_of_text)


str_1 = []
str_2 = []

user_string = input('Введите слова маленькими буквами, разделенные пробелами: ')
if user_string.lower() != user_string:
    print("Ваша строка включает в себя буквы верхнего регистра!")
    exit()
else:
    for el in user_string.split(' '):
        str_1.append(big_start(el))
        str_2.append(my_big_start(el))

print(f'Строка, полученная встроенной функцией: {" ".join(str_1)}')
print(f'Строка, полученная новой функцией: {" ".join(str_2)}')

