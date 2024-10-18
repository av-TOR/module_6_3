class Horse:
    def __init__(self, x_distance=0, y_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        get_pos1 = (self.x_distance, self.y_distance)
        return get_pos1

    def voice(self):
        return print(self.sound)


Pegas = Pegasus()

print(Pegas.get_pos())
Pegas.move(7, 45)
print(Pegas.get_pos())
Pegas.move(1, 3)
print(Pegas.get_pos())

Pegas.voice()
