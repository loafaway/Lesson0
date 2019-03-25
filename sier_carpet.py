import pygame
import time

MAXN = 729
BUF = 0
pygame.init()
surface = pygame.display.set_mode((MAXN+BUF, MAXN+BUF))
pygame.display.set_caption("Sierpinski Carpet")
game_over = False

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
fontObj.set_bold(True)
textSurfaceObj = fontObj.render('Hello, World!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
catx=10
caty=10

SHX = BUF//2
SHY = BUF//2

def carpet(n, x, y):
  if n > 1:
    m = n // 3
    for i in range(m):
       for j in range(m):
         surface.set_at((x+m+SHX+i, y+m+SHY+j), WHITE)
    carpet(m, x, y); carpet(m, x+m, y); carpet(m, x+2*m, y)
    carpet(m, x, y+m); carpet(m, x+2*m, y+m)
    carpet(m, x, y+2*m); carpet(m, x+m, y+2*m); carpet(m, x+2*m, y+2*m)

surface.fill((0, 100, 100))
carpet(MAXN, 0, 0)

while (not game_over):
    # 由 pygame 取得事件 (event)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True

    pygame.display.flip()
    pygame.display.update()
