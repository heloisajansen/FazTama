import pygame
from Classes.gamePhases import StageManager, StartMenu, Stage, PauseMenu
from sys import exit

class Game:
    def __init__(self):
        pygame.init()

        self.screenInfo = pygame.display.Info()
        self.displayScreen = pygame.display.set_mode((self.screenInfo.current_w, self.screenInfo.current_h))

        pygame.display.set_caption("FazTama: Golden guardian")

        self.clock = pygame.time.Clock()

        self.stageManager = StageManager("StartMenu")
        self.startMenu = StartMenu(self.displayScreen, self.stageManager)
        self.stage = Stage(self.displayScreen, self.stageManager)
        self.pause = PauseMenu(self.displayScreen, self.stageManager)

        self.stages = {"StartMenu": self.startMenu, "Stage": self.stage, "PauseMenu": self.pause}

        self.titleMusic = pygame.mixer.Sound("Resources/8bitSyndrome.mp3")
        self.titleMusic.set_volume(0.25)
        self.stageMusic = pygame.mixer.Sound("Resources/justGold.mp3")
        self.stageMusic.set_volume(0.25)

    def mixMusic(self):
        if self.stageManager.getStage() == "StartMenu":
            self.titleMusic.play(loops=-1)
        elif self.stageManager.getStage() == "Stage":
            self.titleMusic.stop()
            self.stageMusic.play(loops=-1)
        else:
            self.stageMusic.stop()
            self.titleMusic.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    self.stageManager.setStage("Stage")
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e and self.stageManager.getStage() == "Stage":
                    self.stageManager.setStage("PauseMenu")
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q and self.stageManager.getStage() == "PauseMenu":
                    self.stageManager.setStage("StartMenu")
            self.stages[self.stageManager.getStage()].run()
            pygame.display.update()
            self.clock.tick(60)
            self.mixMusic()
