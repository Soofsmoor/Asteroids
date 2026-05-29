import pygame
from pygame import font
from player import Player

class Score(pygame.sprite.Sprite):
    def __init__(self, player_instance, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player_instance       
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, 36)

    def update(self, dt):
        pass

    def draw(self, screen):
        score_surface = self.font.render(f"Score: {self.player.score}", True, "white")
        screen.blit(score_surface, (self.x, self.y))