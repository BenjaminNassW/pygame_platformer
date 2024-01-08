import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
        self.width = 0
        self.height = 0

    def get_image(self, x_coor, width, height, scale):
        self.width = width
        self.height = height
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (x_coor, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        #image.set_colorkey((0,0,0))

        return image