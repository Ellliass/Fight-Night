import pygame

#def class

class Projectile(pygame.sprite.Sprite):

    #def class
    def __init__(self, player):
        super().__init__()
        self.velocity = 15
        self.player = player
        self.image = pygame.image.load("image/proj.png")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 180
        self.rect.y = player.rect.y + 150
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner projectile
        self.angle += -4
        self.image = pygame.transform.rotozoom(self.origin_image,
                                               self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    # supp project non ecran
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()


    # verif si touche pas monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supp project
            self.remove()
            monster.damage(self.player.attack)

        #verifie si project pas ecran
        if self.rect.x > 1170:
            self.remove()