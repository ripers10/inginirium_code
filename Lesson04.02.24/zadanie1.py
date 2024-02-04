class car:
    def __init__(self, color, mark, max_speed, weight):
        self.color = color
        self.mark = mark
        self.max_speed = max_speed
        self.weight = weight

    def sound(self):
        print('beep')

    def long_sound(self):
        print('beep-beep')

Lada = car('red', 'granta', '350', '1200')
print(Lada.color)
print(Lada.mark)
print(Lada.max_speed)
print(Lada.weight)

Lada = car('black', 'samara' , '250', '2500')
print(Lada.color)
print(Lada.mark)
print(Lada.max_speed)
print(Lada.weight)

Lada.sound()
Lada.long_sound()
