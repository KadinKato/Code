#Importing libaries that will be needed
import pygame
import random

#Universal color of a pipe
Green = (0,200,0)

def pipe_spawner(swidth, sheight, pwidth, pgap):
    pheight = random.randint(100, sheight - 250)
    bottom = pygame.Rect(swidth, pheight + pgap, pwidth, sheight - (pheight + pgap))
    top = pygame.Rect(swidth, 0, pwidth, pheight)
    return[bottom,top]

def pipe_creation(screen,pipes,color):
    for p in pipes:
        pygame.draw.rect(screen, Green, p)

def pipe_movement(pipes,speed):
    for p in pipes:
        p.centerx -= speed
    return [p for p in pipes if p.right > 0]

def check_collision(bird, pipes, sheight):
    for p in pipes:
        if bird.colliderect(p):
            return False
    if bird.top <= 0 or bird.bottom >= sheight:
        return False
    return True

def score(screen, font, score):
    score_text = font.render(f"Score: {int(score)}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

