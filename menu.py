# menu.py

import pygame
import os
from constants import SCREEN, font, big_font, PLAYER_COLORS, WHITE

class Menu:
    def __init__(self):
        self.player_colors = {
            "Jogador 1": None,
            "Jogador 2": None
        }
        self.selected_player = "Jogador 1"
        self.ready = False
        self.background_image = self.load_background()

    def load_background(self):
        path = os.path.join('assets', 'images', 'color_selection_background.jpg')
        try:
            image = pygame.image.load(path).convert()
            image = pygame.transform.scale(image, (SCREEN.get_width(), SCREEN.get_height()))
            return image
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo da seleção de cores: {e}")
            return None

    def draw(self):
        if self.background_image:
            SCREEN.blit(self.background_image, (0, 0))
        else:
            SCREEN.fill(WHITE)
        
        # Título
        title_text = big_font.render("Seleção de Cores", True, (0, 0, 0))
        SCREEN.blit(title_text, (SCREEN.get_width()//2 - title_text.get_width()//2, 50))

        # Instruções
        instructions = font.render("Use as setas para alternar entre os jogadores.", True, (0, 0, 0))
        SCREEN.blit(instructions, (SCREEN.get_width()//2 - instructions.get_width()//2, 120))

        # Indicação do jogador atual
        player_indicator = font.render(f"Selecionando: {self.selected_player}", True, (0, 0, 0))
        SCREEN.blit(player_indicator, (SCREEN.get_width()//2 - player_indicator.get_width()//2, 160))

        # Opções de cores disponíveis
        y_offset = 250
        box_width = 100
        box_height = 100
        spacing = 150
        num_colors = len(PLAYER_COLORS)
        total_width = num_colors * box_width + (num_colors - 1) * spacing
        x_offset = (SCREEN.get_width() - total_width) // 2  # Centraliza horizontalmente

        for idx, (color_name, color_value) in enumerate(PLAYER_COLORS.items()):
            rect = pygame.Rect(x_offset + idx * (box_width + spacing), y_offset, box_width, box_height)
            pygame.draw.rect(SCREEN, color_value, rect)
            # Desenha borda se a cor estiver selecionada pelo jogador atual
            if self.player_colors[self.selected_player] == color_name:
                pygame.draw.rect(SCREEN, (0, 0, 0), rect, 5)  # Borda mais grossa
            else:
                pygame.draw.rect(SCREEN, (0, 0, 0), rect, 2)  # Borda fina
            # Exibe o nome da cor
            color_text = font.render(color_name, True, (0, 0, 0))
            SCREEN.blit(color_text, (rect.x + rect.width//2 - color_text.get_width()//2, rect.y + rect.height + 10))

        # Exibe as cores selecionadas
        player1_text = font.render(f"Jogador 1 - Cor: {self.player_colors['Jogador 1'] if self.player_colors['Jogador 1'] else 'Não selecionada'}", True, (0, 0, 0))
        SCREEN.blit(player1_text, (SCREEN.get_width()//2 - player1_text.get_width()//2, 450))

        player2_text = font.render(f"Jogador 2 - Cor: {self.player_colors['Jogador 2'] if self.player_colors['Jogador 2'] else 'Não selecionada'}", True, (0, 0, 0))
        SCREEN.blit(player2_text, (SCREEN.get_width()//2 - player2_text.get_width()//2, 500))

        # Mensagem para iniciar o jogo
        if self.player_colors["Jogador 1"] and self.player_colors["Jogador 2"] and not self.ready:
            ready_text = font.render("Pressione ENTER para começar o jogo", True, (0, 0, 0))
            SCREEN.blit(ready_text, (SCREEN.get_width()//2 - ready_text.get_width()//2, SCREEN.get_height() - 100))

        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            y_offset = 250
            box_width = 100
            box_height = 100
            spacing = 150
            num_colors = len(PLAYER_COLORS)
            total_width = num_colors * box_width + (num_colors - 1) * spacing
            x_offset = (SCREEN.get_width() - total_width) // 2  # Centraliza horizontalmente

            for idx, color_name in enumerate(PLAYER_COLORS.keys()):
                rect = pygame.Rect(x_offset + idx * (box_width + spacing), y_offset, box_width, box_height)
                if rect.collidepoint(mouse_x, mouse_y):
                    # Verifica se a cor já está selecionada pelo outro jogador
                    other_player = "Jogador 1" if self.selected_player == "Jogador 2" else "Jogador 2"
                    if self.player_colors[other_player] != color_name:
                        self.player_colors[self.selected_player] = color_name

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.player_colors["Jogador 1"] and self.player_colors["Jogador 2"]:
                self.ready = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # Alterna entre os jogadores
                self.selected_player = "Jogador 1" if self.selected_player == "Jogador 2" else "Jogador 2"
