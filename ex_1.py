import time

class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        i = 1
        while True:
            if i == 1:
                print(self.__color[0])
                i += 1
                time.sleep(7)
            elif i == 2:
                print(self.__color[1])
                i += 1
                time.sleep(2)
            elif i == 3:
                print(self.__color[2])
                i = 1
                time.sleep(8)

tr_light = TrafficLight()
tr_light.running()
