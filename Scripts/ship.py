import pygame

class Ship:

    def __init__(self, aiGame):
        self.screen = aiGame.screen
        self.screen_rect = aiGame.screen.get_rect()

        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
