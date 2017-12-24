# Файл с константами
class Consts:
    # Строковые константы
    keyTemp, keyHum, keyEmp = "Temperature", "Humidity", "Emptiness"
    # Списки оптимальных значений
    TemperatureRange = list(range(16, 35))
    HumidityRange = list(range(50, 101))
    EmptinessRange = list(range(50, 101))

    # Убираем возможность изменения констант
    def __setattr__(self, *_):
        pass

