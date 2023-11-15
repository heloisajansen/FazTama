import pygame

class Stage:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

    def run(self):
        self.displayScreen.fill("blue")

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
