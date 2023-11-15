import pygame

class Button:
    def __init__(self, text, x, y, width, height, displayScreen):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.draw()
        self.font = pygame.font.Font("Resources/font.ttf", 18)
        self.displayScreen = displayScreen

    def draw(self):
        buttonText = self.font.render(self.text, True, "black")
        buttonRect = pygame.rect.Rect((self.x, self.y), (self.width, self.height))
        pygame.draw.rect(self.displayScreen, "red", buttonRect, 0, 5)
        self.displayScreen.blit(buttonText, (self.x + 16, self.y + 5))