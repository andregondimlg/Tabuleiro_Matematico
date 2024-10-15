# question.py

import pygame
import random
from constants import SCREEN, GRAY, BLACK, RED, font
from questions_database import questions_list

class QuestionManager:
    def __init__(self):
        self.questions = questions_list.copy()
        self.current_question = None
        self.question_answered = False
        self.show_question = False
        self.question_start_time = None
        self.time_limit = 30  # segundos
        self.time_left = self.time_limit

    def get_new_question(self):
        if self.questions:
            self.current_question = random.choice(self.questions)
            self.questions.remove(self.current_question)
            self.question_answered = False
            self.show_question = True
            self.question_start_time = pygame.time.get_ticks()
            self.time_left = self.time_limit
        else:
            self.current_question = None
            self.show_question = False

    def update_time_left(self):
        elapsed_time = (pygame.time.get_ticks() - self.question_start_time) / 1000  # Em segundos
        self.time_left = self.time_limit - elapsed_time

    def is_time_up(self):
        return self.time_left <= 0

    def draw_question_interface(self):
        # Área da interface de perguntas
        WIDTH, HEIGHT = SCREEN.get_size()
        interface_width = WIDTH // 3  # Ajuste a largura da interface aqui
        interface_height = HEIGHT // 2  # Ajuste a altura da interface aqui
        interface_x = WIDTH - interface_width - 50  # Margem direita de 50 pixels
        interface_y = (HEIGHT - interface_height) // 2  # Centraliza verticalmente

        interface_rect = pygame.Rect(interface_x, interface_y, interface_width, interface_height)
        pygame.draw.rect(SCREEN, GRAY, interface_rect)
        pygame.draw.rect(SCREEN, BLACK, interface_rect, 2)

        question = self.current_question
        if question is None:
            return

        # Exibe a pergunta
        question_text = font.render(question["question"], True, BLACK)
        SCREEN.blit(question_text, (interface_rect.x + 20, interface_rect.y + 20))

        # Exibe as opções
        for i, option in enumerate(question["options"]):
            option_text = font.render(f"{i+1}. {option}", True, BLACK)
            SCREEN.blit(option_text, (interface_rect.x + 40, interface_rect.y + 80 + i * 40))

        # Exibe o cronômetro
        if self.time_left <= 10:
            time_color = RED
        else:
            time_color = BLACK
        timer_text = font.render(f"Tempo restante: {int(self.time_left)}s", True, time_color)
        SCREEN.blit(timer_text, (interface_rect.x + 20, interface_rect.y + interface_height - 90))

        # Instrução para responder
        instruction_text = font.render("Pressione o número correspondente à resposta.", True, BLACK)
        SCREEN.blit(instruction_text, (interface_rect.x + 20, interface_rect.y + interface_height - 60))

    def handle_event(self, event):
        selected_option = None
        if event.key in [pygame.K_1, pygame.K_KP1]:
            selected_option = 0
        elif event.key in [pygame.K_2, pygame.K_KP2]:
            selected_option = 1
        elif event.key in [pygame.K_3, pygame.K_KP3]:
            selected_option = 2
        elif event.key in [pygame.K_4, pygame.K_KP4]:
            selected_option = 3

        return selected_option
