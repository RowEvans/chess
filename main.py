import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess")

black = (0, 0, 0)
white = (255, 255, 255)
brown = (176, 135, 98)
tan = (232, 214, 175)
gray = (100,100, 100)

#board dimensions
BOARD_X = 200
BOARD_Y = 100
BOARD_WIDTH = 400
BOARD_HEIGHT = 400
SQUARE_WIDTH = int(BOARD_WIDTH / 8)
SQUARE_HEIGHT = int(BOARD_HEIGHT / 8)

def drawBoard(surface):    
    for i in range(0, BOARD_WIDTH, int(BOARD_WIDTH / 8)):
        for j in range(0, BOARD_HEIGHT, int(BOARD_HEIGHT /8)):
            if ((i + j) % 100) == 0:
                color = tan
            else:
                color = brown

            pygame.draw.rect(surface, color, (BOARD_X + i, BOARD_Y + j, SQUARE_WIDTH, SQUARE_HEIGHT))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    
    drawBoard(screen)

    pygame.display.flip()

pygame.quit()
