from statemachine import StateMachine

if __name__ == "__main__":
    device = StateMachine()
    #device.set_start('Temperature')
    #print(device.state)
    device.on_event('Humidity')  # Подача состояний по одному
    device.on_event('100')
    print(device.state)
    device.on_event('Temperature')
    device.on_event('30')
    print(device.state)
    device.on_event('Emptiness')
    device.on_event('30')
    print(device.state)
    events = ('Temperature', '30')   # Передача кортежа (или списка) из состояний
    device.run_all(events)
    print(device.state)





