import pygame

WHITE = (255,255,255)
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 512

def runGame():
    global window, clock

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        window.fill(WHITE)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global window, clock

    pygame.init()
    window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Flying Game')

    clock = pygame.time.Clock()
    runGame()

initGame()