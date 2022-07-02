import pygame
from comet import Comet

# Creer la class pour gerer cet evenement
class CometFallEvent:

    # lors du chargenement -> creer un compteur
    def __init__(self, game):
        self.percent_speed = 3
        self.percent = 0
        self.game = game
        self.fall_mode = False

        # definir un groupe sprite pour stcoker nos cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 150

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1, 15):
            # appaitre 1 boule de feu
            self.all_comets.add(Comet(self))


    def attempt_fall(self):
        # la jauge d'evenement est totalement charger
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            print("Pluie de cometes !!")
            self.meteor_fall()
            self.fall_mode = True # Activer l'evenement


    def update_bar(self, surface):
        # Ajouter du poucentage à la barre
        self.add_percent()

        # barre noir (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe de x
            surface.get_height() -20, # l'axe des y
            surface.get_width(), # longueur de la fênetre
            10 # epaisseur de la barre
        ])
        # barre rouge ( jauge d'event )
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe de x
            surface.get_height() -20,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fênetre
            10 # epaisseur de la barre
        ])