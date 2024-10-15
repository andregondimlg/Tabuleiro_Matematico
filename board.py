import pygame
import os
from constants import SCREEN, font, BLUE, RED, GREEN, GRAY

class Board:
    def __init__(self, x_start=50, y_start=50, square_size=70, squares_per_side=13):
        self.square_size = square_size
        self.squares_per_side = squares_per_side
        self.x_start = x_start
        self.y_start = y_start
        self.board_positions = []
        self.background_image = self.load_background()
        self.create_board()

    def load_background(self):
        path = os.path.join('assets', 'images', 'board_background.jpg')
        try:
            image = pygame.image.load(path).convert()
            board_width = self.square_size * (self.squares_per_side - 1)
            board_height = self.square_size * (self.squares_per_side - 1)
            image = pygame.transform.scale(image, (board_width, board_height))
            return image
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo do tabuleiro: {e}")
            return None

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
        if self.background_image:
            SCREEN.blit(self.background_image, (self.x_start, self.y_start))
        else:
            pygame.draw.rect(SCREEN, GRAY, (self.x_start, self.y_start, self.square_size * (self.squares_per_side -1), self.square_size * (self.squares_per_side -1)))

        cores = [BLUE, RED, GREEN, GRAY]
        for idx, square in enumerate(self.board_positions):
            cor = cores[(idx // 12) % 4]
            pygame.draw.rect(SCREEN, cor, square)
            pos_text = font.render(str(idx+1), True, (255, 255, 255))
            SCREEN.blit(pos_text, (square.x + square.width//2 - pos_text.get_width()//2,
                                   square.y + square.height//2 - pos_text.get_height()//2))
