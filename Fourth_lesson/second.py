# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.

source_list = input("Введите числа через пробел: ").split()

new_list = [source_list[i] for i in range(1, len(source_list)) if source_list[i] > source_list[i - 1]]

print(new_list)

