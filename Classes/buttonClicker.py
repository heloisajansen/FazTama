import pygame

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.draw()

    def draw(self):
        buttonText = font.render(self.text, True, "black")
        buttonRect = pygame.rect.Rect((self.x, self.y), (self.width, self.height))
        pygame.draw.rect(displayScreen, "red", buttonRect, 0, 5)
        displayScreen.blit(buttonText, (self.x + 16, self.y + 5))