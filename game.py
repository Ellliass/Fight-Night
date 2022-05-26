import pygame


from commet_event import CometFallEvent

from player import Player
from monsters import Monster
from anime import Wait

#crée 2eme classe joueur
class Game:

    def __init__(self):
        #def si jeux commencer ou non
        self.is_playing = False
        #generer joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.anima = Wait(self)
        self.all_players.add(self.player)
        #genere evenemnt
        self.comet_event = CometFallEvent(self)
        #groupe monstre
        self.all_monsters = pygame.sprite.Group()
        #mettre score 0
        #text
        self.font = pygame.font.Font("image/my_custom_font.ttf", 25)
        self.score = 0
        self.pressed = {}
    def start(self):
        self.is_playing = True
        self.spawn_monster()
    def game_over(self):
        # remmetre jeux 0
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
    def update(self, screen):
        #aficher score
        score_text = self.font.render(f"Score : {self.score}", 1, (211, 0, 172))
        screen.blit(score_text, (20, 20))
        # appliquer image joueur
        screen.blit(self.player.image, self.player.rect)
        # actualiser la bar joueur
        self.player.update_health_bar(screen)
        #old_score_text = self.font.render(f"Old_Score: {data_stock_info_player.scoredata.dict1}", 1, (20, 20, 20))
        #screen.blit(old_score_text, (20, 70))
         #appliquer bar evenement du jeu
        self.comet_event.update_bar(screen)
        # recup project
        for projectile in self.player.all_projectiles:
            projectile.move()
        # recup monstre du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        #recup comet jeux
        for comet in self.comet_event.all_comets:
            comet.fall()
        # appliquer l'esemble des image de projectile
        self.player.all_projectiles.draw(screen)
        # appliquer monstre
        self.all_monsters.draw(screen)
        #applquer comet
        self.comet_event.all_comets.draw(screen)
        # verifie si il veut gache ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 860:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -60:
            self.player.move_left()
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group,
                            False, pygame.sprite.collide_mask)
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        self.all_monsters.add(monster)
        self.all_monsters.add(monster)

