# 6.Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

goods = []
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'ед': []}
i = 1

while 1:
    print('-----------МЕНЮ-----------')
    print('1. Добавить товар')
    print('2. Посмотреть все товары')
    print('3. Выйти')
    print('4. Сбор аналитики')
    print('--------------------------')
    choice = int(input('Введите команду: '))

    if choice == 1:
        specifications = {
            'Название': input('Введите название товара: '),
            'Цена': input('Введите цену товара: '),
            'Количество': input('Введите количество товара: '),
            'ед': input('Введите единицы измерения: ')
        }
        goods.append(tuple([i, specifications]))

        # user_tuple.append(specifications)
        # print(user_tuple)
        # print(goods)
        # goods.append(tuple(user_tuple))
        # print(goods)
        i += 1

        analytics['Название'].append(specifications['Название'])
        analytics['Цена'].append(specifications['Цена'])
        analytics['Количество'].append(specifications['Количество'])
        analytics['ед'].append(specifications['ед'])

    if choice == 2:
        for good in goods:
            print(good)

    if choice == 3:
        break

    if choice == 4:
        print(analytics)


