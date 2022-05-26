import pygame

class Wait():
    def __init__(self, game):
        self.game = game
        self.percent = 0
        self.percent_speed = 1
        self.anima = False

    def add_percent(self):
        self.percent += self.percent_speed
        self.is_start_loaded()

    def is_start_loaded(self):
        if self.percent <= 40:
            self.anima = True
        elif\
            self.percent >= 100:

            self.anima = False
            self.percent = 0
            self.game.player.image = pygame.image.load("image/perso move.gif")
            self.game.player.image = pygame.transform.scale(self.game.player.image, (280, 350))




