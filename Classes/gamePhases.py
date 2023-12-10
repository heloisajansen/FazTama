import pygame
from Classes.FazBear import FazBearCharacter
from Classes.happinessBar import HappyBar


class Stage:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

        self.borderImage = pygame.image.load("Resources/border.png")
        self.borderResized = pygame.transform.scale(self.borderImage, (800, 800))
        self.filling = pygame.Surface((590, 600))
        self.filling.fill("#6B6B6B")

        self.blockImage = pygame.image.load("Resources/whiteBlock.png")
        self.blockImageResized = pygame.transform.scale(self.blockImage, (550, 200))

        self.background = pygame.image.load("Resources/bg.png")
        self.backgroundResized = pygame.transform.scale(self.background, (594, 800))

        self.FazBearCharacter = FazBearCharacter
        self.normalFreddy = pygame.image.load("Resources/freddySprite01.png")
        self.leftFreddy = pygame.image.load("Resources/freddySprite02.png")
        self.rightFreddy = pygame.image.load("Resources/freddySprite03.png")
        self.characterPos = pygame.math.Vector2(400, 300)

        self.HappyBarOnScreen = HappyBar(430, 180, 40, 300, 100)

        self.gameFont = pygame.font.Font("Resources/font.ttf", 38)
        self.textSurfaceGoToMenu = self.gameFont.render("Aperte E para pausar", False, "Black")

    def run(self):
        self.displayScreen.fill("gray")
        self.displayScreen.blit(self.borderResized, (300, 0))
        self.displayScreen.blit(self.filling, (400, 100))
        self.displayScreen.blit(self.backgroundResized, (400, -100))
        self.displayScreen.blit(self.blockImageResized, (440, 25))

        self.mousePos = pygame.mouse.get_pos()
        self.FazBearCharacter.updateCharacter(self, self.mousePos)
        self.FazBearCharacter.drawingSprites(self)

        self.HappyBarOnScreen.updateBar()
        self.HappyBarOnScreen.drawBar(self.displayScreen)

        self.HappyBarOnScreen.drawButtons(self.displayScreen)

        self.displayScreen.blit(self.textSurfaceGoToMenu, (485, 120))


class StartMenu:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

        self.logoImage = pygame.image.load("Resources/menuScreen01.png")
        self.logoResized = pygame.transform.scale(self.logoImage, (500, 800))

        self.gameFont = pygame.font.Font("Resources/font.ttf", 45)
        self.color = "#BE5555"
        self.textSurfaceEnter = self.gameFont.render("Pressione X para iniciar", False, self.color)
        self.textSurfaceQuit = self.gameFont.render("Pressione ESC para sair", False, self.color)

    def run(self):
        self.displayScreen.fill("white")
        self.displayScreen.blit(self.logoResized, (450, 0))
        self.displayScreen.blit(self.textSurfaceEnter, (390, 600))
        self.displayScreen.blit(self.textSurfaceQuit, (400, 650))

class PauseMenu:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

        self.color = "#BE5555"
        self.gameFont = pygame.font.Font("Resources/font.ttf", 45)
        self.textSurfaceGoBack = self.gameFont.render("Pressione X para voltar", False, self.color)
        self.textSurfaceGoBackMain = self.gameFont.render("Pressione Q para voltar para o menu incial", False, self.color)
        self.textSurfaceGoToCredits = self.gameFont.render("Pressione C para ir para os créditos", False, self.color)
    def run(self):
        self.displayScreen.fill("white")
        self.displayScreen.blit(self.textSurfaceGoBack, (390, 330))
        self.displayScreen.blit(self.textSurfaceGoBackMain, (150, 450))
        self.displayScreen.blit(self.textSurfaceGoToCredits, (190, 570))

class StageCredits:
    def __init__(self, displayScreen, stageManager):
        self.displayScreen = displayScreen
        self.stageManager = stageManager

        self.gameFont = pygame.font.Font("Resources/font.ttf", 45)
        self.color = "#BE5555"
        self.textSurfaceCredits = self.gameFont.render("Créditos", False, self.color)
        self.textSurfaceLine01 = self.gameFont.render("Obra inspirada na franquia FNAF", False, self.color)
        self.textSurfaceLine02 = self.gameFont.render("Música feita por The Living Tombstone e Z3r0", False, self.color)
        self.textSurfaceLine03 = self.gameFont.render("Arte criada por Heloísa Jansen", False, self.color)
        self.textSurfaceLine04 = self.gameFont.render("Pressione E para voltar", False, self.color)
        self.textSurfaceLine05 = self.gameFont.render("'Totus Tuus Maria'", False, self.color)

    def run(self):
        self.displayScreen.fill("gray")
        self.displayScreen.blit(self.textSurfaceCredits, (570, 0))
        self.displayScreen.blit(self.textSurfaceLine01, (280, 100))
        self.displayScreen.blit(self.textSurfaceLine02, (100, 200))
        self.displayScreen.blit(self.textSurfaceLine03, (290, 300))
        self.displayScreen.blit(self.textSurfaceLine04, (390, 650))
        self.displayScreen.blit(self.textSurfaceLine05, (460, 400))


class StageManager:
    def __init__(self, currentStage):
        self.currentStage = currentStage

    def getStage(self):
        return self.currentStage

    def setStage(self, stage):
        self.currentStage = stage
