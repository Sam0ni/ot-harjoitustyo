import pygame
from database_connection import get_database_connection
from scores.scores import Scores

class Menu:
    """This class compiles all the assets for the menu, and has functions for them.
    """
    def __init__(self):
        """class constructor which creates the menu
        """
        pygame.font.init()
        self.cursor = 1
        self.start_color = (255,0,0)
        self.scores_color = (0,0,255)
        self.quit_color = (0,0,255)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.starttext = ""
        self.scorestext = ""
        self.quittext = ""
        self.initfonts()
        self.scores = Scores(get_database_connection())

    def initfonts(self):
        """initializes the texts
        """
        self.starttext = self.font.render("Start", True, self.start_color)
        self.scorestext = self.font.render("Scores", True, self.scores_color)
        self.quittext = self.font.render("Quit", True, self.quit_color)

    def move_cursor_up(self):
        """Changes the highlighted text to the next and changes the current highlighted text back to normal
        """
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
        """Changes the highlighted text to the next and changes the current highlighted text back to normal
        """
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

    def go_there(self):
        """Selects the highlighted option

        Returns:
            True: if start is highlighted
            False: if quit is highlighted
            "highscores": if highscores is highlighted
        """
        if self.cursor == 1:
            return True
        elif self.cursor == 3:
            return False
        else:
            return "highscores"

    def inithighscores(self):
        """Fetches 10 best scores

        Returns:
            List: returns a list of tuples which scontain playername and score
        """
        highscores = self.scores.get_highscores()
        return highscores
