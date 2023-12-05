import pygame
class FazBearCharacter(pygame.sprite.Sprite):
    def __init__(self, displayScreen):
        self.displayScreen = displayScreen
        self.characterPos = pygame.math.Vector2(450,100)
        self.leftFreddy = pygame.image.load("Resources/freddySprite01.png")
        self.rightFreddy = pygame.image.load("Resources/freddySprite02.png")
        self.normalFreddy = pygame.image.load("Resources/freddySprite03.png")

        super().__init__()
        self.characterImage = self.normalFreddy

    def updateCharacter(self, mousePos):
        angle = pygame.math.Vector2(mousePos[0] - self.characterPos.x, mousePos[1] - self.characterPos.y).angle_to((1,0))
        if -45 <= angle <= 45:
            self.characterImage = self.rightFreddy
        elif 135 < angle <= 225:
            self.characterImage = self.leftFreddy
        else:
            self.characterImage = self.normalFreddy

    def drawingSprites(self):
        self.displayScreen.blit(self.characterImage, (450,100))

    def runningFreddy(self):
        allSprites = pygame.sprite.Group()
        allSprites.add(self)