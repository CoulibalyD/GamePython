import pygame
import random
import animation


# Creation de Monster

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 550 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # infliger des degats
        self.health -= amount

        # verifier si son nouveau nombre de vie est inferieur ou égal à 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # ajouter le nombre de points
            self.game.add_score(self.loot_amount)

            # si la barre d'evenement est charger à son maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monster.remove(self)

                # appel de la méthode pour essayer de declencher la pluie de commet
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # definir la position de notre jauge de vie ainsi que sa largeur et son epaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        # definir la position de l'arrière plan de notre jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner notre bar de vie
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)

    def forward(self):
        # Le deplacement ne se fait que s'il ya collision avec un group de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre en collision avec le joueur

        else:
            # Infliger des degats (au joueur)$
            self.game.player.damage(self.attack)


# definir une class pour la Mummy
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)


# definir une classe pour l'alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), offset=130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)
