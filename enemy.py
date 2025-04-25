class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += 1
class Alien:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name} saldırıyor!")
