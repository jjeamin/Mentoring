# -*- coding: utf-8 -*-
import pygame
import random
from time import sleep

WHITE = (255, 255, 255)
RED = (255,0,0)

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 512
AIRCRAFT_WIDTH = 100
AIRCRAFT_HEIGHT = 55
MONSTER_WIDTH = 110
MONSTER_HEIGHT = 65
#
FIREBALL1_WIDTH = 130
FIREBALL1_HEIGHT = 65
FIREBALL2_WIDTH = 90
FIREBALL2_HEIGHT = 55
#
def drawText(text,font):
    textSurface = font.render(text,True,RED)
    return textSurface, textSurface.get_rect()

def Message(text):
    global window
    
    font = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = drawText(text, font)
    TextRect.center = ((WINDOW_WIDTH/2),(WINDOW_HEIGHT/2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(2)
    runGame()
    
    
def end():
    global window
    Message('THE END')
    

def drawObject(obj,x, y):
    global window
    window.blit(obj, (x, y))

def runGame():
    global window, aircraft, clock, background, background_next
    global monster, fires, bullet, boom

    #
    isShot = False
    boom_count = 0
    #

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
        # KEY EVENT
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
        
        # window clear
        window.fill(WHITE)

        # background
        background_x -= 2
        background_x_next -= 2

        if background_x == -WINDOW_WIDTH:
            background_x = WINDOW_WIDTH

        if background_x_next == -WINDOW_WIDTH:
            background_x_next = WINDOW_WIDTH

        drawObject(background, background_x, 0)
        drawObject(background_next, background_x_next, 0)
        
        # Aircraft
        y += y_change
        if y < 0:
            y = 0
        elif y > WINDOW_HEIGHT - AIRCRAFT_HEIGHT:
            y = WINDOW_HEIGHT - AIRCRAFT_HEIGHT

        drawObject(aircraft, x, y)
        
        # monster
        monster_x -= 7
        if monster_x <= 0:
            monster_x = WINDOW_WIDTH
            monster_y = random.randrange(0,WINDOW_HEIGHT)

        #drawObject(monster, monster_x, monster_y)
        
        # fire
        #
        if fire[1] is None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = WINDOW_WIDTH
            fire_y = random.randrange(0,WINDOW_HEIGHT)
            random.shuffle(fires)
            fire = fires[0]
            
        if fire[1] != None:
            drawObject(fire[1],fire_x,fire_y)
        #
        # bullet
        if len(bullet_xy) != 0:
            for i,bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]
                
                if bxy[0] > monster_x:
                    if bxy[1] > monster_y and bxy[1] < monster_y + MONSTER_HEIGHT:
                        bullet_xy.remove(bxy)
                        isShot = True
                
                if bxy[0] >= WINDOW_WIDTH:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
        #
        if x + AIRCRAFT_WIDTH > monster_x:
            if(y > monster_y and y < monster_y + MONSTER_HEIGHT) or \
            (y + AIRCRAFT_HEIGHT > monster_y) and y + AIRCRAFT_HEIGHT < monster_y + MONSTER_HEIGHT:
                end()
                
        if fire[1] != None:
            if fire[0] == 0:
                fire_w = FIREBALL1_WIDTH
                fire_h = FIREBALL1_HEIGHT
            elif fire[0] == 1:
                fire_w = FIREBALL2_WIDTH
                fire_h = FIREBALL2_HEIGHT
                
            if x + AIRCRAFT_WIDTH > fire_x:
                if(y > fire_y and y < fire_y + fire_h) or \
                (y + AIRCRAFT_HEIGHT > fire_y) and y + AIRCRAFT_HEIGHT < fire_y + fire_h:
                    end()
        #
        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)
                
        if not isShot:
            drawObject(monster, monster_x, monster_y)
        else:
            drawObject(boom, monster_x, monster_y)
            boom_count += 1
            if boom_count > 5:
                boom_count = 0
                monster_x = WINDOW_WIDTH
                monster_y = random.randrange(0,WINDOW_HEIGHT - MONSTER_HEIGHT)
                isShot = False
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def initGame():
    global window, aircraft, clock, background, background_next
    global monster, fires, bullet, boom

    pygame.init()
    window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Flying Game')
    aircraft = pygame.transform.scale(pygame.image.load('./img/airplane2.png'), (AIRCRAFT_WIDTH, AIRCRAFT_HEIGHT))


    background = pygame.transform.scale(pygame.image.load('./img/background.jpg'), (WINDOW_WIDTH, WINDOW_HEIGHT))
    background_next = background.copy()

    monster = pygame.transform.scale(pygame.image.load('./img/devil.png'), (MONSTER_WIDTH, MONSTER_HEIGHT))

    fire1 = pygame.transform.scale(pygame.image.load('./img/fire1.png'), (FIREBALL1_WIDTH, FIREBALL1_HEIGHT))
    fire2 = pygame.transform.scale(pygame.image.load('./img/fire2.png'), (FIREBALL2_WIDTH, FIREBALL2_HEIGHT))

    #
    fires = [(0,fire1), 
             (1,fire2), 
             (2,None), 
             (3,None), 
             (4,None), 
             (5,None), 
             (6,None)]
    #

    bullet = pygame.transform.scale(pygame.image.load('./img/bullet.png'), (20, 10))

    boom = pygame.transform.scale(pygame.image.load('./img/boom.png'), (100, 80))

    clock = pygame.time.Clock()
    runGame()

if __name__ == '__main__':
    initGame()
