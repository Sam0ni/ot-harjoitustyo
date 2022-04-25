import pygame

class Menu:
    def __init__(self, dispx, dispy):
        pygame.font.init()
        self.cursor = 1
        self.start_color = (255,0,0)
        self.scores_color = (0,0,255)
        self.quit_color = (0,0,255)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.displaywidth = dispx
        self.displayheight = dispy
        self.starttext = ""
        self.scorestext = ""
        self.quittext = ""
        self.initfonts()

    def initfonts(self):
        self.starttext = self.font.render("Start", True, self.start_color)
        self.scorestext = self.font.render("Scores", True, self.scores_color)
        self.quittext = self.font.render("Quit", True, self.quit_color)

    def move_cursor_up(self):
        if self.cursor == 1:
            self.cursor = 3
            self.start_color = (0,0,255)
            self.quit_color = (255,0,0)
        elif self.cursor == 2:
            self.cursor = 1
            self.scores_color = (0,0,255)
            self.start_color = (255,0,0)
        else:
            self.cursor = 2
            self.quit_color = (0,0,255)
            self.scores_color = (255,0,0)
        self.initfonts()
    
    def move_cursor_down(self):
        if self.cursor == 1:
            self.cursor = 2
            self.start_color = (0,0,255)
            self.scores_color = (255,0,0)
        elif self.cursor == 2:
            self.cursor = 3
            self.scores_color = (0,0,255)
            self.quit_color = (255,0,0)
        else:
            self.cursor = 1
            self.quit_color = (0,0,255)
            self.start_color = (255,0,0)
        self.initfonts()

    def go(self):
        if self.cursor == 1:
            return True
        elif self.cursor == 3:
            return False
        else:
            return "highscores"