import pygame
import sys
import os
from constants import SCREEN, WHITE, BLACK, font, big_font
from board import Board
from player import Player
from dice import Dice
from question import QuestionManager
from menu import Menu
from constants import PLAYER_COLORS

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.dice = Dice()
        self.question_manager = QuestionManager()
        self.clock = pygame.time.Clock()
        self.running = True
        self.in_initial_screen = True
        self.in_menu = False
        self.current_player_index = 0
        self.message = ""
        self.menu = Menu()
        self.menu_background = self.load_menu_background()
        self.game_background = self.load_game_background()

    def load_menu_background(self):
        path = os.path.join('assets', 'images', 'menu_background.jpg')
        try:
            image = pygame.image.load(path).convert()
            image = pygame.transform.scale(image, (SCREEN.get_width(), SCREEN.get_height()))
            return image
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo do menu: {e}")
            return None

    def load_game_background(self):
        path = os.path.join('assets', 'images', 'game_background.jpg')
        try:
            image = pygame.image.load(path).convert()
            image = pygame.transform.scale(image, (SCREEN.get_width(), SCREEN.get_height()))
            return image
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo do jogo: {e}")
            return None

    def draw_initial_screen(self):
        if self.menu_background:
            SCREEN.blit(self.menu_background, (0, 0))
        else:
            SCREEN.fill(WHITE)
        title_text = big_font.render("Bem-vindo ao Jogo de Tabuleiro Matemático!", True, BLACK)
        instruction_text = font.render("Pressione qualquer tecla para começar.", True, BLACK)
        SCREEN.blit(title_text, (SCREEN.get_width()//2 - title_text.get_width()//2, SCREEN.get_height()//2 - 100))
        SCREEN.blit(instruction_text, (SCREEN.get_width()//2 - instruction_text.get_width()//2, SCREEN.get_height()//2))
        pygame.display.update()

    def draw_instructions(self):
        instructions = [
            f"Vez do {self.current_player().name}",
            "Pressione ESPAÇO para rolar o dado.",
            "Objetivo: Chegar ao final do tabuleiro."
        ]
        margin = 50
        for i, text in enumerate(instructions):
            instruction_text = font.render(text, True, WHITE)
            x = SCREEN.get_width() - instruction_text.get_width() - margin
            y = SCREEN.get_height() - (150 - i * 30)
            SCREEN.blit(instruction_text, (x, y))

    def main_loop(self):
        while self.running:
            if self.in_initial_screen:
                self.draw_initial_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        self.in_initial_screen = False
                        self.in_menu = True
            elif self.in_menu:
                self.menu.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    else:
                        self.menu.handle_event(event)
                        if self.menu.ready:
                            self.start_game()
                            self.in_menu = False
            else:
                if self.game_background:
                    SCREEN.blit(self.game_background, (0, 0))
                else:
                    SCREEN.fill(WHITE)
                
                self.board.draw()
                
                for player in self.players:
                    player.draw()
                
                self.draw_instructions()
                
                self.dice.draw_result(self.board, self.message)

                if self.question_manager.show_question and self.question_manager.current_question:
                    self.question_manager.update_time_left()
                    if self.question_manager.is_time_up():
                        self.message = f"{self.current_player().name} - Tempo esgotado! Você errou a pergunta."
                        self.current_player().move_back(result)
                        self.question_manager.show_question = False
                        self.question_manager.question_answered = False  #Reseta o estado da pergunta
                        self.next_player()
                    else:
                        self.question_manager.draw_question_interface()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if self.question_manager.show_question and not self.question_manager.question_answered:
                            selected_option = self.question_manager.handle_event(event)
                            if selected_option is not None:
                                self.question_manager.question_answered = True
                                selected_answer = self.question_manager.current_question["options"][selected_option]
                                if selected_answer == self.question_manager.current_question["answer"]:
                                    self.message = f"{self.current_player().name} - Resposta correta!"
                                    self.question_manager.show_question = False
                                    self.question_manager.question_answered = False  # Reseta o estado
                                    self.next_player()
                                else:
                                    self.message = f"{self.current_player().name} - Resposta incorreta! A resposta correta era: {self.question_manager.current_question['answer']}"
                                    self.current_player().move_back(result)
                                    self.question_manager.show_question = False
                                    self.question_manager.question_answered = False  # Reseta o estado
                                    self.next_player()
                        elif event.key == pygame.K_SPACE and not self.dice.rolling and not self.question_manager.show_question:
                            self.dice.result = None
                            self.message = ""
                            draw_funcs = [self.board.draw] + [p.draw for p in self.players] + [self.draw_instructions]
                            result = self.dice.roll_dice_animation(self.board, draw_funcs)
                            if result:
                                self.dice.result = result
                                completed_lap = self.current_player().move(result)
                                if completed_lap:
                                    self.message = f"{self.current_player().name} completou uma volta!"
                                else:
                                    self.message = ""
                                if (self.current_player().position + 1) % 5 == 0:
                                    self.question_manager.get_new_question()
                                    if not self.question_manager.show_question:
                                        self.message = "Sem mais perguntas disponíveis."
                                else:
                                    self.next_player()

                pygame.display.update()
                self.clock.tick(60)

    def start_game(self):
        color1 = PLAYER_COLORS[self.menu.player_colors["Jogador 1"]]
        color2 = PLAYER_COLORS[self.menu.player_colors["Jogador 2"]]
        self.players.append(Player(self.board, "Jogador 1", color1))
        self.players.append(Player(self.board, "Jogador 2", color2))

    def current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def quit(self):
        pygame.quit()
        sys.exit()
