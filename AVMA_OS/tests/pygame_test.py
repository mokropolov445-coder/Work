import pygame
import sys
from player import Player
from move import mova_and_collide
pygame.init()

game_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Test game')
game_clock = pygame.time.Clock()

platforms = [
    pygame.Rect(0, 550, 100, 250),
    pygame.Rect(300, 300, 20, 560),
    pygame.Rect(20, 780, 0, 300),
]

player = Player(100, 200)

run_game = True
while run_game:
    dt = game_clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    mova_and_collide(player, platforms, dt)
    game_screen.fill((0, 0, 0))
    for p in platforms:
        pygame.draw.rect(game_screen, (100, 100, 100), p)
    game_screen.blit(player.image, player.rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
