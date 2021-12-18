# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
# реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
from time import sleep


class TrafficLight:
    traffic_light_color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        for i in range(0,3):
            if i == 0:
                print(TrafficLight.traffic_light_color[i])
                sleep(7)
            elif i == 1:
                print(TrafficLight.traffic_light_color[i])
                sleep(2)
            else:
                print(TrafficLight.traffic_light_color[i])
                sleep(6)

my_traffic_light = TrafficLight()
my_traffic_light.running()
