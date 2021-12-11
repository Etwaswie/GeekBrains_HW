# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
# за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    count = 1
    for el in range(1, n + 1):
        count *= el
    yield count


all_numbers = ''

try:
    number = int(input("Введите число: "))
    for j in range(1, number + 1):
        if j == number:
            all_numbers = all_numbers + str(j)
        else:
            all_numbers = all_numbers + str(j) + ' * '

    for i in fact(number):
        print(f'{number}! = {all_numbers} = {i}')
except ValueError:
    print("Это не число!")
