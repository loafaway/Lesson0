import pygame
import time

pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("The Tower of Hanoi Demo!")
game_over = False

FPS = 3
fpsClock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)

Anchors = {'A': (93, 358), 'B': (293, 358), 'C': (493, 358)}

#fontObj = pygame.font.Font('freesansbold.ttf', 24)
fontObj = pygame.font.Font(r'c:\windows\fonts\mingliu.ttc', 28)
fontObj.set_bold(True)
fontObj.set_underline(True)
fontObj2 = pygame.font.Font(r'c:\windows\fonts\mingliu.ttc', 24)

fontObj1 = pygame.font.Font('freesansbold.ttf', 14)

#'''
textSurfaceObj = fontObj2.render('遞迴之例示：六層河內塔', True, WHITE, BLUE)
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

XY = [(93, 213), (93, 203), (93, 193), (93, 183), (93, 173), (93, 163), (93, 153),
  (93, 143), (93, 133), (93, 123), (93, 113), (93, 103), (93, 93), (93, 83), (93, 73),
  (143, 73), (193, 73), (243, 73), (293, 73), (343, 73), (393, 73), (443, 73),
  (493, 73), (493, 108), (493, 133), (493, 158),
  (493, 188), (493, 218), (493, 248), (493, 278), (493, 308), (493, 338), (493, 358)]

catx=10
caty=10
X = 10
Y = 10
idx = 0
De = 0

while (not game_over):
    # 由 pygame 取得事件 (event)
    surface.fill((31, 255, 231))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            idx = 0
            De = 2
            #X, Y = 493, 358
    '''
    textRectObj.center = (110+textSurfaceObj.get_width//2,     10+textSurfaceObj.get_height//2)
    '''
    textRectObj.center = (132, 12)
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

    pygame.draw.circle(surface, (225, 255, 0), (X-50, Y-30), 15, 2)

    if idx < len(XY):
        X, Y = XY[idx]
        idx += 1

    '''
    textRectObj1.center = (X, Y)
    surface.blit(textSurfaceObj1, textRectObj1)
    '''
    #textsurf, textrect = textSurfaceObj1, textRectObj1
    textsurf, textrect = Array[De]
    textrect.center = (X, Y)
    surface.blit(textsurf, textrect) 

    textRectObj2.center = (93, 242)
    surface.blit(textSurfaceObj2, textRectObj2)
    textRectObj3.center = (93, 271)
    surface.blit(textSurfaceObj3, textRectObj3)
    textRectObj4.center = (93, 300)
    surface.blit(textSurfaceObj4, textRectObj4)
    textRectObj5.center = (93, 329)
    surface.blit(textSurfaceObj5, textRectObj5)
    textRectObj6.center = (93, 358)
    surface.blit(textSurfaceObj6, textRectObj6)

    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)
