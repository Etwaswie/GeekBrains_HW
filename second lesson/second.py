# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

user_list = []
num = 0

count = int(input('Сколько элементов добавим в список? '))
for i in range(count):
    user_list.append(input(f'Введите элемент № {i + 1}: '))

while num < len(user_list) - 1:
    element = user_list.pop(num)
    user_list.insert(num + 1, element)
    num += 2

print(user_list)

