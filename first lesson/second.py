# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

hours_str = 'часам'
minutes_str = 'минутам'
seconds_str = 'секундам'

time_in_seconds = int(input('Введите время в секундах: '))

hours = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
seconds = (time_in_seconds % 3600) % 60

if hours % 10 == 1:
    hours_str = 'часу'

if minutes % 10 == 1:
    minutes_str = 'минуте'

if seconds % 10 == 1:
    seconds_str = 'секунде'

print(f"Указанное время эквивалентно {hours} {hours_str}, {minutes} {minutes_str} и {seconds} {seconds_str}")
