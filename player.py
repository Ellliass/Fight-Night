
import pygame

from projectile import Projectile
#class representer joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 200
        self.max_health = 200
        self.attack = 30
        self.velocity = 9
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("image/perso move.gif")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (280, 350))
        self.rect.x = 300
        self.rect.y = 320
        self.percent = 0
        self.percent_speed = 5
        self.tire = True
        self.hard = 150
        self.medium = 100


    def add_percent(self):
        self.percent += self.percent_speed
        self.is_full_loaded()

    def is_full_loaded(self):
        if self.percent >= 50:
            self.tire = False
            if self.percent >= 100:
                self.test()

    def test(self):
            self.tire = True
            self.percent = 0

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

        else:
            #si vie = 0
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 20, self.rect.y + 0, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 20, self.rect.y + 0, self.health, 7])

    def launch_projectile(self):
            #crée instance projectile
            self.all_projectiles.add(Projectile(self))

    def move_right(self):
        #verif si touche pas monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
