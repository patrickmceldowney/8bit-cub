import pygame
from settings import *


class Endgame:
    def __init__(self, player):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.player = player

        # dimensions
        size = self.display_surface.get_size()
        self.height = size[1] * 0.4
        self.width = size[0] // 2
        self.left = (size[0] - self.width) // 2
        self.top = (size[1] - self.height) // 2
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def display(self):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_BORDER_ACTIVE, self.rect, 4)

        text_surf = self.font.render('Game Over', False, TEXT_COLOR)
        text_rect = text_surf.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 20))
        respawn_surf = self.font.render('Press R to Respawn or Q to quit', False, TEXT_COLOR)
        respawn_rect = respawn_surf.get_rect()
        respawn_rect.center = self.display_surface.get_rect().center
        self.display_surface.blit(text_surf, text_rect)
        self.display_surface.blit(respawn_surf, respawn_rect)
