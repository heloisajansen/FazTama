import pygame
from Classes.gamePhases import StageManager, StartMenu, Stage
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

        self.stageManager = StageManager("StartMenu")
        self.startMenu = StartMenu(self.displayScreen, self.stageManager)
        self.stage = Stage(self.displayScreen, self.stageManager)

        self.stages = {"StartMenu": self.startMenu, "Stage": self.stage}

        self.titleMusic = pygame.mixer.Sound("Resources/8bitSyndrome.mp3")
        self.titleMusic.set_volume(0.25)

    def mixMusic(self):
        if self.stageManager.getStage() == "StartMenu":
            self.titleMusic.play(loops=-1)
        elif self.stageManager.getStage() == "Stage":
            self.titleMusic.stop()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    self.stageManager.setStage("Stage")
            self.stages[self.stageManager.getStage()].run()
            pygame.display.update()
            self.clock.tick(60)
            self.mixMusic()
