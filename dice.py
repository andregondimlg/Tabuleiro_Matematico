import pygame
import random
from constants import SCREEN, big_font, font, GREEN, BLACK, WHITE
from utils import get_board_center

class Dice:
    def __init__(self):
        self.result = None
        self.rolling = False

    def roll_dice_animation(self, board, player_pos, draw_functions):
        self.rolling = True
        roll_start_time = pygame.time.get_ticks()
        animation_duration = 1000  

        while self.rolling:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - roll_start_time

            if elapsed_time >= animation_duration:
                self.rolling = False
                self.result = random.randint(1, 6)
                return self.result
            else:
              
                temp_result = random.randint(1, 6)
                SCREEN.fill(WHITE)
                for func in draw_functions:
                    func()
                
                board_center_x, board_center_y = get_board_center(board)
                temp_text = big_font.render(str(temp_result), True, BLACK)
                SCREEN.blit(temp_text, (board_center_x - temp_text.get_width()//2, board_center_y - temp_text.get_height()//2))
                pygame.display.update()
                pygame.time.delay(100) 

    def draw_result(self, board, message):
        if self.result is not None:
            board_center_x, board_center_y = get_board_center(board)
            dice_text = big_font.render(f"{self.result}", True, GREEN)
            SCREEN.blit(dice_text, (board_center_x - dice_text.get_width()//2, board_center_y - dice_text.get_height()//2))

            if message:
                message_text = font.render(message, True, BLACK)
                SCREEN.blit(message_text, (board_center_x - message_text.get_width()//2, board_center_y + dice_text.get_height()//2))
