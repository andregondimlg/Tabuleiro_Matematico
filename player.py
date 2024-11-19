# player.py

import pygame
from constants import SCREEN, BLACK

class Player:
    def __init__(self, board, name, color, path_points):
        self.board = board
        self.position = 0
        self.name = name
        self.color = color
        self.path_points = path_points  # Armazena a lista de pontos

    def move(self, steps):
        self.position += steps 
        if self.position >= len(self.path_points):
            self.position = self.position % len(self.path_points)
            return True  # Completou uma volta
        return False

    def move_back(self, steps):
        self.position -= steps
        if self.position < 0:
            self.position = 0

    def draw(self):
        if self.position < len(self.path_points):
            square = self.path_points[self.position]
            # Desenha um círculo com uma borda para destacar o jogador
            pygame.draw.circle(SCREEN, self.color, (square["x"], square["y"]), 22)
            pygame.draw.circle(SCREEN, BLACK, (square["x"], square["y"]), 22, 2)  # Borda preta
    