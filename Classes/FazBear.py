import pygame
class FazBearCharacter(pygame.sprite.Sprite):
    def __init__(self, displayScreen):
        self.displayScreen = displayScreen
        self.characterImage = self.normalFreddy

    def updateCharacter(self, mousePos):
        eyeAngle = pygame.math.Vector2(mousePos[0] - self.characterPos.x, mousePos[1] - self.characterPos.y).angle_to((1,0))
        if -45 <= eyeAngle <= 45:
            self.characterImage = self.rightFreddy
        elif 135 < eyeAngle <= 225:
            self.characterImage = self.leftFreddy
        else:
            self.characterImage = self.normalFreddy

    def drawingSprites(self):
        self.displayScreen.blit(self.characterImage, (450,100))

    def runningFreddy(self):
        allSprites = pygame.sprite.Group()
        allSprites.add(self)