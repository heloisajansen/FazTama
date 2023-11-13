import pygame
from sys import exit

class Game:
    def __init__(self):
        pygame.init()

        self.screenInfo = pygame.display.Info()
        self.screenWidth = self.screenInfo.current_w
        self.screenHeight = self.screenInfo.current_h
        self.displayScreen = pygame.display.set_mode((self.screenWidth, self.screenHeight), pygame.FULLSCREEN)

        pygame.display.set_caption("FazTama: Golden guardian")

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
            pygame.display.update()
            self.clock.tick(60)

