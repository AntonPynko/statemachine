from time import sleep
import random
class Sensor:


    def __init__(self, name, time, range):
        self.__name = name  # устанавливаем название сенсора
        self.__time = time  # -//- время работы сенсора
        self.__range = range    # -//- диапазон значений



    def generate_data(self):
        output_values = dict() # словарь для сохранения показаний датчика
        i = 0 # первый ключ для словаря
        while self.__time > 0: # пока время не истекло, снимаем показания датчика
            output_values[i] = random.randint(self.__range["min"], self.__range["max"]) # запись в словарь рандомного значения от min до max
            self.__time -= 1 # фиксируем прошествие секунды
            i += 1 # задаем новый ключ для следующего показания датчика
            sleep(1) # остановка работы цикла на 1 секунду
        return(output_values) # выдача словаря с показаниями датчика










