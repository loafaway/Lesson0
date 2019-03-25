import pygame
import time

BUF = 20
pygame.init()
surface = pygame.display.set_mode((1024+BUF+1, 512+BUF))
pygame.display.set_caption("Sierpinski Gasket")
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

SHX = 512+BUF//2
SHY = BUF//2
def sier(n, x, y):
  if n == 1:
    surface.set_at((x+SHX, y+SHY), WHITE)
    surface.set_at((x+SHX-1, y+SHY+1), WHITE)
    surface.set_at((x+SHX+1, y+SHY+1), WHITE)
  else:
    sier(n//2, x, y)
    sier(n//2, x-n//2, y+n//2)
    sier(n//2, x+n//2, y+n//2)

surface.fill((0, 100, 100))
sier(512, 0, 0)
pygame.image.save(surface, 'gasket.png')

while (not game_over):
    # 由 pygame 取得事件 (event)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True

    pygame.display.flip()
    pygame.display.update()
