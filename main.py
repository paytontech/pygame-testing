import pygame

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


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('paytondev')

circleX = 250
circleY = 250
running = True
acceleration = 0
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
textfont = pygame.font.SysFont('Comic Sans MS', 30)
while running:
    accelText = 'Acceleration: ' + str(acceleration)
    textfont.render_to(screen, (40, 350), accelText, (0, 0, 0))
    keys = pygame.key.get_pressed()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYUP:
            acceleration = 0
        if event.type == pygame.QUIT:
            running = False

    if keys[K_UP]:
                
                acceleration += 0.01
                circleY -= 0.5 * acceleration
    elif keys[K_DOWN]:
                acceleration += 0.01
                circleY += 0.5 * acceleration
    elif keys[K_LEFT]:
                acceleration += 0.01
                circleX -= 0.5 * acceleration
    elif keys[K_RIGHT]:
                acceleration += 0.01
                circleX += 0.5 * acceleration
    if keys == []:
        acceleration = 0
    if circleX > 800:
        circleX = 0
    if circleY > 600:
        circleY = 0
    if circleX < 0:
        circleX = 800
    if circleY < 0:
        circleY = 600
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (circleX, circleY), 75)

    # Flip the display
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()