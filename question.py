import pygame
import random
from constants import SCREEN, GRAY, BLACK, RED, font
from questions_database import questions_list

class QuestionManager:
    def __init__(self):
        # Inicializa a lista de perguntas e configurações
        self.questions = questions_list.copy()  # Copia a lista de perguntas do banco de dados
        self.current_question = None  # Pergunta atual
        self.question_answered = False  # Controle se a pergunta foi respondida
        self.show_question = False  # Controle de exibição da pergunta
        self.question_start_time = None  # Tempo de início da pergunta
        self.time_limit = 30  # Limite de tempo para responder (em segundos)
        self.time_left = self.time_limit  # Tempo restante

    def get_new_question(self):
        # Seleciona uma nova pergunta aleatoriamente
        if self.questions:
            self.current_question = random.choice(self.questions)  # Escolhe aleatoriamente
            self.questions.remove(self.current_question)  # Remove a pergunta já selecionada
            self.question_answered = False  # Marca que a pergunta ainda não foi respondida
            self.show_question = True  # Habilita a exibição da pergunta
            self.question_start_time = pygame.time.get_ticks()  # Marca o tempo de início
            self.time_left = self.time_limit  # Reseta o tempo restante
        else:
            self.current_question = None  # Se não houver perguntas, não exibe nada
            self.show_question = False

    def update_time_left(self):
        # Atualiza o tempo restante baseado no tempo decorrido
        elapsed_time = (pygame.time.get_ticks() - self.question_start_time) / 1000  # Converte milissegundos em segundos
        self.time_left = self.time_limit - elapsed_time  # Subtrai o tempo decorrido do limite

    def is_time_up(self):
        # Verifica se o tempo acabou
        return self.time_left <= 0

    def draw_question_interface(self):
        # Desenha a interface da pergunta de forma transparente no centro da tela

        # Obtém as dimensões da tela
        WIDTH, HEIGHT = SCREEN.get_size()
        
        # Configura a largura e altura da interface de perguntas
        interface_width = WIDTH // 3  
        interface_height = HEIGHT // 2  

        # Centraliza a interface, calculando a posição baseada no centro da tela
        interface_x = (WIDTH // 2) - (interface_width // 2)  # Centro da tela menos metade da largura da interface
        interface_y = (HEIGHT // 2) - (interface_height // 2)  # Centro da tela menos metade da altura da interface

        # Cria uma superfície com canal alfa para transparência
        transparent_surface = pygame.Surface((interface_width, interface_height), pygame.SRCALPHA)
        
        # Preenche a superfície com uma cor cinza semitransparente (GRAY)
        transparent_surface.fill((128, 128, 128, 220))  # Último valor 180 é o nível de transparência (0-255)

        # Desenha a borda preta na superfície transparente
        pygame.draw.rect(transparent_surface, BLACK, transparent_surface.get_rect(), 2, border_radius=30)

        question = self.current_question  # Obtém a pergunta atual
        if question is None:
            return  # Se não houver pergunta, não faz nada

        # Renderiza o texto da pergunta
        question_text = font.render(question["question"], True, BLACK)
        transparent_surface.blit(question_text, (20, 20))  # Desenha o texto na superfície transparente

        # Renderiza as opções de resposta
        for i, option in enumerate(question["options"]):
            option_text = font.render(f"{i+1}. {option}", True, BLACK)
            transparent_surface.blit(option_text, (40, 80 + i * 40))  # Desenha cada opção na superfície

        # Exibe o cronômetro (mudando a cor para vermelho se restarem menos de 10 segundos)
        time_color = RED if self.time_left <= 10 else BLACK
        timer_text = font.render(f"Tempo restante: {int(self.time_left)}s", True, time_color)
        transparent_surface.blit(timer_text, (20, interface_height - 90))  # Posiciona o cronômetro

        # Exibe a instrução para responder
        instruction_text = font.render("Pressione o número correspondente à resposta.", True, BLACK)
        transparent_surface.blit(instruction_text, (20, interface_height - 60))  # Instrução de como responder

        # "Blitar" a superfície transparente na tela principal (SCREEN) no centro
        SCREEN.blit(transparent_surface, (interface_x, interface_y))  # Copia a superfície transparente para a tela principal

    def handle_event(self, event):
        # Trata os eventos de seleção de resposta
        selected_option = None
        if event.key in [pygame.K_1, pygame.K_KP1]:  # Se o jogador pressionou '1'
            selected_option = 0  # Primeira opção
        elif event.key in [pygame.K_2, pygame.K_KP2]:  # Se o jogador pressionou '2'
            selected_option = 1  # Segunda opção
        elif event.key in [pygame.K_3, pygame.K_KP3]:  # Se o jogador pressionou '3'
            selected_option = 2  # Terceira opção
        elif event.key in [pygame.K_4, pygame.K_KP4]:  # Se o jogador pressionou '4'
            selected_option = 3  # Quarta opção

        return selected_option  # Retorna a opção selecionada
