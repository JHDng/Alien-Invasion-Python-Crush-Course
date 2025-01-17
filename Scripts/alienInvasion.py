import sys
import pygame
from Scripts.settings import Settings


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip() #Updates frames

if __name__ == '__main__': #executes only if the script is run not imported
    ai = AlienInvasion()
    ai.run_game()