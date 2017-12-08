from class1 import Sensor
import random
import threading

def printer(Sensor, event):
    event.set() # установка флажка потоком, т.к. у нас всего один поток, то сброс флажка можно опустить
    output = Sensor.generate_data().copy() # принимаем показания датчика в словарь output
    for item in output: # цикл вывода всех снятых показаний датчика
        print("Температура: {}".format(output[item]))


def main():
    min1 = random.randint(0, 10) # задание минимального значения диапазона
    max1 = random.randint(20, 30) # задание максимального значения диапазона
    range1 = {"min": min1,
             "max": max1}

    sensor1 = Sensor("sensor1", 3, range1)

    e1 = threading.Event()
    t1 = threading.Thread(target=printer, args=(sensor1, e1))
    t1.start()
    t1.join()

if __name__ == "__main__":
    main()

