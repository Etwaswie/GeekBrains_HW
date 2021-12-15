# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для
# каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести словарь на экран.

with open('5.6.txt', encoding='utf-8') as file:

    for line in file:
        subj = line.split(' ')
        # print(subj)
        sum = 0
        hours = ''
        my_dict = {}

        for el in range(1, len(subj)):
            hours = (''.join([symbol for symbol in subj[el] if symbol.isdigit()]))

            try:
                int(hours)
                sum += int(hours)
            except ValueError:
                pass

            my_dict[subj[0]] = sum

        print(my_dict)
