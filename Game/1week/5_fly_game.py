import pygame
import random

WHITE = (255, 255, 255)
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 512
AIRCRAFT_WIDTH = 100
AIRCRAFT_HEIGHT = 55

def drawObject(obj,x, y):
    global window
    window.blit(obj, (x, y))

def runGame():
    global window, aircraft, clock, background, background_next
    global monster, fires, bullet

    bullet_xy = []

    x = WINDOW_WIDTH * 0.05
    y = WINDOW_HEIGHT * 0.8
    y_change = 0

    background_x = 0
    background_x_next = WINDOW_WIDTH

    monster_x = WINDOW_WIDTH
    monster_y = random.randrange(0,WINDOW_HEIGHT)

    fire_x = WINDOW_WIDTH
    fire_y = random.randrange(0,WINDOW_HEIGHT)
    random.shuffle(fires)
    fire = fires[0]

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
                elif event.key == pygame.K_SPACE:
                    bullet_x = x + AIRCRAFT_WIDTH
                    bullet_y = y + AIRCRAFT_HEIGHT/2

                    bullet_xy.append([bullet_x,bullet_y])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        window.fill(WHITE)

        background_x -= 2
        background_x_next -= 2

        if background_x == -WINDOW_WIDTH:
            background_x = WINDOW_WIDTH

        if background_x_next == -WINDOW_WIDTH:
            background_x_next = WINDOW_WIDTH

        drawObject(background, background_x, 0)
        drawObject(background_next, background_x_next, 0)
        #
        y += y_change
        if y < 0:
            y = 0
        elif y > WINDOW_HEIGHT - AIRCRAFT_HEIGHT:
            y = WINDOW_HEIGHT - AIRCRAFT_HEIGHT

        drawObject(aircraft, x, y)
        #
        monster_x -= 7
        if monster_x <= 0:
            monster_x = WINDOW_WIDTH
            monster_y = random.randrange(0,WINDOW_HEIGHT)

        drawObject(monster, monster_x, monster_y)
        #
        if fire is None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = WINDOW_WIDTH
            fire_y = random.randrange(0,WINDOW_HEIGHT)
            random.shuffle(fires)
            fire = fires[0]
        if fire != None:
            drawObject(fire,fire_x,fire_y)
        #
        if len(bullet_xy) != 0:
            for i,bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]
                if bxy[0] >= WINDOW_WIDTH:
                    bullet_xy.remove(bxy)

        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def initGame():
    global window, aircraft, clock, background, background_next
    global monster,fires,bullet

    pygame.init()
    window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Flying Game')
    aircraft = pygame.transform.scale(pygame.image.load('./img/airplane2.png'), (AIRCRAFT_WIDTH, AIRCRAFT_HEIGHT))


    background = pygame.transform.scale(pygame.image.load('./img/background.jpg'), (WINDOW_WIDTH, WINDOW_HEIGHT))
    background_next = background.copy()

    monster = pygame.transform.scale(pygame.image.load('./img/devil.png'), (100, 80))

    fire1 = pygame.transform.scale(pygame.image.load('./img/fire1.png'), (100, 80))
    fire2 = pygame.transform.scale(pygame.image.load('./img/fire2.png'), (100, 80))

    fires = [fire1, fire2, None, None, None, None, None]

    bullet = pygame.transform.scale(pygame.image.load('./img/bullet.png'), (20, 10))

    clock = pygame.time.Clock()
    runGame()

if __name__ == '__main__':
    initGame()
