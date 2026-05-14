import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess")

font = pygame.font.Font(None, 16)

#ranks
letters = "abcdefgh"

#colors
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
    
    #add ranks
    for i in range(8):
        if (i % 2) == 0:
            color = tan
        else:
            color = brown

        text = font.render(f"{letters[i]}", True, color)
        text_rect = text.get_rect(center=((BOARD_X + 8 + (i * 50)), (BOARD_Y + BOARD_HEIGHT - 8)))
        surface.blit(text, text_rect)

        text2 = font.render(f"{i + 1}", True, color)
        text2_rect = text2.get_rect(center=((BOARD_X + 8), (BOARD_Y + BOARD_HEIGHT - ((i + 1) * 50) + 8)))
        surface.blit(text2, text2_rect)

#pieces
blackBoard = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]

whiteBoard = [
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ]
piece_font = pygame.font.Font(None, 24)

def drawPieces(surface):
    for i in range(8):
        for j in range(8):
            if blackBoard[i][j] == '-':
                continue
            text = piece_font.render(f"{blackBoard[i][j]}", True, black)
            text_rect = text.get_rect(center=(BOARD_X + 25 + (j * 50), (BOARD_Y + 25 + (i * 50))))
            surface.blit(text, text_rect)

    for i in range(8):
        for j in range(8):
            if whiteBoard[i][j] == '-':
                continue
            text = piece_font.render(f"{whiteBoard[i][j]}", True, white)
            text_rect = text.get_rect(center=((BOARD_X + 25 + (j * 50)), (BOARD_Y + 25 + (i * 50))))
            surface.blit(text, text_rect)
    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(black)
    
    drawBoard(screen)
    drawPieces(screen)

    pygame.display.flip()

pygame.quit()
