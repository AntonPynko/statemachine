from statemachine import StateMachine
import random
from methods import start_transitions, temperature_state_transitions, \
                    humidity_state_transitions, is_empty_state_transitions


if __name__ == "__main__":
    m = StateMachine()  # инициализация конечного автомата
    m.add_state("Start", start_transitions)  # добавление состояния и переходов из него
    m.add_state("temperature_state", temperature_state_transitions)  # -//-
    m.add_state("humidity_state", humidity_state_transitions)  # -//-
    m.add_state("is_empty_state", is_empty_state_transitions)  # -//-
    m.add_state("neg_state", None, end_state=1)  # добавление конечного состояния
    m.add_state("pos_state", None, end_state=1)  # -//-
    m.add_state("error_state", None, end_state=1)  # -//-
    m.set_start("Start")    # инициализация начального состояния

    temperature = str(random.randint(16, 45))  # задание случайного значения температуры
    state = m.run("Temperature {}".format(temperature))  # получение и запись состояния температуры
    if state == "neg_state":  # вывод на экран необходимых действий по приведению текущего состояния в норму
        print("Turn on air conditioners")
    elif state == "error_state":
        print("Control system received wrong command")
    else:
        print("Temperature is good")

    humidity = str(random.randint(0, 100))  # аналогично предыдущему блоку
    state = m.run("Humidity {}".format(humidity))
    if state == "neg_state":
        print("Turn on irrigation system")
    elif state == "error_state":
        print("Control system received wrong command")
    else:
        print("Humidity is good")

    filling = str(random.randint(0, 100))   # аналогично блоку команд с температурой
    state = m.run("Empty {}".format(filling))
    if state == "neg_state":
        print("Turn on water supply system")
    elif state == "error_state":
        print("Control system received wrong command")
    else:
        print("No need to fill tank")

