from states import PosState, eventNames


class StateMachine:

    def __init__(self):
        # Обозначаем PosState стартовым состоянием по умолчанию
        self.state = PosState()

    def set_start(self, event):
        # Передача иного стартового состояния
        if event in eventNames:
            self.state = eventNames[event]

    def on_event(self, event):
        # Входящие события передаются в состояния, которые потом их обрабатывают
        # результатом является новое состояние
        self.state = self.state.on_event(event)

    def run_all(self, events):
        # Передача списка событий
        for i in events:
            self.state = self.state.on_event(i)



