import pygame
import time

def drawDisk(disk, x, y):
    disk[1].center = (x, y)
    surface.blit(disk[0], disk[1])

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption('The Tower of Hanoi Demo!')

FPS = 12
fpsClock = pygame.time.Clock()
game_over = False

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 190)
BLACK = (50, 50, 50)

Tops = {'A': 213, 'B': 358, 'C': 358}
Anchors = {'A': (93, 358), 'B': (293, 358), 'C': (493, 358)}
States = {'A': (93, 213), 'B': (293, 358), 'C': (493, 358)}
Disks_on_Sites = {'A': [6, [5, 4, 3, 2, 1, 0]], 'B': [0, []], 'C': [0, []]}
 
#fontObj = pygame.font.Font('freesansbold.ttf', 24)
fontObj = pygame.font.Font(r'c:\windows\fonts\mingliu.ttc', 28)
fontObj.set_bold(True)
fontObj.set_underline(True)
fontObj2 = pygame.font.Font(r'c:\windows\fonts\mingliu.ttc', 24)

fontObj1 = pygame.font.Font('freesansbold.ttf', 14)

#'''
textSurfaceObj = fontObj2.render('遞迴示例：六層河內塔', True, WHITE, BLUE)
textRectObj = textSurfaceObj.get_rect()
#textRectObj.center = (200, 150)
#'''

pegSurfaceObj1 = fontObj1.render('A', True, GREEN, BLUE)
pegRectObj1 = pegSurfaceObj1.get_rect()
pegSurfaceObj2 = fontObj1.render('B', True, GREEN, BLUE)
pegRectObj2 = pegSurfaceObj2.get_rect()
pegSurfaceObj3 = fontObj1.render('C', True, GREEN, BLUE)
pegRectObj3 = pegSurfaceObj3.get_rect()


textSurfaceObj1 = fontObj.render('1', True, BLACK, WHITE)
textRectObj1 = textSurfaceObj1.get_rect()
textSurfaceObj2 = fontObj.render(' 2 ', True, BLACK, WHITE)
textRectObj2 = textSurfaceObj2.get_rect()
textSurfaceObj3 = fontObj.render('  3  ', True, BLACK, WHITE)
textRectObj3 = textSurfaceObj3.get_rect()
textSurfaceObj4 = fontObj.render('   4   ', True, BLACK, WHITE)
textRectObj4 = textSurfaceObj4.get_rect()
textSurfaceObj5 = fontObj.render('    5    ', True, BLACK, WHITE)
textRectObj5 = textSurfaceObj5.get_rect()
textSurfaceObj6 = fontObj.render('     6     ', True, BLACK, WHITE)
textRectObj6 = textSurfaceObj6.get_rect()

Array = [
  (textSurfaceObj1, textRectObj1), (textSurfaceObj2, textRectObj2),
  (textSurfaceObj3, textRectObj3), (textSurfaceObj4, textRectObj4),
  (textSurfaceObj5, textRectObj5), (textSurfaceObj6, textRectObj6)]

'''
XY = [(93, 213), (93, 203), (93, 193), (93, 183), (93, 173), (93, 163), (93, 153),
  (93, 143), (93, 133), (93, 123), (93, 113), (93, 103), (93, 93), (93, 83), (93, 73),
  (143, 73), (193, 73), (243, 73), (293, 73), (343, 73), (393, 73), (443, 73),
  (493, 73), (493, 108), (493, 133), (493, 158),
  (493, 188), (493, 218), (493, 248), (493, 278), (493, 308), (493, 338), (493, 358)]
'''


XY=[]
#

starty = Anchors['A'][1]-Disks_on_Sites['A'][0]*28+(29-Disks_on_Sites['A'][0])
totaly = starty - 39
incry = totaly // 10
for i in range(10):
   #tempy = Anchors['A'][1]-Disks_on_Sites['A']*28+(29-Disks_on_Sites['A'][0])
   #XY.append((Anchors['A'][0], Anchors['A'][1]-Disk_on_Sites['A'][0]*28-i*10))
   tmp_y=starty-i*incry
   XY.append((Anchors['A'][0], tmp_y ))
