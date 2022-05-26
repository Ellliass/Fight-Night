import pygame
import math

import Enrengistreur_donner
import Nickname
import user_data.namedata
from user_data import scoredata
from game import Game

pygame.init()
#def clock
clock = pygame.time.Clock()
FPS = 70

#fenetre gen
pygame.display.set_caption("Night Fight")
gameIcon = pygame.image.load('image/proj.png')
pygame.display.set_icon(gameIcon)
screencode = (1165, 670)
screen = pygame.display.set_mode(screencode)

#charger image fond
background = pygame.image.load("image/fond game.jpg")

#importe bienvenue
banner = pygame.image.load("image/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.6)
banner_rect.y = math.ceil(screen.get_height()/50)

play_button = pygame.image.load("image/start_button.png")
play_button = pygame.transform.scale(play_button, (400, 180))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.2)
play_button_rect.y = math.ceil(screen.get_height()/ 1.9)
Nickname.MyWindow
#charger jeu
game = Game()
screen = pygame.display.set_mode(screencode)
running = True
#boucle tant condition vraie
while running:
    # appliquer un fond a l'image
    screen.blit(background, (0, 2))
    pseudo = user_data.namedata.dict1
    #verif si le jeux commence ou non
    if game.is_playing:
        #declanche instruction des partie
        game.update(screen)
        Enrengistreur_donner.save(game)
        #verif si jeux pas commencer
    else:

        #ajouterecran bienvenue
        screen.blit(banner, (330, 0))
        screen.blit(play_button, play_button_rect)
        # barre de dif
        pygame.draw.rect(screen, (111, 210, 46), [50, 40, 70, 45])
        pygame.draw.rect(screen, (255, 90, 0), [150, 40, 70, 45])
        pygame.draw.rect(screen, (200, 0, 0), [250, 40, 70, 45])
        pseudotext = game.font.render(f"Name: {pseudo}", 1, (0, 232, 150))
        screen.blit(pseudotext, (10, 0))
        Buid_name = game.font.render(f"Build_By: Reptille_Eliashm ", 1, (199, 0, 57))
        screen.blit(Buid_name, (850, 635))
    #mettre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
    #que l'evenement est fermer fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #detecter joueur touche clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter touche espace projectile
            if event.key == pygame.K_SPACE and game.player.tire == False:
                game.player.launch_projectile()
                if game.anima.anima == True:
                    game.player.image = pygame.image.load("image/perso comb.gif")
                    game.player.image = pygame.transform.scale(game.player.image, (280, 350))

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verif si souris touche bouton
            if play_button_rect.collidepoint(event.pos):
                #mettre me jeux en true
                game.start()
            if event.pos >= (51, 82) and game.is_playing == False:
                if event.pos <= (120, 40):
                    print( )

                if event.pos >= (140, 39) and game.is_playing == False:
                    if event.pos <= (220, 82):
                        print( )
                        if game.player.health >= 200:
                            game.player.health -= game.player.medium


                    if event.pos <= (320, 39) and game.is_playing == False:
                        if event.pos >= (250, 82):
                            print( )
                            if game.player.health >= 200:
                                game.player.health -= game.player.hard



    #fixer le nombre de fps
    clock.tick(FPS)
