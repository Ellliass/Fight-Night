import pygame
from anime import Wait
from comet import Comet

#cree class evenement
class CometFallEvent:
    #los du chargement -> crée conteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 4
        self.game = game
        self.fall_mode = False

        #def un groupe de sprite pour comet
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #boucme
        for i in range(1, 5):
        #apparaitre 1 boule
            self.all_comets.add(Comet(self))
            self.all_comets.add(Comet(self))


    def attempt_fall(self):
        #jauge charger
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True #activer l'evenement



    def update_bar(self, surface):

        #ajouter pourcentafe a la bar
        self.add_percent()
        self.game.player.add_percent()
        self.game.anima.add_percent()


        #bar noir arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #l'axe des x
            surface.get_height() - 20, #l'axe des y
            surface.get_width(), #longueur de fenetre
            10 #epesseur
        ])
        #bar violet (jauge avant)
        pygame.draw.rect(surface, (128, 0, 128), [
            0,  # l'axe des x
            surface.get_height() - 20,  #l'axe des y
            (surface.get_width() / 100) * self.percent,  #longueur de fenetre
            10  #epesseur
        ])
