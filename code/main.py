import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.running = True

    def run(self):
        while self.running:
            self.get_events()
            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.level.toggle_menu()

                if self.level.game_over:

                    if event.key == pygame.K_r:
                        self.level.game_over = False
                        self.level = Level()
                    if event.key == pygame.K_q:
                        pygame.display.quit()
                        pygame.quit()



if __name__ == '__main__':
    game = Game()
    game.run()
