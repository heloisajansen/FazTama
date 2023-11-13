import pygame
from sys import exit

pygame.init()

screenInfo = pygame.display.Info()
screenWidth = screenInfo.current_w
screenHeight = screenInfo.current_h
displayScreen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)

pygame.display.set_caption("FazTama: Golden guardian")
clock = pygame.time.Clock()

font = pygame.font.Font("Resources/font.ttf", 16)

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 pygame.quit()
                 exit()
    pygame.display.update()
    clock.tick(60)