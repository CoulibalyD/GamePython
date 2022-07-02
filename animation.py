import pygame


# Class animation*


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # commencer l'animation à l'image 0
        self.images = animation.get(sprite_name)
        self.animation = False

    # definir une methode pour demarer l'animation
    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self, loop=False):

        # verifier si l'animation est active
        if self.animation:  # pas besoin de mettre 'True' à defaut c'est 'True'

            # passer à l'image suivante
            self.current_image += 1

            #   verifier si on atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0

                # Verifier si l'animation n'est pas en mode boucle
                if loop is False:

                    # desactiver l'animation
                    self.animation = False

            # modifier l'image precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# definir une fonction pour changer les images d'un sprite
def load_animation_images(sprite_name):
    # Chager les 24 images de ce sprite dans le dossier correspondante
    images = []

    # recuperer le chemin du dossier pour ce sprite
    path = f'assets/{sprite_name}/{sprite_name}'

    # boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenue de la liste d'images
    return images


# definir un dictionnaire qui va contenir les images chargées de chaque sprites
# mummy -> [...mummy1.png, ..mummy2.png,...]
# mummy -> [...player1.png, ...player2.png,...]
animation = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien'),
}
