import pygame

WHITE = (255,255,255)
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 512

def back(x,y):
    global window, background
    window.blit(background,(x,y))

def airplane(x,y):
    global window, aircraft
    window.blit(aircraft,(x,y))

def runGame():
    global window, aircraft, clock

    x = WINDOW_WIDTH * 0.05
    y = WINDOW_HEIGHT * 0.8
    y_change = 0

    background_x = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        y += y_change
        window.fill(WHITE)

        back(background_x,0)
        airplane(x,y)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global window, aircraft,clock,background

    pygame.init()
    window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Flying Game')
    aircraft = pygame.image.load('./img/airplane2.png')
    aircraft = pygame.transform.scale(aircraft, (120, 80))

    background = pygame.image.load('./img/background.jpg')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    clock = pygame.time.Clock()
    runGame()

initGame()