incrx=200*(ord('C')-ord('A')) // 10
for i in range(11):
    tmp_x=Anchors['A'][0] + incrx*i
    XY.append((tmp_x, tmp_y))

Ly=Anchors['C'][1]-Disks_on_Sites['C'][0]*28+(29-Disks_on_Sites['C'][0]) - tmp_y
incry = Ly//10
iy= tmp_y# incry
while iy <= Anchors['C'][1]:
    XY.append((tmp_x, iy))
    iy += incry
if iy> Anchors['C'][1]:
   XY.append((tmp_x, Anchors['C'][1]))

catx=10
caty=10
X = Anchors['A'][0]
Y = Anchors['A'][1]-Disks_on_Sites['A'][0]*28+23
idx = 0
De = 0
Disks_on_Sites['A'][1].pop()

while (not game_over):
    # 由 pygame 取得事件 (event)
    surface.fill((31, 255, 231))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Disks_on_Sites['A'][0] -= 1
            Disks_on_Sites['C'][0] += 1
            if Disks_on_Sites['A'][1]:
               Disks_on_Sites['A'][1].pop()
            Disks_on_Sites['C'][1].append(0)
            if idx == len(XY): idx = 0
            De = 1
            #X, Y = 493, 358

    textRectObj.center = (120, 12)
    surface.blit(textSurfaceObj, textRectObj)

    pygame.draw.rect(surface, (150, 150, 150), (90, 100, 5, 273), 0)
    pygame.draw.rect(surface, (150, 150, 150), (290, 100, 5, 273), 0)
    pygame.draw.rect(surface, (150, 150, 150), (490, 100, 5, 273), 0)
    pygame.draw.rect(surface, (150, 150, 0), (0, 373, 600, 27), 0)

    pegRectObj1.center = (Anchors['A'][0], Anchors['A'][1]+28)
    surface.blit(pegSurfaceObj1, pegRectObj1)
    pegRectObj2.center = (Anchors['B'][0], Anchors['B'][1]+28)
    surface.blit(pegSurfaceObj2, pegRectObj2)
    pegRectObj3.center = (Anchors['C'][0], Anchors['C'][1]+28)
    surface.blit(pegSurfaceObj3, pegRectObj3)

    pygame.draw.circle(surface, (225, 255, 0), (X-50, Y-15), 15, 2)
 
    
    if idx < len(XY):
        X, Y = XY[idx]
        idx += 1
   
    ###
    '''
    textRectObj1.center = (X, Y)
    surface.blit(textSurfaceObj1, textRectObj1)
    '''

    #textsurf, textrect = textSurfaceObj1, textRectObj1
    textsurf, textrect = Array[De]
    textrect.center = (X, Y)
    surface.blit(textsurf, textrect) 

    #textRectObj2.center = (93, 242)
    #surface.blit(textSurfaceObj2, textRectObj2)
    
    '''
    textRectObj3.center = (93, 271)
    surface.blit(textSurfaceObj3, textRectObj3)
    textRectObj4.center = (93, 300)
    surface.blit(textSurfaceObj4, textRectObj4)
    textRectObj5.center = (93, 329)
    surface.blit(textSurfaceObj5, textRectObj5)
    textRectObj6.center = (93, 358)
    surface.blit(textSurfaceObj6, textRectObj6)
    '''
    for i in Disks_on_Sites['A'][1]:
         drawDisk(Array[i], Anchors['A'][0], 213 + 29*i)

    for i in Disks_on_Sites['C'][1]:
         drawDisk(Array[i], Anchors['C'][0], 213 + 29*i)


    '''

    drawDisk(Array[1], Anchors['A'][0], 242)
    if De!= 2:
        drawDisk(Array[2], Anchors['A'][0], 271)
    else:
        drawDisk(Array[0], Anchors['A'][0], 271)
    drawDisk(Array[3], Anchors['A'][0], 300)
    drawDisk(Array[4], Anchors['A'][0], 329)
    drawDisk(Array[5], Anchors['A'][0], 358)
    '''

    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)
