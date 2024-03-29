# the original thing was too messy and destroyed for me to even read - redoing it here
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
    K_w,
    K_a,
    K_s,
    K_d
)

pygame.init()

class c_axis(Enum):
    up = 1
    down = -1
    left = 2
    right = -2
font = pygame.font.SysFont('arial', 24)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('paytondev')
circleX = 400
circleY = 300
accelerationX = 0
accelerationY = 0
accelMultiplier = 0.001
running = True
accelText = "..."


def moveUp():
    global accelerationY
    accelerationY+=accelMultiplier
def moveDown():
    global accelerationY
    accelerationY-=accelMultiplier
def moveLeft():
    global accelerationX
    accelerationX+=accelMultiplier
def moveRight():
    global accelerationX
    accelerationX-=accelMultiplier
def checkBounds():
    global circleX, circleY, accelerationX, accelerationY
    if circleX > 800:
        accelerationX+=(accelMultiplier * 10)
    if circleX < 0:
        accelerationX-=(accelMultiplier * 10)
    if circleY > 600:
        accelerationY+=(accelMultiplier * 10)
    if circleY < 0:
        accelerationY-=(accelMultiplier * 10)


while running:
    if accelerationX == 0:
        accelerationX = 0
    if accelerationY == 0:
        accelerationY = 0
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0 and keys[pygame.K_LCTRL]:
                accelMultiplier+=accelMultiplier
            elif event.y > 0:
                accelMultiplier+=0.001
            elif event.y < 0 and keys[pygame.K_LCTRL]:
                accelMultiplier-=accelMultiplier
            elif event.y < 0:
                accelMultiplier-=0.001
    
    if keys[K_UP]:
        moveUp()
    if keys[K_DOWN]:
        moveDown()
    if keys[K_LEFT]:
        moveLeft()
    if keys[K_RIGHT]:
        moveRight()    
    if keys[K_SPACE]:
        accelerationX = 0   
        accelerationY = 0  
        accelMultiplier = 0.001 
    accelText = "X: " + str(accelerationX) + ", Y: " + str(accelerationY) + ", accelMultiplier: " + str(accelMultiplier)
    #if there are no keys being pressed
    #and if acceleration is not zero
    #subtract acceleration by accelMultiplier
    if accelerationY != 0:
        if (keys[K_UP] != True and keys[K_DOWN] != True):
            if accelerationY > 0:
                accelerationY-=accelMultiplier
            else:
                accelerationY+=accelMultiplier
    if accelerationX != 0:
        if (keys[K_LEFT] != True and keys[K_RIGHT] != True):
            if accelerationX > 0:
                accelerationX-=accelMultiplier
            else:
                accelerationX+=accelMultiplier


    #movement. if acceleration > 0, circle moves in that direction. if acceleration = 0, circle doesnt move (hopefully)
    circleY-=0.5*accelerationY
    circleX-=0.5*accelerationX
    checkBounds()
    
    screen.fill((255, 255, 255))
    img = font.render(accelText, True, (0,0,0))
    pygame.draw.circle(screen, (0, 0, 255), (circleX, circleY), 75)
    screen.blit(img, [100, 100])
    pygame.display.flip()
pygame.quit()
