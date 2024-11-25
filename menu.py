import pygame
import os
from constants import SCREEN, font, big_font, PLAYER_COLORS, WHITE, BLACK, RED
from questions_database import habilidades, COLOR_DESCRIPTIONS


class Menu:
    def __init__(self):
        # Inicializa a lista de perguntas e configurações
        self.questions = habilidades.copy()  # Copia a lista de perguntas do banco de dados
        self.current_question = None  # Pergunta atual
        self.question_answered = False  # Controle se a pergunta foi respondida
        self.show_question = False  # Controle de exibição da pergunta

    def __init__(self):
        self.player_colors = {
            "Jogador 1": None,
            "Jogador 2": None,
            "Jogador 3": None,
            "Jogador 4": None
        }
        self.player_names = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4"]
        self.selected_player_index = 0
        self.ready = False
        self.background_image = self.load_background()
        
        # carrega os sons
        self.select_sound = self.load_sound('select.mp3')  # som ao selecionar uma cor
        self.start_game_sound = self.load_sound('start.mp3')  # som ao iniciar o jogo

    def load_background(self):
        path = os.path.join('assets', 'images', 'color_selection_background.jpg')
        try:
            image = pygame.image.load(path).convert()
            image = pygame.transform.scale(image, (SCREEN.get_width(), SCREEN.get_height()))
            return image
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo da seleção de cores: {e}")
            return None

    # função generica onde carrega um som a partir de um arquivo ( file_name )
    def load_sound(self, file_name):
        sound_path = os.path.join('assets', 'sounds_effects', file_name)
        try:
            sound = pygame.mixer.Sound(sound_path)
            sound.set_volume(0.60)
            print(f"Som {file_name} carregado.")
            return sound
        except pygame.error as e:
            print(f"Erro ao carregar o som {file_name}: {e}")
            return None

    def draw(self):
        if self.background_image:
            SCREEN.blit(self.background_image, (0, 0))
        else:
            SCREEN.fill(WHITE)
        
        title_text = big_font.render("Seleção de Personagens", True, (0, 0, 0))
        SCREEN.blit(title_text, (SCREEN.get_width()//2 - title_text.get_width()//2, 50))

        instructions = font.render("Use as setas para alternar entre os jogadores.", True, (0, 0, 0))
        SCREEN.blit(instructions, (SCREEN.get_width()//2 - instructions.get_width()//2, 120))

        current_player = self.player_names[self.selected_player_index]
        player_indicator = font.render(f"Selecionando: {current_player}", True, (0, 0, 0))
        SCREEN.blit(player_indicator, (SCREEN.get_width()//2 - player_indicator.get_width()//2, 160))

        y_offset = 250
        box_width = 100
        box_height = 100
        spacing = 150
        num_colors = len(PLAYER_COLORS)
        total_width = num_colors * box_width + (num_colors - 1) * spacing
        x_offset = (SCREEN.get_width() - total_width) // 2  # Centraliza horizontalmente

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for idx, (color_name, color_value) in enumerate(PLAYER_COLORS.items()):
            rect = pygame.Rect(x_offset + idx * (box_width + spacing), y_offset, box_width, box_height)
            pygame.draw.rect(SCREEN, color_value, rect)
           # Verifica se o mouse está sobre o retângulo
            if rect.collidepoint(mouse_x, mouse_y):
                habilidade_texto = COLOR_DESCRIPTIONS.get(color_name, "FOCO desconhecida.")
                self.Menu_habilidade(rect, habilidade_texto)

           
            if self.player_colors[current_player] == color_name:
                pygame.draw.rect(SCREEN, (0, 0, 0), rect, 5)  # Borda mais grossa
            else:
                pygame.draw.rect(SCREEN, (0, 0, 0), rect, 2)  # Borda fina
            # Exibe o nome da cor
            color_text = font.render(color_name, True, (0, 0, 0))
            SCREEN.blit(color_text, (rect.x + rect.width//2 - color_text.get_width()//2, rect.y + rect.height + 10))

        # Exibe as cores selecionadas
        y_positions = [450, 500, 550, 600]
        for i, player_name in enumerate(self.player_names):
            personagem = self.player_colors[player_name] if self.player_colors[player_name] else 'Não selecionada'
            player_text = font.render(f"{player_name} - Personagem: {personagem}", True, (0, 0, 0))
            SCREEN.blit(player_text, (SCREEN.get_width()//2 - player_text.get_width()//2, y_positions[i]))

        # Mensagem para iniciar o jogo
        if all(self.player_colors[player] for player in self.player_names) and not self.ready:
            ready_text = font.render("Pressione ENTER para começar o jogo", True, (0, 0, 0))
            SCREEN.blit(ready_text, (SCREEN.get_width()//2 - ready_text.get_width()//2, SCREEN.get_height() - 100))

        pygame.display.update()

    def fade_in_out(self, fade_duration=150, fade_out=True):
        # Cria a superfície de transição com suporte para alfa (transparência)
        fade_surface = pygame.Surface((SCREEN.get_width(), SCREEN.get_height()))
        fade_surface.fill((255, 255, 255, 0))  # Cor branca
        fade_surface.set_alpha(0 if fade_out else 255)  # Se for fade-in começa transparente, se for fade-out começa branco

        clock = pygame.time.Clock()
        total_steps = fade_duration // 16  # Número de passos do efeito (aproximadamente 60 FPS)
        alpha_step = 255 // total_steps  # Passo de alteração do alpha a cada quadro
        
        alpha = 100 if fade_out else 0  # Se for fade-out, começa branco (255), e fade-in começa transparente (0)

        for _ in range(total_steps):
            fade_surface.set_alpha(alpha)  # Define a transparência da superfície
            SCREEN.blit(fade_surface, (0, 0))  # Aplica a superfície de transição
            pygame.display.update()
            
            # Altera o alpha de acordo com o tipo de fade
            alpha -= alpha_step if fade_out else -alpha_step
            clock.tick(60)  # Mantém a taxa de 60 FPS
        
        # Garantir que a opacidade final seja 0 ou 255
        fade_surface.set_alpha(0 if fade_out else 255)
        SCREEN.blit(fade_surface, (0, 0))  # Aplica o último quadro da transição
        pygame.display.update()  # Atualiza a tela para refletir a transição final

    def handle_event(self, event):
        current_player = self.player_names[self.selected_player_index]
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
                    # Verifica se a cor já está selecionada por outro jogador
                    if color_name not in self.player_colors.values():
                        self.player_colors[current_player] = color_name
                        if self.select_sound:
                            self.select_sound.play()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and all(self.player_colors[player] for player in self.player_names):
                # Realiza o efeito de transição (fade-out) antes de iniciar o jogo
                self.fade_in_out(fade_out=True)
                self.ready = True
                # Toca som de início do jogo
                if self.start_game_sound:
                    self.start_game_sound.play()

            elif event.key == pygame.K_LEFT:
                self.selected_player_index = (self.selected_player_index - 1) % len(self.player_names)
            elif event.key == pygame.K_RIGHT:
                self.selected_player_index = (self.selected_player_index + 1) % len(self.player_names)
    
    
    def Menu_habilidade(self, rect, habilidade):
        """
        Exibe um menu de habilidades ajustado ao retângulo.
        """
        # Calcula o tamanho do texto renderizado
        habilidade_text_surface = font.render(habilidade, True, BLACK)
        text_width, text_height = habilidade_text_surface.get_size()

        # Configura as dimensões do menu baseadas no tamanho do texto
        padding = 20  # Espaçamento extra ao redor do texto
        menu_width = max(text_width + padding, rect.width)  # Largura mínima igual ao retângulo
        menu_height = text_height + padding

        # Calcula a posição do menu com base na posição do retângulo
        menu_x = rect.x
        menu_y = rect.y - menu_height - 10  # Acima do retângulo

        # Ajusta o menu para não ultrapassar os limites da tela
        if menu_x + menu_width > SCREEN.get_width():
            menu_x = SCREEN.get_width() - menu_width
        if menu_y < 0:
            menu_y = rect.y + rect.height + 10  # Move para baixo se ultrapassar o limite superior

        # Cria uma superfície transparente para o menu
        transparent_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        transparent_surface.fill((128, 128, 128, 220))  # Fundo cinza semitransparente

        # Desenha a borda preta
        pygame.draw.rect(transparent_surface, BLACK, transparent_surface.get_rect(), 2, border_radius=10)

        # Adiciona o texto da habilidade no menu
        text_x = (menu_width - text_width) // 2  # Centraliza o texto horizontalmente
        text_y = (menu_height - text_height) // 2  # Centraliza o texto verticalmente
        transparent_surface.blit(habilidade_text_surface, (text_x, text_y))

        # Renderiza o menu na tela principal
        SCREEN.blit(transparent_surface, (menu_x, menu_y))
