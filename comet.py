import pygame
import random
# class commet
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #def l'image comette
        self.image = pygame.image.load("image/comet.png")
        self.image = pygame.transform.scale(self.image, (70, 130))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 2)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #verif si comet 0
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            #apparaitre 3 pr monstre
            self.comet_event.game.spawn_monster()


    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur sol
        if self.rect.y >= 700:
            #retirer boul
            self.remove()

            #si ya py de bou de feux
            if len(self.comet_event.all_comets) == 0:
                print('evenement fini')
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
        #verifier boul touch joueur

        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print("toucher")
            #retirer boul
            self.remove()
            #subir degat
            self.comet_event.game.player.damage(20)