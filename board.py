import pygame
from constants import SCREEN, BLUE, WHITE, RED, GREEN, GRAY,font

class Board:
    # define, tamanho, quantidade de quadrados e onde vão ser criados 
    def __init__(self, x_start=50, y_start=50, square_size=60, squares_per_side=13):
        self.square_size = square_size # tamanho da quadrado 
        self.squares_per_side = squares_per_side #numero de quadrados por lado 
        self.x_start = x_start 
        self.y_start = y_start
        self.board_positions = []
        self.create_board() #cria os quadrados 

    def create_board(self):
        self.board_positions.clear()
        board_width = self.square_size * (self.squares_per_side - 1)
        board_height = self.square_size * (self.squares_per_side - 1)

      
        for i in range(self.squares_per_side):
            x = self.x_start + i * self.square_size
            y = self.y_start
            rect = pygame.Rect(x, y, self.square_size, self.square_size)
            self.board_positions.append(rect)

        
        for i in range(1, self.squares_per_side):
            x = self.x_start + board_width
            y = self.y_start + i * self.square_size
            rect = pygame.Rect(x, y, self.square_size, self.square_size)
            self.board_positions.append(rect)

        
        for i in range(1, self.squares_per_side):
            x = self.x_start + board_width - i * self.square_size
            y = self.y_start + board_height
            rect = pygame.Rect(x, y, self.square_size, self.square_size)
            self.board_positions.append(rect)

    
        for i in range(1, self.squares_per_side -1):
            x = self.x_start
            y = self.y_start + board_height - i * self.square_size
            rect = pygame.Rect(x, y, self.square_size, self.square_size)
            self.board_positions.append(rect)

    def draw(self):
        cores = [BLUE,RED, GREEN, GRAY]
        for idx, square in enumerate(self.board_positions):
            
            cor = cores[(idx // 12) % 4]
                
            pygame.draw.rect(SCREEN, cor, square)
            pos_text = font.render(str(idx+1), True, WHITE)
            SCREEN.blit(pos_text, (square.x + square.width//2 - pos_text.get_width()//2,
                                    square.y + square.height//2 - pos_text.get_height()//2))
