import pygame

class Stage:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

        self.borderImage = pygame.image.load("Resources/border.png")
        self.borderResized = pygame.transform.scale(self.borderImage, (800,800))
        self.filling = pygame.Surface((590,600))
        self.filling.fill("#6B6B6B")

    def run(self):
        self.displayScreen.fill("#B1B1B1")
        self.displayScreen.blit(self.borderResized,(300,0))
        self.displayScreen.blit(self.filling, (400,100))
class StartMenu:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

        self.logoImage = pygame.image.load("Resources/menuScreen01.png")
        self.logoResized = pygame.transform.scale(self.logoImage,(500, 800))
        self.startImage = pygame.image.load("Resources/menuScreen02.png")
        self.startResized = pygame.transform.scale(self.startImage,(350, 250))

    def run(self):
        self.displayScreen.fill("white")
        self.displayScreen.blit(self.logoResized, (450,0))
        self.displayScreen.blit(self.startResized, (520, 550))

class StageManager:
    def __init__(self, currentStage):
        self.currentStage = currentStage
    def getStage(self):
        return self.currentStage
    def setStage(self, stage):
        self.currentStage = stage
