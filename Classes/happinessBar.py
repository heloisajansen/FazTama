import pygame

class HappyBar():
    def __init__(self, x, y, widht, height, maxHp):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        self.hp = maxHp
        self.maxHp = maxHp

    def drawBar(self, displayScreen):
        self.displayScreen = displayScreen
        ratio = self.hp / self.maxHp
        pygame.draw.rect(self.displayScreen, "#BE5555", (self.x, self.y, self.widht, self.height))
        pygame.draw.rect(self.displayScreen, "#A1BE55", (self.x, self.y, self.widht, self.height))
