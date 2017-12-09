def start_transitions(txt):     # функция, реализующая переходы из начального состояния
    splitted_txt = txt.split(" ", 1)    # разбиение строки на список из первого слова и оставшейся части
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")    # присваиваем переменным элементы списка
    # если в списке больше 1 элемента, иначе word = txt, а txt = ''
    if word == "Temperature":   # анализируем какое состояние будет следующим
        newState = "temperature_state"
    elif word == "Humidity":
        newState = "humidity_state"
    elif word == "Empty":
        newState = "is_empty_state"
    else:
        newState = "error_state"
    return (newState, txt)


def temperature_state_transitions(txt):     # функция, реализующая переходы из состояния обработки температуры
    splitted_txt = txt.split(" ", 1)        # далее аналогично предыдущей функции
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    digit = int(word)
    if digit >= 26:
        newState = "neg_state"
    elif digit in range(0, 26):
        newState = "pos_state"
    else:
        newState = "error_state"
    return (newState, txt)


def humidity_state_transitions(txt):
    splitted_txt = txt.split(" ", 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    digit = int(word)
    if digit < 50:
        newState = "neg_state"
    elif digit in range(50, 100):
        newState = "pos_state"
    else:
        newState = "error_state"
    return (newState, txt)


def is_empty_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    digit = int(word)
    if digit < 20:
        newState = "neg_state"
    elif digit in range(20, 100):
        newState = "pos_state"
    else:
        newState = "error_state"
    return (newState, txt)
