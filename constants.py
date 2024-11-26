import pygame

pygame.init()

WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Tabuleiro Matemático")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
YELLOW = (255, 215, 0)
GRAY = (200, 200, 200)


PLAYER_COLORS = { # personagens
    "Willy Cat": WHITE,
    "Dr Newton": RED,
    "Sir Pi-thon": YELLOW,
    "Fionacci": GREEN
}

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 70)

HABILIDADES = {
    "Willy Cat": "remover_alternativas",
    "Dr Newton": "dobro_movimento",
    "Sir Pi-thon": "trocar_pergunta",
    "Fionacci": "bonus_por_velocidade",
    "Jogador 1": "remover_alternativas",  # Exemplo para nome padrão
    "Jogador 2": "dobro_movimento",
    "Jogador 3": "trocar_pergunta",
    "Jogador 4": "bonus_por_velocidade",
}

