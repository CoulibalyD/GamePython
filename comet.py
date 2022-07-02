import pygame
import random
# Class comet

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image associer a cette comette
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # Verifier si le npmbre de comet de 0
        if len(self.comet_event.all_comets) == 0:
            print("L'evenement est fini")
            # remettre la barre à 0
            self.comet_event.reset_percent()
            # apparaitre les 2 premiers monstre
            self.comet_event.game.start()


    def fall(self):
        self.rect.y += self.velocity
        # ne tombe pas sur le sol
        if self.rect.y >= 510:
            print('sol')
            # retirer la boule de jeu
            self.remove()

            # s'il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("L'evenement est finiii")
                # remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

            # verifier si la boule de jeu touche le joueur

            if self.comet_event.game.check_collision(
                    self, self.comet_event.game.all_players
            ):
                print(' Joueur Toucher !')
                # retirer la boule de feu
                self.remove()
                # subir 10 points de degats
                self.comet_event.game.player.damage(20)
