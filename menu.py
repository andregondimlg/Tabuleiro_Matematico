# menu.py

import pygame
from constants import SCREEN, WHITE, BLACK, font, big_font, PLAYER_COLORS

class Menu:
    def __init__(self):
        self.player_colors = {
            "Jogador 1": None,
            "Jogador 2": None
        }
        self.selected_player = "Jogador 1"
        self.ready = False

    def draw(self):
        SCREEN.fill(WHITE)
        title_text = big_font.render("Seleção de Cores", True, BLACK)
        SCREEN.blit(title_text, (SCREEN.get_width()//2 - title_text.get_width()//2, 50))

        instructions = font.render("Use as setas para alternar entre os jogadores.", True, BLACK)
        SCREEN.blit(instructions, (SCREEN.get_width()//2 - instructions.get_width()//2, 120))

        
        player_indicator = font.render(f"Selecionando: {self.selected_player}", True, BLACK)
        SCREEN.blit(player_indicator, (SCREEN.get_width()//2 - player_indicator.get_width()//2, 160))

        
        y_offset = 250
        x_offset = 200
        spacing = 150
        for idx, color_name in enumerate(PLAYER_COLORS.keys()):
            color_value = PLAYER_COLORS[color_name]
            rect = pygame.Rect(x_offset + idx * spacing, y_offset, 100, 100)
            pygame.draw.rect(SCREEN, color_value, rect)
            
            if self.player_colors[self.selected_player] == color_name:
                pygame.draw.rect(SCREEN, BLACK, rect, 5)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect, 2)
            
            color_text = font.render(color_name, True, BLACK)
            SCREEN.blit(color_text, (rect.x + rect.width//2 - color_text.get_width()//2, rect.y + rect.height + 10))

       
        player1_text = font.render(f"Jogador 1 - Cor: {self.player_colors['Jogador 1'] if self.player_colors['Jogador 1'] else 'Não selecionada'}", True, BLACK)
        SCREEN.blit(player1_text, (SCREEN.get_width()//2 - player1_text.get_width()//2, 450))

        player2_text = font.render(f"Jogador 2 - Cor: {self.player_colors['Jogador 2'] if self.player_colors['Jogador 2'] else 'Não selecionada'}", True, BLACK)
        SCREEN.blit(player2_text, (SCREEN.get_width()//2 - player2_text.get_width()//2, 500))

        if self.player_colors["Jogador 1"] and self.player_colors["Jogador 2"] and not self.ready:
            ready_text = font.render("Pressione ENTER para começar o jogo", True, BLACK)
            SCREEN.blit(ready_text, (SCREEN.get_width()//2 - ready_text.get_width()//2, SCREEN.get_height() - 100))

        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            y_offset = 250
            x_offset = 200
            spacing = 150
            for idx, color_name in enumerate(PLAYER_COLORS.keys()):
                rect = pygame.Rect(x_offset + idx * spacing, y_offset, 100, 100)
                if rect.collidepoint(mouse_x, mouse_y):
                    
                    other_player = "Jogador 1" if self.selected_player == "Jogador 2" else "Jogador 2"
                    if self.player_colors[other_player] != color_name:
                        self.player_colors[self.selected_player] = color_name

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.player_colors["Jogador 1"] and self.player_colors["Jogador 2"]:
                self.ready = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                
                self.selected_player = "Jogador 1" if self.selected_player == "Jogador 2" else "Jogador 2"
