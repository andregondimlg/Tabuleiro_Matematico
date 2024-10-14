import pygame
from constants import SCREEN

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
            return True 
        return False

    def move_back(self, steps):
        self.position -= steps
        if self.position < 0:
            self.position = 0

    def draw(self):
        if self.position < len(self.board.board_positions):
            square = self.board.board_positions[self.position]
            square_size = self.board.square_size
            pygame.draw.circle(SCREEN, self.color, (square.x + square_size//2, square.y + square_size//2), 30)
