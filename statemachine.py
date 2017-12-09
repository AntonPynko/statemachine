class StateMachine:
    def __init__(self):
        self.handlers = {}  # множество обработчиков
        self.startState = None  # начальное состояние
        self.endStates = []  # список конечных состояний

    def add_state(self, name, handler, end_state=0):  # функция добавления состояния
        name = name.upper()     # сохранения имени состояния в верхнем регистре в переменную name
        self.handlers[name] = handler   # добавляем принятый обработчик в множество обработчиков
        if end_state:   # если end_state задан не нулем, то добавляем конечное состояние в список конечных состояний
            self.endStates.append(name)

    def set_start(self, name):      # указываем стартовое состояние
        self.startState = name.upper()

    def run(self, cargo):   # запускаем конечный автомат с принятой на обработку строкой
        try:    # первым должен выполнятся обработчик стартового состояния, если оно не задано, возвращаем ошибку
            handler = self.handlers[self.startState]
        except Exception:
            exception_meaning = "must call .set_start() before .run()"
            return exception_meaning
        if not self.endStates:  # проверка на наличие хотя бы одного конечного состояния
            exception_meaning = "at least one state must be an end_state"
            return exception_meaning
        while True:     # основной цикл конечного автомата
            (newState, cargo) = handler(cargo)  # кортеж из состояния и обрабатываемой строки
                                                # получает результат работы обработчика
            if newState.upper() in self.endStates:  # если полученное состояние находится в списке конечных
                return newState  # возращаем значение этого состояния
            else:   # иначе добавляем это состояние в переменную обработчика
                handler = self.handlers[newState.upper()]
