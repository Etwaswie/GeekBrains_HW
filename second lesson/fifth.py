# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
# новый элемент с тем же значением должен разместиться после них

rating = [7, 5, 5, 3, 1]

while 1:
    new_rate = int(input(f'Текущий рейтинг {rating}. Введите число: '))
    if new_rate <= 0:
        print('Это не натуральное число!')

    for el in rating:
        if el > new_rate:
            pass
        else:
            rating.insert(rating.index(el), new_rate)
            break