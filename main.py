import pygame
import pygame.freetype
from enum import Enum

from pygame.locals import  (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_RETURN,
    KEYDOWN,
    QUIT,
    KEYUP,
)

pygame.init()

class c_axis(Enum):
    up = 1
    down = -1
    left = 2
    right = -2

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('paytondev')

circleX = 250
circleY = 250
running = True
acceleration = 0
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font = pygame.font.SysFont('arial', 24)
accelMultiplier = 0.001

def slow(axis):
    global acceleration
    global circleX
    global circleY
    acceleration-=accelMultiplier
    match axis:
        case c_axis.up:
            circleY -= accelMultiplier * acceleration
            print("slowing circleY")
while running:
    accelText = "Acceleration: " + str(acceleration)
    keys = pygame.key.get_pressed()
    img = font.render(accelText, True, (0,0,0))
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYUP:
            if keys[K_UP]:
                slow(c_axis.up)
            elif keys[K_DOWN]:
                slow(c_axis.down)
            elif keys[K_LEFT]:
                slow(c_axis.left)
            elif keys[K_RIGHT]:
                slow(c_axis.right)
            
        if event.type == pygame.QUIT:
            running = False
    #redoing this
    """
    This code (from what i can gather) check if no keys are being held down, and if so, subtracts acceleration my accelMultiplier
    This is undoubtedly spaghetti code and is largely impossible to read.
    I'm leaving this code here for anybody who thinks that their code is messy. hopefully this brings some confidence to that person.
    anyways im redoing this entire thing so yeah
    """
    """ if accelStopYUp:
        if acceleration > 0:
            acceleration -= accelMultiplier
            circleY -= 0.5 * acceleration
        elif acceleration < 0:
            accelStopYUp = False
    #else:
        #print("done with accelStopYUp")
    if accelStopYDown:
        if acceleration > 0:
            acceleration -= accelMultiplier
            circleY += 0.5 * acceleration
        elif acceleration < 0:
            accelStopYDown = False
    #else:
        #print("done with accelStopYDown")
    if accelStopXLeft:
        if acceleration > 0:
            acceleration -= accelMultiplier
            circleX -= 0.5 * acceleration
        elif acceleration < 0:
            accelStopXLeft = False
    #else:
        #print("done with accelStopxLeft")
    if accelStopXRight:
        if acceleration > 0:
            acceleration -= accelMultiplier
            circleX += 0.5 * acceleration
        elif acceleration < 0:
            accelStopXRight = False
    #else:
        #print("done with accelStopxRight") """
    if keys[K_UP]:
                
                acceleration += accelMultiplier
                circleY -= 0.5 * acceleration
    elif keys[K_DOWN]:
                acceleration += accelMultiplier
                circleY += 0.5 * acceleration
    elif keys[K_LEFT]:
                acceleration += accelMultiplier
                circleX -= 0.5 * acceleration
    elif keys[K_RIGHT]:
                acceleration += accelMultiplier
                circleX += 0.5 * acceleration
    if keys == []:
        acceleration = 0
    if circleX > 600:
        circleX = 0
        accelStopYUp = True
    if circleY > 800:
        circleY = 0
    if circleX < 0:
        circleX = 600
    if circleY < 0:
        circleY = 800
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (circleX, circleY), 75)
    screen.blit(img, [100, 100])
    # Flip the display
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()



