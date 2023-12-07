import pygame

class HappyBar:
    def __init__(self, x, y, widht, height, maxHp):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        self.hp = maxHp
        self.maxHp = maxHp
        self.startTime = pygame.time.get_ticks()

        self.feedingButton = pygame.image.load("Resources/pizzaButton.png")
        self.cuddlingButton = pygame.image.load("Resources/cuddleButton.png")
        self.feedingButtonRect = self.feedingButton.get_rect()
        self.cuddlingButtonRect = self.cuddlingButton.get_rect()
        self.feedingButtonRect.x, self.feedingButtonRect.y = self.x - 500, self.y
        self.cuddlingButtonRect.x, self.cuddlingButtonRect.y = self.x + 530, self.y
    def drawButtons(self, displayScreen):
        self.displayScreen = displayScreen
        self.displayScreen.blit(self.feedingButton, self.feedingButtonRect)
        self.displayScreen.blit(self.cuddlingButton, self.cuddlingButtonRect)
    def updateBar(self):
        self.currentTime = pygame.time.get_ticks()
        self.mousePos = pygame.mouse.get_pos()
        if self.currentTime > self.startTime + 600:
            self.hp -= 1
            self.startTime = self.currentTime
        if pygame.mouse.get_pressed()[0]:
            if (self.feedingButtonRect.collidepoint(self.mousePos) or self.cuddlingButtonRect.collidepoint(self.mousePos)) and self.hp < 100:
                self.hp += 1
    def drawBar(self, displayScreen):
        self.displayScreen = displayScreen
        ratio = self.hp / self.maxHp
        pygame.draw.rect(self.displayScreen, "#BE5555", (self.x, self.y, self.widht, self.height))
        pygame.draw.rect(self.displayScreen, "#A1BE55", (self.x, self.y, self.widht, self.height * ratio))





