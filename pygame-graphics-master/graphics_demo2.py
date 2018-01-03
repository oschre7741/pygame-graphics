# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "I wish I Could Do This But I Live In South Carolina"
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

def draw_cloud(x, y):
    x = random.randrange(-100, 1000)
    y = random.randrange(-100, 10)
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

    
snow_list = []
for i in range(200):
        x = random.randrange(0, 1000)
        y = random.randrange(0, 500)
        snow_list.append([x, y])
        
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
    screen.fill(BLUE)
    '''snow'''
    pygame.draw.line(screen, WHITE, [0, 500], [1000, 500], 200)
    
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1
        if snow_list[i][1] > 500:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 1000)
            snow_list[i][0] = x

    ''' clouds '''
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)
    draw_cloud(x, y)


    
    '''snowman'''
    pygame.draw.ellipse(screen, WHITE, [300, 250, 200, 200])
    pygame.draw.ellipse(screen, WHITE, [325, 150, 150, 150])
    pygame.draw.ellipse(screen, WHITE, [350, 75, 100, 100])

    '''arms'''
    pygame.draw.line(screen, BROWN, [465, 210], [500, 135], 10)
    pygame.draw.line(screen, BROWN, [300, 135], [335, 210], 10)
    
    '''buttons'''
    pygame.draw.ellipse(screen, BLACK, [395, 200, 15, 15])
    pygame.draw.ellipse(screen, BLACK, [395, 250, 15, 15])
    pygame.draw.ellipse(screen, BLACK, [395, 300, 15, 15])

    '''eyes'''
    pygame.draw.ellipse(screen, BLACK, [375, 100, 10, 10])
    pygame.draw.ellipse(screen, BLACK, [410, 100, 10, 10])

    '''nose'''
    pygame.draw.polygon(screen, ORANGE, [[393, 115], [393,130], [415, 123]])

    '''hat'''
    pygame.draw.rect(screen, BLACK, [375, 10, 50, 55])
    pygame.draw.rect(screen, BLACK, [363, 60, 75, 25])

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
   # pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
