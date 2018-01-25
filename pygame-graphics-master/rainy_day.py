# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Rainy Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (42, 96, 21)
WHITE = (232, 232, 232)
BLUE = (82, 147, 175)
YELLOW = (255, 255, 175)
GREY = (90, 91, 91)
GRAY = (50, 52, 53)

# Make clouds
num_clouds = 50
clouds = []
for i in range(num_clouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GRAY, [x + 20, y + 20, 60, 40])

''' Make rain '''
rain = []
for i in range(1000):
    x = random.randrange(-500, 800)
    y = random.randrange(-10, 600)
    z = random.randrange(1, 5)
    r = [x, y, z, z]
    rain.append(r)

def draw_rain(r):
    x = r[0]
    y = r[1]

    pygame.draw.ellipse(screen, BLUE, r)
    
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] += 1

        if c[0] > 900:
           c[0] = random.randrange(-800, -100)
           c[1] = random.randrange(-50, 200)

    for r in rain:
        r[0] += 2.5
        r[1] += 6

        if r[1] > random.randrange(500, 900):
            r[0] = random.randrange(-500, 800)
            r[1] = random.randrange(-10, 0)
             
    # Drawing code
    ''' sky '''
    screen.fill(GREY)

    ''' sun '''
   # pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' rain '''
    for r in rain:
        draw_rain(r)
        
    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

   

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
