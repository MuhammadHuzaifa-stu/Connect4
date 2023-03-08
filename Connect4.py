import numpy as np
import pygame
import math

rows = 6
cols = 7

blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

def create_board():
    board = np.zeros((rows,cols))
    return board

board = create_board()

def valid(board, col):
    return board[0][col] == 0
        
def valid_posi(board, col):
    for i in range(rows-1,-1,-1):
        if board[i][col] == 0:
            return i
        
def place_piece(board, r, col, piece):
    board[r][col] = piece

def winning(board, piece):
    
    for i in range(cols-3):     #For horizontal pieces
        for j in range(rows):
            if board[j][i]  == piece and board[j][i+1]  == piece and board[j][i+2]  == piece and board[j][i+3]  == piece:
                return True
            
    for i in range(cols):     #For vertical pieces
        for j in range(rows-3):
            if board[j][i]  == piece and board[j+1][i]  == piece and board[j+2][i]  == piece and board[j+3][i]  == piece:
                return True
    
    for i in range(cols-3):     #For slopes pieces
        for j in range(rows-3):
            if board[j][i]  == piece and board[j+1][i+1]  == piece and board[j+2][i+2]  == piece and board[j+3][i+3]  == piece:
                return True
    
    for i in range(cols-3):     #For slopes pieces
        for j in range(3,rows):
            if board[j][i]  == piece and board[j-1][i+1]  == piece and board[j-2][i+2]  == piece and board[j-3][i+3]  == piece:
                return True
    
def draw_board(board):
    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(screen, blue, (i*square, j*square+square, square, square))
            if board[j][i] == 0:
                pygame.draw.circle(screen, black, (int(i*square+square/2), int(j*square+square+square/2)), radius)
            elif board[j][i] == 1:
                pygame.draw.circle(screen, red, (int(i*square+square/2), int(j*square+square+square/2)), radius)
            else:
                pygame.draw.circle(screen, green, (int(i*square+square/2), int(j*square+square+square/2)), radius)
    pygame.display.update()    

game_over = False
turn = 0
pygame.init()
square = 100
width = cols*square
height = (rows+1)*square
size = (width, height)
radius = int(square/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)

pygame.display.update()
font = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:   
            pygame.draw.rect(screen, black, (0,0, width, square))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red, (posx, int(square/2)), radius)
            else:
                pygame.draw.circle(screen, green, (posx, int(square/2)), radius)
        
        pygame.display.update()        
        if event.type == pygame.MOUSEBUTTONDOWN:   
            pygame.draw.rect(screen, black, (0,0, width, square))
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/square))
                if valid(board, col):
                    x = valid_posi(board, col)
                    place_piece(board, x, col, 1)
                    if winning(board, 1):
                        label = font.render("Player 1 wins!!", 1, red)
                        screen.blit(label, (30,10))
                        game_over = True
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/square))
                if valid(board, col):
                    x = valid_posi(board, col)
                    place_piece(board, x, col, 2)
                    if winning(board, 2):
                        label = font.render("Player 2 wins!!", 1, green)
                        screen.blit(label, (30,10))
                        game_over = True
            draw_board(board)     
            turn += 1
            turn %= 2
            if game_over:
                pygame.time.wait(2000)
print("\n\t\tGAME OVER")
    