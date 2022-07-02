import pygame


# definir la classe projectile
class Projectile(pygame.sprite.Sprite):

    # definir le constructeur

    def __init__(self, player):
        super().__init__()
        self.velocity = 6
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.x = player.rect.x + 122
        self.rect.y = player.rect.y + 82
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player.all_projectiles.remove(self)
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # Verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            # Supprimer le projectile
            self.remove()
            # infliger des degats
            monster.damage(self.player.attack)

        # Verifier si votre projectile n'est plus présent sur l'ecran
        if self.rect.x > 1080:
            # Supprimer Projectile (en dehors de l'ecran)
            self.remove()
            print("Projectile supprimer...")
