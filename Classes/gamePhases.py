import pygame
from Classes.FazBear import FazBearCharacter

class Stage:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

        self.borderImage = pygame.image.load("Resources/border.png")
        self.borderResized = pygame.transform.scale(self.borderImage, (800,800))
        self.filling = pygame.Surface((590,600))
        self.filling.fill("#6B6B6B")

        self.background = pygame.image.load("Resources/bg.png")
        self.backgroundResized = pygame.transform.scale(self.background, (594,800))

        self.FazBearCharacter = FazBearCharacter
        self.normalFreddy = pygame.image.load("Resources/freddySprite01.png")
        self.leftFreddy = pygame.image.load("Resources/freddySprite02.png")
        self.rightFreddy = pygame.image.load("Resources/freddySprite03.png")
        self.characterPos = pygame.math.Vector2(400, 300)

    def run(self):
        self.displayScreen.fill("#B1B1B1")
        self.displayScreen.blit(self.borderResized,(300,0))
        self.displayScreen.blit(self.filling, (400,100))
        self.displayScreen.blit(self.backgroundResized, (400,-100))

        self.mousePos = pygame.mouse.get_pos()
        self.FazBearCharacter.updateCharacter(self, self.mousePos)
        self.FazBearCharacter.drawingSprites(self)

class StartMenu:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

        self.logoImage = pygame.image.load("Resources/menuScreen01.png")
        self.logoResized = pygame.transform.scale(self.logoImage,(500, 800))

        self.gameFont = pygame.font.Font("Resources/font.ttf", 45)
        self.textSurfaceEnter = self.gameFont.render("Pressione X para iniciar", False, "#BE5555")
        self.textSurfaceQuit = self.gameFont.render("Pressione ESC para sair", False, "#BE5555")

    def run(self):
        self.displayScreen.fill("white")
        self.displayScreen.blit(self.logoResized, (450,0))
        self.displayScreen.blit(self.textSurfaceEnter, (390,600))
        self.displayScreen.blit(self.textSurfaceQuit, (400, 650))
class StageManager:
    def __init__(self, currentStage):
        self.currentStage = currentStage
    def getStage(self):
        return self.currentStage
    def setStage(self, stage):
        self.currentStage = stage
