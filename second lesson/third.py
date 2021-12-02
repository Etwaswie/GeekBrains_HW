# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
seasons_list = ['зиму', 'весну', 'лето', 'осень']

month = int(input('Введите номер месяца: '))

if month in [12, 1, 2]:
    print(f'{seasons_dict[1]}! Я тоже люблю {seasons_list[0]}.')
elif month in [3, 4, 5]:
    print(f'{seasons_dict[2]}! Я тоже люблю {seasons_list[1]}.')
elif month in [6, 7, 8]:
    print(f'{seasons_dict[3]}! Я тоже люблю {seasons_list[2]}.')
elif month in [9, 10, 11]:
    print(f'{seasons_dict[4]}! Я тоже люблю {seasons_list[3]}.')
else: print("Ой, я не знаю такого месяца!")
    
