import pygame
import math
from game import Game

pygame.init()
# definir une clock
clock = pygame.time.Clock()
FPS = 82

# generer la fenetre de notre jeu

pygame.display.set_caption("Dracoul Game")
screen = pygame.display.set_mode((1080, 710))

# importer l'arriere plan
background = pygame.image.load('assets/bg.jpg')

# importer charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer charger le bouton pour lancer le jeu
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# Charger notre jeu
game = Game()

running = True

# boucle tan que cette condition est vrai


while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # Verifier si le jeu à commencer
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # Verifier si le jeu n'a pas commencer
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.QUIT
            print("Fermeture du jeu")

        # Detection de touche utilisee
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche sapace est appuyez
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                    # print("Projectile lancerr")
                else:
                    # Mettre le jeu en mode "lance"
                    game.start()
                    # jouer le don
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verification pour savoir si la souris est en collision avec le boutton jouer
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode "lance"
                game.start()
                #jouer le don
                game.sound_manager.play('click')

    # Fixer le nombre de fps sur ma clock Pour que le jeu soit moins ou plus lent
    clock.tick(FPS)

