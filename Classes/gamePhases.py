class Stage:
    def __init__(self, display, stageManager):
        self.display = display
        self.stageManager = stageManager

    def run(self):
        self.display.fill("blue")

class StartMenu:
    def __init__(self, display, stageManager):
        self.display = display
        self.stageManager = stageManager

    def run(self):
        self.display.fill("black")

class StageManager:
    def __init__(self, currentStage):
        self.currentStage = currentStage
    def getStage(self):
        return self.currentStage
    def setStage(self, stage):
        self.currentStage = stage
