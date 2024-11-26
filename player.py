# player.py

import pygame
from constants import SCREEN, BLACK

class Player:
    def __init__(self, board, name, color):
        self.board = board
        self.position = 0
        self.name = name
        self.color = color

    def move(self, steps):
        self.position += steps 
        if self.position >= len(self.board.board_positions):
            self.position = self.position % len(self.board.board_positions)
            return True  # Completou uma volta
        return False

    def move_back(self, steps):
        self.position -= steps
        if self.position < 0:
            self.position = 0

    def draw(self):
        if self.position < len(self.board.board_positions):
            square = self.board.board_positions[self.position]
            square_size = self.board.square_size
            # Desenha um círculo com uma borda para destacar o jogador
            pygame.draw.circle(SCREEN, self.color, (square.x + square_size//2, square.y + square_size//2), 30)
            pygame.draw.circle(SCREEN, BLACK, (square.x + square_size//2, square.y + square_size//2), 30, 2)  # Borda preta
