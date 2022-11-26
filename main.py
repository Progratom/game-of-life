import copy
import pygame

pygame.init()
SIZE = 30
CELL = 20
screen = pygame.display.set_mode(((SIZE+2)*(2+CELL)+100, (SIZE+2)*(2+CELL)+100))
clock = pygame.time.Clock()
GREY = (128, 128, 128)
DARK_GREY = (50, 50, 50)
BLUE = (0, 0, 225)

def generate_board():

    board_line = 0  
    for boardY in matrix:  
        board_col = 0  
        for boardX in boardY: 
            if board_line == 0 or board_line == (len(boardY)-1):
                pygame.draw.rect(screen, DARK_GREY, pygame.Rect(board_col * (CELL+2), board_line * (CELL+2), CELL, CELL))
            elif board_col == 0 or board_col == (len(boardY)-1):
                pygame.draw.rect(screen, DARK_GREY, pygame.Rect(board_col * (SIZE+2), board_line * (CELL+2), CELL, CELL))
            elif boardX == 0:
                pygame.draw.rect(screen, GREY, pygame.Rect(board_col * (CELL+2), board_line * (CELL+2), CELL, CELL))
            elif boardX == 1:
                pygame.draw.rect(screen, BLUE, pygame.Rect(board_col * (CELL+2), board_line * (CELL+2), CELL, CELL))
            board_col = board_col + 1 
        board_line = board_line + 1  

    pygame.display.flip()


def createMatrix(size):
    line = []
    for i in range(size+2):
        line.append(0)
    matrix = []
    for i in range(size+2):
        matrix.append(line.copy())
    return matrix

def priMat(matrix, size):
    for i in range(size):
        for j in range(size-1):
            print(str(matrix[i+1][j+1]) + " ", end = ' ')
        print(str(matrix[i+1][size]) + " ")
    print()

def find_neighbour(y, x, matrix):
    arr = [-1, 0, 1]
    neig = 0

    for i in arr:
        for j in arr:
            #print(str(i) + " " + str(j))
            if matrix[y+i][x+j] == 1:
                if i == 0 and j == 0:
                    pass
                else:
                    neig += 1
    return neig

def find_ne(y, x, matice):
    count = 0
    count += matice[y - 1][x - 1];
    count += matice[y - 1][x];
    count += matice[y - 1][x + 1];
    count += matice[y][x - 1];
    count += matice[y][x + 1];
    count += matice[y + 1][x - 1];
    count += matice[y + 1][x];
    count += matice[y + 1][x + 1];
    
    return(count)



def change(matrix, pomat, size):
    for i in range(size):
        for j in range(size):
            neig = find_neighbour(i+1, j+1, matrix)
            if matrix[i+1][j+1] == 0:
                if neig == 3:
                    pomat[i+1][j+1] = 1
                else:
                    pomat[i+1][j+1] = 0
            elif matrix[i+1][j+1] == 1:
                if (neig == 2 or neig == 3):
                    pomat[i+1][j+1] = 1
                else:
                    pomat[i+1][j+1] = 0



    return(pomat)



def mouse():
    end = True
    while end:
        generate_board()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return("l", pygame.mouse.get_pos())
                elif event.button == 3:
                    return("r", pygame.mouse.get_pos())
                end = False
            elif event.type == pygame.QUIT:
                pygame.quit() 
        clock.tick(30)




matrix = createMatrix(SIZE)
poMat = copy.deepcopy(matrix)

end = True
while end:
    typ, pozice = mouse()
    if typ == "r":
        end = False
    if typ == "l":
        y, x = pozice
        for i in range(SIZE+2):
            if x > i*(CELL+2) and x < (i+1)*(CELL+2):
                line = i
        for i in range(SIZE+2):
            if y > i*(CELL+2) and y < (i+1)*(CELL+2):
                col = i
        matrix[line][col] = 1


max_gen = 100
gen = 0
while gen != max_gen:
    gen += 1
    poMat = change(matrix, poMat, SIZE)
    matrix = copy.deepcopy(poMat)
    #priMat(matrix, SIZE)
    generate_board()
    clock.tick(10)



