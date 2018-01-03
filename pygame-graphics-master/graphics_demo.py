# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (198, 19, 28)
GREEN = (21, 96, 21)
BLUE = (57, 140, 198)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BROWN = (96, 45, 21)
YELLOW = (255, 170, 0)
    

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(WHITE)
    '''house'''
    pygame.draw.rect(screen, RED, [250, 250, 300, 300])
    pygame.draw.rect(screen, BROWN, [420, 420, 75, 200])
    pygame.draw.polygon(screen, BROWN, [[200, 250], [400,125], [600, 250]])
    pygame.draw.rect(screen, BLUE, [300, 300, 75, 75])
    pygame.draw.rect(screen, BLUE, [450, 300, 75, 75])
    
    '''grass'''
    pygame.draw.line(screen, GREEN, [0, 550], [1000, 550], 100)
    
    '''sky'''
    pygame.draw.line(screen, BLUE, [0, 0], [1000,0], 100)
    
    '''tree'''
    pygame.draw.rect(screen, BROWN, [50, 150, 50, 375])
    pygame.draw.ellipse(screen, GREEN, [-25, 50, 200, 200])
    
    '''sun'''
    pygame.draw.ellipse(screen, YELLOW, [700, -100, 200, 200])
    
    '''fence'''
    y = 530
    for x in range(5, 1000, 30):
        post = [[x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]]
        pygame.draw.polygon(screen, WHITE, post)

    pygame.draw.rect(screen, WHITE, [0, y+10, 1000, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 1000, 5])

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
   # pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
