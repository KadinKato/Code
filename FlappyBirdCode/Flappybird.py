#Important different libaries that will be needed
import pygame
import sys
import random
from Game_Creations import pipe_creation, pipe_spawner, pipe_movement, check_collision, score

def FlappyBirdCore():
    #Initiliazing Pygame and the sound mixer
    pygame.init()
    pygame.mixer.init()

    #Screen settings
    Width, Height = 400, 600
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Flappy Bird")

    #Colors
    White = (255, 255, 255)
    Blue = (135, 206, 235)
    Green = (0, 200, 0)

    #Misc
    Bird = pygame.image.load("THEBIRDY.png").convert_alpha()
    #Need to add THEBIRD.png picture into your pygame folder.
    Bird = pygame.transform.scale(Bird, (50,40))
    bird_rect = Bird.get_rect(center=(100, Height//2))

    #Game variables
    running = True
    gravity = 0.7
    bird_movement = 0
    Scoring_Number = 0

    #Sounds
    #Jump = pygame.mixer.Sound("67.mp3")           

    #pipe dimensions
    pipe_width = 60
    pipe_gap = 150
    pipe_speed = 3
    pipes = []

    # Events
    Spawnpipe = pygame.USEREVENT
    pygame.time.set_timer(Spawnpipe, 1200)
    font = pygame.font.SysFont(None, 40)
    clock = pygame.time.Clock()

    #Flappy Bird runs when true
    while True:
        
        #Every event in pygame will run
        for event in pygame.event.get():

            #If the event is to quit, this runs
            #When user exits, pygame quits and the system ends
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #If the event is a keypress, this runs
            if event.type == pygame.KEYDOWN:

                #If they key pressed is Space and running is True, this runs
                #The bird is set to -8 movement(In pygame, negative is up)
                if event.key == pygame.K_SPACE and running:
                    bird_movement = -8

                #If they key pressed is Space and running is False, this runs
                if event.key == pygame.K_SPACE and not running:
                    #This is at the end when the game needs to be reset if they decide to play agian
                    bird_rect.center = (100, Height // 2)
                    bird_movement = 0
                    pipes.clear()
                    Scoring_Number = 0
                    running = True 
            
            #If the event is Spawnpipe event, this runs
            #Exttends the list of pipes at their own dimensions
            if event.type == Spawnpipe: 
                pipes.extend(pipe_spawner(Width, Height, pipe_width, pipe_gap))

        #Sets the screen color to Blue
        screen.fill(Blue)
        
        #If running is true, this runs
        if running:
            #Bird Movement
            bird_movement += gravity
            bird_rect.centery += bird_movement
            screen.blit(Bird, bird_rect)

            #Pipes
            pipes = pipe_movement(pipes, pipe_speed)
            pipe_creation(screen,pipes,Green)

            # Collision
            running = check_collision(bird_rect, pipes, Height)

            # Scoring
            for pipe in pipes:
                if pipe.centerx == bird_rect.centerx:
                    Scoring_Number += 0.5  
            score(screen, font, Scoring_Number)

        #In any other case, this runs
        else:
            game_over_surface = font.render("Game Over! Press SPACE", True, (0, 0, 0))
            screen.blit(game_over_surface, (30, Height // 2 - 20))

        #Updates the screen with the user events as well as updates the tick at 60FPS
        pygame.display.update()
        clock.tick(60)

#The main method where the game will run in
if __name__ == "__main__":
    FlappyBirdCore()
