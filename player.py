import pygame
from projectile import Projectile
import animation

# Creation du joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
             self.health -= amount
        else:
            # Si le joueur n'a plus de points de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # definir la position de notre jauge de vie ainsi que sa largeur et son epaisseur
        bar_position = [self.rect.x + 50, self.rect.y +15, self.health, 8]

        # definir la position de l'arrière plan de notre jauge de vie
        back_bar_position = [self.rect.x + 50, self.rect.y +15, self.max_health, 8]

        # dessiner notre bar de vie
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)

    def launch_projectile(self):
        # Creation une nouvelle instance
        self.all_projectiles.add(Projectile(self))
        # demarer l'animation du lancer
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        #si le joueur n'est pas collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monster):
           self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity