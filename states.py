from constants import keyTemp, keyHum, keyEmp, TemperatureRange, HumidityRange, EmptinessRange


class State:
    # определение служебных функций для состояния

    def __init__(self):
        # Выполнение текущего состояния
        pass

    def on_event(self, event):
        # Обработка событий которые делигированны этому состоянию
        pass

    def __repr__(self):
        # Модуль представления состояния
        return self.__str__()

    def __str__(self):
        # Возврат имени состояния
        return self.__class__.__name__


class TemperatureState(State):  # Состояние температуры
    def on_event(self, value):
        try:
            int(value)
        except ValueError:
            return ErrorState()
        if int(value) in TemperatureRange:
            return PosState()
        else:
            return NegState()


class HumidityState(State):  # Состояние влажности
    def on_event(self, value):
        try:
            int(value)
        except ValueError:
            return ErrorState()
        if int(value) in HumidityRange:
            return PosState()
        else:
            return NegState()


class EmptinessState(State):   # Состояние заполненности резервуара
    def on_event(self, value):
        try:
            int(value)
        except ValueError:
            return ErrorState()
        if int(value) in EmptinessRange:
            return PosState()
        else:
            return NegState()


eventNames = {  # Словарь с возможными входными состояниями
    keyTemp: TemperatureState(),
    keyHum: HumidityState(),
    keyEmp: EmptinessState()
}


class NegState(State):
    def on_event(self, event):
        if event in eventNames:
            return eventNames[event]
        return self


class PosState(State):
    def on_event(self, event):
        if event in eventNames:
            return eventNames[event]
        return self


class ErrorState(State):
    def on_event(self, event):
        if event in eventNames:
            return eventNames[event]
        return self



