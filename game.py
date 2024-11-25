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
        self.in_player_count_screen = False
        self.current_player_index = 0
        self.message = ""
        self.menu = Menu()
        self.menu_background = self.load_menu_background()
        self.game_background = self.load_game_background()
        self.player_count = 0

        pygame.mixer.init()  # Inicializa o mixer de som

        # Carrega sons
        self.background_sound = self.load_sound('sounds_effects/fall.mp3', background=True)
        self.keypress_sound = self.load_sound('sounds_effects/start.mp3')

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
        path = os.path.join('assets', 'images', 'board_background.png')
        try:
            image = pygame.image.load(path).convert()
            image = pygame.transform.scale(image, (SCREEN.get_width(), SCREEN.get_height()))
            return image
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo do jogo: {e}")
            return None

    def load_sound(self, file_path, background=False):
        sound_path = os.path.join('assets', file_path)
        try:
            if background:
                pygame.mixer.music.load(sound_path)
                pygame.mixer.music.set_volume(0.75)
                pygame.mixer.music.play(loops=-1, start=0.0)  # Toca em loop
                return True
            else:
                sound = pygame.mixer.Sound(sound_path)
                sound.set_volume(0.60)
                return sound
        except pygame.error as e:
            print(f"Erro ao carregar som '{file_path}': {e}")
            return None

    def draw_text_centered(self, surface, text, font, rect, color):
        """
        Desenha um texto centralizado dentro de um retângulo.
        """
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + " " + word if current_line else word
            if font.size(test_line)[0] <= rect.width - 20:  # Margem de 20px
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        total_text_height = sum(font.size(line)[1] for line in lines)
        y_offset = rect.y + (rect.height - total_text_height) // 2

        for line in lines:
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect(center=(rect.x + rect.width // 2, y_offset))
            surface.blit(text_surface, text_rect)
            y_offset += font.size(line)[1]


    def show_message(self, text, duration=2000):
        window_width, window_height = 720, 80
        window_x = (SCREEN.get_width() - window_width) // 2
        window_y = SCREEN.get_height() - window_height - 150  # posição inferior da janela

        # Criação da superfície de mensagem com bordas arredondadas
        message_surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA)
        pygame.draw.rect(
            message_surface,
            (0, 0, 0, 180),  # Fundo semi-transparente
            (0, 0, window_width, window_height),
            border_radius=25
        )

        # Divide o texto em linhas para caber na janela
        message_font = pygame.font.Font(None, 36)
        words = text.split(" ")
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + " " + word if current_line else word
            if message_font.size(test_line)[0] <= window_width - 20:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        # Calcular a posição inicial para centralizar verticalmente
        total_text_height = sum(message_font.size(line)[1] for line in lines)
        y_offset = (window_height - total_text_height) // 2  # Centraliza verticalmente

        # Renderiza as linhas na superfície
        for line in lines:
            text_rendered = message_font.render(line, True, WHITE)
            text_rect = text_rendered.get_rect(center=(window_width // 2, y_offset))
            message_surface.blit(text_rendered, text_rect)
            y_offset += message_font.size(line)[1]  # Ajusta o deslocamento para a próxima linha

        SCREEN.blit(message_surface, (window_x, window_y))
        pygame.display.update()
        pygame.time.delay(duration)

    def fade_in_out(self, fade_duration=150, fade_out=True):
        fade_surface = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()))
        fade_surface.fill((255, 255, 255))
        clock = pygame.time.Clock()
        total_steps = fade_duration // 16
        alpha_step = 255 // total_steps
        alpha = 100 if fade_out else 0  # Mais suave com valor inicial de 100

        for _ in range(total_steps):
            fade_surface.set_alpha(alpha)
            SCREEN.blit(fade_surface, (0, 0))
            pygame.display.update()
            alpha -= alpha_step if fade_out else -alpha_step
            clock.tick(60)

    def draw_initial_screen(self):
        if self.menu_background:
            SCREEN.blit(self.menu_background, (0, 0))
        else:
            SCREEN.fill(WHITE)
        title_text = big_font.render("Doze Destinos!", True, BLACK)
        instruction_text = font.render("Pressione qualquer tecla para começar.", True, BLACK)
        SCREEN.blit(title_text, (SCREEN.get_width()//2 - title_text.get_width()//2, SCREEN.get_height()//2 - 100))
        SCREEN.blit(instruction_text, (SCREEN.get_width()//2 - instruction_text.get_width()//2, SCREEN.get_height()//2))
        pygame.display.update()

    def draw_instructions(self):
        instructions = [
            f"Vez do {self.current_player().name}",
            "Pressione ESPAÇO para rolar o dado.",
        ]
        margin = 50
        for i, text in enumerate(instructions):
            instruction_text = font.render(text, True, WHITE)
            x = SCREEN.get_width() - instruction_text.get_width() - margin
            y = SCREEN.get_height() - (150 - i * 30)
            SCREEN.blit(instruction_text, (x, y))

    def draw_player_count_screen(self):

         # tela para seleção do número de jogadores.

        SCREEN.fill(WHITE)
        title_text = big_font.render("Selecione o número de jogadores", True, BLACK)
        instruction_text = font.render("Use as teclas 2, 3 ou 4 para selecionar a quantidade de jogadores.", True, BLACK)
        SCREEN.blit(title_text, (SCREEN.get_width()//2 - title_text.get_width()//2, SCREEN.get_height()//2 - 100))
        SCREEN.blit(instruction_text, (SCREEN.get_width()//2 - instruction_text.get_width()//2, SCREEN.get_height()//2))

        pygame.display.update()

    def main_loop(self):
        while self.running:
            if self.in_initial_screen:
                self.draw_initial_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        if self.keypress_sound:
                            self.keypress_sound.play()
                        self.fade_in_out(fade_out=True)
                        self.in_initial_screen = False
                        self.in_player_count_screen = True  # Ir para a tela de número de jogadores
                        self.fade_in_out(fade_out=False)
            elif self.in_player_count_screen:
                self.draw_player_count_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_2, pygame.K_3, pygame.K_4]:
                            self.player_count = int(event.unicode)
                            self.menu.player_names = self.menu.player_names[:self.player_count]  # Ajusta o número de jogadores no menu
                            self.in_player_count_screen = False
                            self.in_menu = True  # Ir para o menu de seleção de personagens
                            if self.keypress_sound:
                                self.keypress_sound.play()
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

                for player in self.players:
                    player.draw()

                self.draw_instructions()
                self.dice.draw_result(self.board, self.message)

                if self.question_manager.show_question and self.question_manager.current_question:
                    self.question_manager.update_time_left()
                    if self.question_manager.is_time_up():
                        self.show_message(f"{self.current_player().name} - Tempo esgotado! Você errou a pergunta.")
                        self.current_player().move_back(self.dice.result)
                        self.question_manager.show_question = False
                        self.question_manager.question_answered = False
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
                                    self.show_message(f"{self.current_player().name} - Resposta correta!")
                                    self.question_manager.show_question = False
                                    self.question_manager.question_answered = False
                                    self.next_player()
                                else:
                                    self.show_message(f"{self.current_player().name} - Resposta incorreta! A resposta correta era: {self.question_manager.current_question['answer']}")
                                    self.current_player().move_back(self.dice.result)
                                    self.question_manager.show_question = False
                                    self.question_manager.question_answered = False
                                    self.next_player()
                        elif event.key == pygame.K_SPACE and not self.dice.rolling and not self.question_manager.show_question:
                            self.dice.result = None
                            self.message = ""
                            draw_funcs = [p.draw for p in self.players] + [self.draw_instructions]
                            result = self.dice.roll_dice_animation(self.board, draw_funcs)
                            if result:
                                self.dice.result = result
                                completed_lap = self.current_player().move(result)
                                if completed_lap:
                                    self.show_message(f"{self.current_player().name} completou uma volta!")
                                if (self.current_player().position + 1) % 1 == 0:
                                    self.question_manager.get_new_question()
                                else:
                                    self.next_player()

            pygame.display.update()
            self.clock.tick(60)

    def start_game(self):
        for player_name in self.menu.player_names:
            color_name = self.menu.player_colors[player_name]
            color = PLAYER_COLORS[color_name]
            self.players.append(Player(self.board, player_name, color, self.board.path_points))

    def current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)


    def habilidades (self):
        for Player_name in self.menu.player_names:
            self.show_message(f"{self.current_player().name}precione 5 para usar a habilidade")