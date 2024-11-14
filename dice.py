import pygame 
import random
import os
from constants import SCREEN, font, WHITE
from utils import get_board_center

pygame.mixer.init() 

class Dice:
    def __init__(self):
        self.result = None
        self.rolling = False
        self.dice_images = self.load_dice_images()
        self.current_image = None
        self.roll_sound = self.load_roll_sound()

    def load_dice_images(self):
        images = {}
        for i in range(1, 7):
            path = os.path.join('assets', 'images', f'dice_{i}.png')
            try:
                image = pygame.image.load(path).convert_alpha()
                image = pygame.transform.scale(image, (100, 100))  # Ajuste o tamanho conforme necessário
                images[i] = image
            except pygame.error as e:
                print(f"Erro ao carregar a imagem do dado {i}: {e}")
            except FileNotFoundError:
                print(f"Imagem do dado {i} não encontrada.")
        return images

    def load_roll_sound(self):
        try:
            sound_path = os.path.join('assets', 'sounds_effects', 'dice.mp3')
            return pygame.mixer.Sound(sound_path)
        except pygame.error as e:
            print(f"Erro ao carregar o som do dado: {e}")
            return None

    def roll_dice_animation(self, board, draw_functions):
        self.rolling = True
        if self.roll_sound:
            self.roll_sound.play()  # Toca o som ao iniciar a rolagem

        animation_cycles = 10  # Número de ciclos de troca de face
        cycle_delay = 100       # Tempo entre cada troca de face em milissegundos
        cycle_count = 0
        clock = pygame.time.Clock()

        while self.rolling and cycle_count < animation_cycles:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Escolhe uma face aleatória para exibir
            random_face = random.randint(1, 6)
            self.current_image = self.dice_images.get(random_face, None)

            for func in draw_functions:
                func()
            dice_rect = self.current_image.get_rect(center=(1734, 179))
            if self.current_image:
                SCREEN.blit(self.current_image, dice_rect.topleft)
            pygame.display.update()

            pygame.time.delay(cycle_delay)
            cycle_count += 1
            clock.tick(60)

        # Após a animação, define o resultado final
        self.result = random.randint(1, 6)
        self.current_image = self.dice_images.get(self.result, None)
        self.rolling = False

        # Atualiza a tela com o resultado final
        for func in draw_functions:
            func()
        if self.current_image:
            dice_rect = self.current_image.get_rect(center=(1734, 179))  # Posição fixa para o dado
            SCREEN.blit(self.current_image, dice_rect.topleft)
        pygame.display.update()

        return self.result

    def draw_result(self, board, message):
        if self.result is not None and self.current_image:
            # Usando a posição fixa do dado
            dice_rect = self.current_image.get_rect(center=(1734, 179))
            SCREEN.blit(self.current_image, dice_rect.topleft)

            if message:
                message_text = font.render(message, True, (0, 0, 0))
                SCREEN.blit(message_text, (700 - message_text.get_width()//2, 100 + dice_rect.height//2))
