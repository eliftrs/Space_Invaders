class Player:
    def __init__(self):
        self.health = 3
        self.name = "Oyuncu1"
    
    def hit(self):
        self.health -= 1
        print(f"{self.name} vuruldu! Kalan can: {self.health}")

# test
p = Player()
p.hit()
