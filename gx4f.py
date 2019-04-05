import pygame, time


######################################################################################

def hanoi(n, fro='A', to='B', aux='C'):
    
    if n == 1:
        TOH.append((1, fro, to))
    else:
        hanoi(n-1, fro, aux, to)
        TOH.append((n, fro, to))
        hanoi(n-1, aux, to, fro)

######################################################################################

def drawDisk(disk, x, y):

    disk[1].center = (x, y)
    surface.blit(disk[0], disk[1])

######################################################################################

def drawAll(peg):

    if Disks_on_Sites[peg]:
        Tops[peg] = 358
        for i in Disks_on_Sites[peg]:
            drawDisk(Array[i], Anchors[peg], Tops[peg])
            Tops[peg] -= 29

######################################################################################

def setRoute(n, fro, to):
    global XY
    XY = []

    inc = (39-Tops[fro]) // 17
    x = Anchors[fro] 
    y = Tops[fro]
    XY.append((x, y))
    while y > 39:
        y += inc
        XY.append((x, y))
    if y < 39:
        XY.pop()
        XY.append((x, 39))

    if ord(to) > ord(fro):
        inc = (Anchors[to]-Anchors[fro]) // 9
        x = Anchors[fro]
        XY.append((x, 39))
        while x < Anchors[to]:
            x += inc
            XY.append((x, 39))
        if x > Anchors[to]:
            XY.pop()
            XY.append((Anchors[to], 39))
    else:
        inc = (Anchors[to]-Anchors[fro]) // 9
        x = Anchors[fro]
        XY.append((x, 39))
        while x > Anchors[to]:
            x += inc
            XY.append((x, 39))
        if x < Anchors[to]:
            XY.pop()
            XY.append((Anchors[to], 39))

    inc = (Tops[to]-39) // 17
    x = Anchors[to] 
    y = 39
    XY.append((x, y))
    while y < Tops[to]:
        y += inc
        XY.append((x, y))
    if y > Tops[to]:
        XY.pop()
        XY.append((x, Tops[to]))

#####################################################################################

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption('The Tower of Hanoi Demo!')

FPS = 30
fpsClock = pygame.time.Clock()
game_over = False

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 190)
BLACK = (50, 50, 50)

Tops = {'A': 213, 'B': 358, 'C': 358}
Anchors = {'A': 93, 'B': 293, 'C': 493}
Disks_on_Sites = {'A': [6, 5, 4, 3, 2, 1], 'B': [], 'C': []}
 
fontObj1 = pygame.font.Font('freesansbold.ttf', 14)
fontObj2 = pygame.font.Font(r'c:\windows\fonts\mingliu.ttc', 24)
fontObj3 = pygame.font.Font(r'c:\windows\fonts\mingliu.ttc', 28)
fontObj3.set_bold(True)
fontObj3.set_underline(True)

textSurfObj = fontObj2.render('遞迴示例：六層河內塔', True, WHITE, BLUE)
textRectObj = textSurfObj.get_rect()

pegSurfObj1 = fontObj1.render('A', True, GREEN, BLUE)
pegRectObj1 = pegSurfObj1.get_rect()
pegSurfObj2 = fontObj1.render('B', True, GREEN, BLUE)
pegRectObj2 = pegSurfObj2.get_rect()
pegSurfObj3 = fontObj1.render('C', True, GREEN, BLUE)
pegRectObj3 = pegSurfObj3.get_rect()


textSurfObj0 = fontObj3.render('', True, BLACK, WHITE)
textRectObj0 = textSurfObj0.get_rect()
textSurfObj1 = fontObj3.render('1', True, BLACK, WHITE)
textRectObj1 = textSurfObj1.get_rect()
textSurfObj2 = fontObj3.render(' 2 ', True, BLACK, WHITE)
textRectObj2 = textSurfObj2.get_rect()
textSurfObj3 = fontObj3.render('  3  ', True, BLACK, WHITE)
textRectObj3 = textSurfObj3.get_rect()
textSurfObj4 = fontObj3.render('   4   ', True, BLACK, WHITE)
textRectObj4 = textSurfObj4.get_rect()
textSurfObj5 = fontObj3.render('    5    ', True, BLACK, WHITE)
textRectObj5 = textSurfObj5.get_rect()
textSurfObj6 = fontObj3.render('     6     ', True, BLACK, WHITE)
textRectObj6 = textSurfObj6.get_rect()

Array = [(textSurfObj0, textRectObj0),
  (textSurfObj1, textRectObj1), (textSurfObj2, textRectObj2),
  (textSurfObj3, textRectObj3), (textSurfObj4, textRectObj4),
  (textSurfObj5, textRectObj5), (textSurfObj6, textRectObj6)]

#TOH = [(1, 'A', 'C'), (2, 'A', 'B'), (1, 'C', 'B')]
#TOH = [(2, 'A', 'B'), (1, 'A', 'C')]
TOH = []
hanoi(6)


#X, Y = 10, 10
idx = 0
idx_TOH = 0
De, from_peg, to_peg = TOH[idx_TOH]
idx_TOH = 1
Disks_on_Sites[from_peg].pop()
setRoute(De, from_peg, to_peg)
finished = False

while not game_over:
    # 由 pygame 取得事件 (event)
    surface.fill((31, 255, 231))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
            #X, Y = 493, 358

    textRectObj.center = (120, 12)
    surface.blit(textSurfObj, textRectObj)

    pygame.draw.rect(surface, (150, 150, 150), (90, 100, 5, 273), 0)
    pygame.draw.rect(surface, (150, 150, 150), (290, 100, 5, 273), 0)
    pygame.draw.rect(surface, (150, 150, 150), (490, 100, 5, 273), 0)
    pygame.draw.rect(surface, (150, 150, 0), (0, 373, 600, 27), 0)

    pegRectObj1.center = (Anchors['A'], 386)
    surface.blit(pegSurfObj1, pegRectObj1)
    pegRectObj2.center = (Anchors['B'], 386)
    surface.blit(pegSurfObj2, pegRectObj2)
    pegRectObj3.center = (Anchors['C'], 386)
    surface.blit(pegSurfObj3, pegRectObj3)


    drawAll('A')
    drawAll('B')
    drawAll('C')


    if idx < len(XY):
        X, Y = XY[idx]
        idx += 1
    else:
        time.sleep(0.05)
        if not finished:
            Disks_on_Sites[to_peg].append(De)
            Tops[to_peg] -= 29

        if idx_TOH < len(TOH):
            De, from_peg, to_peg = TOH[idx_TOH]
            Disks_on_Sites[from_peg].pop()
            setRoute(De, from_peg, to_peg)
            idx_TOH += 1
            idx = 0
        else:
            finished = True
        

    #'''
    textsurf, textrect = Array[De]
    textrect.center = (X, Y)
    surface.blit(textsurf, textrect)
    #'''

    

    pygame.display.flip()
    #time.sleep(0.01)
    pygame.display.update()
    fpsClock.tick(FPS)
