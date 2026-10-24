import pygame

def mova_and_collide(player, platforms, dt):
    keys = pygame.key.get_pressed()

    player.vel_x = 0
    if keys[pygame.K_LEFT]:
        player.vel_x = -300
    if keys[pygame.K_RIGHT]:
        player.vel_x = 300

    player.rect.x += player.vel_x * dt

    for p in platforms:
        if player.rect.colliderect(p):
            if player.vel_x > 0:
                player.rect_right = p.left
            elif player.vel_x < 0:
                player.rect_left = p.right
            player.vel_x = 0
    player.vel_y = 0
    if keys[pygame.K_DOWN]:
        player.vel_y = 300
    if keys[pygame.K_UP]:
        player.vel_y = -300

    player.rect.y += player.vel_y * dt
    for p in platforms:
        if player.rect.colliderect(p):
            if player.vel_y < 0:
                player.rect_down = p.top
            elif player.vel_y > 0:
                player.rect_up = p.bottom
