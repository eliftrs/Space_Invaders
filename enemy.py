class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += 1
