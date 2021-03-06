############################################################
#
#      Title:  The Tower of Hanoi of 6 Levels
#     Author:  Greg Huang
#       Date:  2019/03/27
#  Copyright:  Released under a "Simplified BSD" license
#
############################################################

import pygame

############################################################

def tower_hanoi(n):

    global TOH
    TOH = []
    toh(TOH, n)

############################################################

def toh(log, n, fro='A', to='B', aux='C'):

    if n == 1:
        log.append((1, fro, to))
    else:
        toh(log, n-1, fro, aux, to)
        log.append((n, fro, to))
        toh(log, n-1, aux, to, fro)

############################################################

def drawDisk(disk, x, y):

    disk[1].center = (x, y)
    surface.blit(disk[0], disk[1])

############################################################

def drawAll(peg):

    # global H

    if Disks_on_Sites[peg]:
        Tops[peg] = 378 - (H+1)//2
        for i in Disks_on_Sites[peg]:
            drawDisk(Array[i], Anchors[peg], Tops[peg])
            Tops[peg] -= H

############################################################

def setRoute(n, fro, to):

    global XY
    XY = []

    # vertical movement on the source position

    inc = (63-Tops[fro]) // 15
    x = Anchors[fro] 
    y = Tops[fro]
    XY.append((x, y))
    while y > 63:
        y += inc
        XY.append((x, y))
    if y < 63:
        XY.pop()
        XY.append((x, 63))

    # horizontal movement over the top

    if ord(to) > ord(fro):
        inc = (Anchors[to]-Anchors[fro]) // 15
        x = Anchors[fro]
        XY.append((x, 63))
        while x < Anchors[to]:
            x += inc
            XY.append((x, 63))
        if x > Anchors[to]:
            XY.pop()
            XY.append((Anchors[to], 63))
    else:
        inc = (Anchors[to]-Anchors[fro]) // 15
        x = Anchors[fro]
        XY.append((x, 63))
        while x > Anchors[to]:
            x += inc
            XY.append((x, 63))
        if x < Anchors[to]:
            XY.pop()
            XY.append((Anchors[to], 63))

    # vertical movement on the destination position

    inc = (Tops[to]-63) // 15
    x = Anchors[to] 
    y = 63
    XY.append((x, y))
    while y < Tops[to]:
        y += inc
        XY.append((x, y))
    if y > Tops[to]:
        XY.pop()
        XY.append((x, Tops[to]))

############################################################

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption('"The Tower of Hanoi of 6 Levels" Demo!')

FPS = 60
ADJ = -50
fpsClock = pygame.time.Clock()
game_over = False

WHITE = (255, 255, 255)
BLUE = (0, 0, 190)
BLACK = (50, 50, 50)
GREY = (180, 180, 180) 

Anchors = {'A': 98, 'B': 298, 'C': 498}
Disks_on_Sites = {'A': [6, 5, 4, 3, 2, 1], 'B': [], 'C': []}

soundObj = pygame.mixer.Sound('diesel-horn.wav')

fontObj1 = pygame.font.SysFont('arial', 14)
fontObj2 = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 24)
fontObj3 = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 28)
fontObj3.set_bold(True)
fontObj3.set_underline(True)

''' 中文顯示
textObj = fontObj2.render('遞迴示例：六層河內塔', True, WHITE, BLUE)
'''
textObj = fontObj2.render('An Exemplar of Recursion', True, WHITE, BLUE)
textRectObj = textObj.get_rect()

pegObj1 = fontObj1.render('A', True, WHITE, BLUE)
pegRectObj1 = pegObj1.get_rect()
pegObj2 = fontObj1.render('B', True, WHITE, BLUE)
pegRectObj2 = pegObj2.get_rect()
pegObj3 = fontObj1.render('C', True, WHITE, BLUE)
pegRectObj3 = pegObj3.get_rect()

diskObj0 = fontObj3.render('', True, BLACK, WHITE)
diskRectObj0 = diskObj0.get_rect()
diskObj1 = fontObj3.render('1', True, BLACK, WHITE)
diskRectObj1 = diskObj1.get_rect()
diskObj2 = fontObj3.render(' 2 ', True, BLACK, WHITE)
diskRectObj2 = diskObj2.get_rect()
diskObj3 = fontObj3.render('  3  ', True, BLACK, WHITE)
diskRectObj3 = diskObj3.get_rect()
diskObj4 = fontObj3.render('   4   ', True, BLACK, WHITE)
diskRectObj4 = diskObj4.get_rect()
diskObj5 = fontObj3.render('    5    ', True, BLACK, WHITE)
diskRectObj5 = diskObj5.get_rect()
diskObj6 = fontObj3.render('     6     ', True, BLACK, WHITE)
diskRectObj6 = diskObj6.get_rect()

H = diskRectObj0.height
Tops = {'A': 378-5*H-(H+1)//2, 'B': 378-(H+1)//2, 'C': 378-(H+1)//2}

Array = [(diskObj0, diskRectObj0),
    (diskObj1, diskRectObj1), (diskObj2, diskRectObj2),
    (diskObj3, diskRectObj3), (diskObj4, diskRectObj4),
    (diskObj5, diskRectObj5), (diskObj6, diskRectObj6)]

tower_hanoi(6)
FINAL = 6
De, fro_peg, to_peg = TOH[0]
step = 1
Disks_on_Sites[fro_peg].pop()
setRoute(De, fro_peg, to_peg)
X, Y = XY[0]
idx = 1
finished = False

while not game_over:

    surface.fill((25, 255, 255))

    pressed = pygame.key.get_pressed()
    ALT_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            FPS += ADJ
            ADJ = -ADJ
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and ALT_held:
                game_over = True

    surface.blit(textObj, textRectObj)

    pygame.draw.rect(surface, GREY, (96, 100, 4, 278), 0)
    pygame.draw.rect(surface, GREY, (296, 100, 4, 278), 0)
    pygame.draw.rect(surface, GREY, (496, 100, 4, 278), 0)
    pygame.draw.rect(surface, (150, 150, 0), (0, 378, 600, 22), 0)

    pegRectObj1.center = (Anchors['A'], 389)
    surface.blit(pegObj1, pegRectObj1)
    pegRectObj2.center = (Anchors['B'], 389)
    surface.blit(pegObj2, pegRectObj2)
    pegRectObj3.center = (Anchors['C'], 389)
    surface.blit(pegObj3, pegRectObj3)

    drawAll('A')
    drawAll('B')
    drawAll('C')

    stepObj = fontObj1.render(str(step), True, WHITE, BLACK)
    stepRectObj = stepObj.get_rect()
    stepRectObj.center = (Anchors['B'], (textRectObj.height+1)//2)
    surface.blit(stepObj, stepRectObj)

    if not finished:

        text, textrect = Array[De]
        textrect.center = (X, Y)
        surface.blit(text, textrect)

        if idx < len(XY):
            X, Y = XY[idx]
            idx += 1
        else:
            if FINAL == De:
                FINAL -= 1
                soundObj.play()
                pygame.time.wait(1000)
                soundObj.stop()

            Disks_on_Sites[to_peg].append(De)
            Tops[to_peg] -= H

            if step < len(TOH):
                De, fro_peg, to_peg = TOH[step]
                step += 1
                Disks_on_Sites[fro_peg].pop()
                setRoute(De, fro_peg, to_peg)
                X, Y = XY[0]
                idx = 1
            else:
                finished = True

    pygame.display.update()
    fpsClock.tick(FPS)
