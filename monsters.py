import pygame
import random
import ast
#cree une classe monstre
import pygame.sysfont


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.2
        self.image = pygame.image.load("image/monst.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect.x = 1000 + random.randint(0, 500)
        self.rect.y = 400
        self.velocity = 2 + random.randint(0, 2)



    def damage(self, amount):
        #inflige degat
        self.health -= amount

        #verifie si vie est inferieur a 0
        if self.health <= 0:
            #supp monstre
            self.rect.x = 1200 + random.randint(0, 300)
            self.health = self.max_health
            #ajouter point
            self.game.score += 1


            #si la bar devenement est charger au max
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

        #pluie
        self.game.comet_event.attempt_fall()


    def update_health_bar(self, surface):
         # dessiner bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y + -5, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y + -5, self.health, 5])



    def forward(self):
        #le deplacement ce fait que si touche pas joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            #si monstre touche joeueur
        else:
            #degat pr joeur
            self.game.player.damage(self.attack)




