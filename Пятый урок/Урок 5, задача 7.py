# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json

with open('5.7.txt', encoding='utf-8') as file:

    sum_profit = 0
    firms = {}
    avg_profit = {}
    count = 0
    list = []

    for line in file:
        count += 1
        data = line.split(' ')
        profit = int(data[2]) - int(data[3])
        if profit >= 0:
            sum_profit += profit

        firms[data[0]] = profit
    avg_profit['average_profit'] = round(sum_profit / count)

    list.append(firms)
    list.append(avg_profit)

    print(list)

with open('5.7.json', 'w+') as file_1:
    json.dump(list, file_1)