import pygame

class Board:
    def __init__(self):
        self.square_size = 60  # Tamanho de cada quadrado no tabuleiro
        self.path_points = self.generate_path_points()  # Gera os pontos de caminho do tabuleiro

    def generate_path_points(self):
        """Gera uma lista de coordenadas x e y para os pontos de caminho do tabuleiro."""
        path_points = [
            {"casa": 1,  "x": 483, "y": 285}, # cordenadas ajustadas - by th
            {"casa": 2,  "x": 616, "y": 290},
            {"casa": 3,  "x": 772, "y": 290},
            {"casa": 4,  "x": 929, "y": 287},
            {"casa": 5,  "x": 1079, "y": 278},
            {"casa": 6,  "x": 1221, "y": 271},
            {"casa": 7,  "x": 1407, "y": 257},
            {"casa": 8,  "x": 1541, "y": 265},
            {"casa": 9,  "x": 1684, "y": 334},
            {"casa": 10, "x": 1723, "y": 486},
            {"casa": 11, "x": 1633, "y": 592},
            {"casa": 12, "x": 1487, "y": 645},
            {"casa": 13, "x": 1337, "y": 662},
            {"casa": 14, "x": 1143, "y": 661},
            {"casa": 15, "x": 1019, "y": 597},
            {"casa": 16, "x": 1107, "y": 496},
            {"casa": 17, "x": 1275, "y": 506},
            {"casa": 18, "x": 1420, "y": 526},
            {"casa": 19, "x": 1566, "y": 499},
            {"casa": 20, "x": 1566, "y": 395},
            {"casa": 21, "x": 1393, "y": 363},
            {"casa": 22, "x": 1246, "y": 350},
            {"casa": 23, "x": 1070, "y": 374},
            {"casa": 24, "x": 895, "y": 427},
            {"casa": 25, "x": 806, "y": 575},
            {"casa": 26, "x": 881, "y": 711},
            {"casa": 27, "x": 1048, "y": 769},
            {"casa": 28, "x": 1199, "y": 778},
            {"casa": 29, "x": 1397, "y": 757},
            {"casa": 30, "x": 1542, "y": 737},
            {"casa": 31, "x": 1692, "y": 733},
            {"casa": 32, "x": 1727, "y": 848},
            {"casa": 33, "x": 1580, "y": 883},
            {"casa": 34, "x": 1403, "y": 891},
            {"casa": 35, "x": 1228, "y": 886},
            {"casa": 36, "x": 1087, "y": 882},
            {"casa": 37, "x": 913, "y": 880},
            {"casa": 38, "x": 734, "y": 860},
            {"casa": 39, "x": 587, "y": 827},
            {"casa": 40, "x": 559, "y": 677},
            {"casa": 41, "x": 660, "y": 585},
            {"casa": 42, "x": 702, "y": 435},
            {"casa": 43, "x": 548, "y": 388},
            {"casa": 44, "x": 418, "y": 477},
            {"casa": 45, "x": 397, "y": 611},
            {"casa": 46, "x": 390, "y": 753},
        ]
        return path_points

    def draw(self, screen):
        """Desenha os quadrados no caminho com as bordas pretas."""
        for point in self.path_points:
            rect = pygame.Rect(point["x"], point["y"], self.square_size, self.square_size)
            pygame.draw.rect(screen, (255, 255, 255), rect)  # Desenha o quadrado branco
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)      # Desenha a borda preta

    def get_square_center(self, index):
        """Retorna o centro de um quadrado com base no índice de path_points."""
        if 0 <= index < len(self.path_points):
            point = self.path_points[index]
            return point["x"] + self.square_size // 2, point["y"] + self.square_size // 2
        return None
