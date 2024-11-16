import pygame

class Board:
    def __init__(self):
        self.square_size = 60  
        self.path_points = self.generate_path_points() 

    def generate_path_points(self):
        """gera uma lista de coordenadas x e y para os pontos de caminho do tabuleiro."""
        path_points = [
            {"casa": 1,  "x": 466, "y": 281},
            {"casa": 2,  "x": 609, "y": 286},
            {"casa": 3,  "x": 762, "y": 292},
            {"casa": 4,  "x": 920, "y": 291},
            {"casa": 5,  "x": 1071, "y": 283},
            {"casa": 6,  "x": 1231, "y": 273},
            {"casa": 7,  "x": 1395, "y": 257},
            {"casa": 8,  "x": 1543, "y": 276},
            {"casa": 9,  "x": 1677, "y": 343},
            {"casa": 10, "x": 1715, "y": 483},
            {"casa": 11, "x": 1627, "y": 596},
            {"casa": 12, "x": 1480, "y": 659},
            {"casa": 13, "x": 1318, "y": 683},
            {"casa": 14, "x": 1146, "y": 670},
            {"casa": 15, "x": 1014, "y": 590},
            {"casa": 16, "x": 1114, "y": 499},
            {"casa": 17, "x": 1274, "y": 507},
            {"casa": 18, "x": 1442, "y": 531},
            {"casa": 19, "x": 1592, "y": 501},
            {"casa": 20, "x": 1567, "y": 386},
            {"casa": 21, "x": 1399, "y": 359},
            {"casa": 22, "x": 1233, "y": 343},
            {"casa": 23, "x": 1065, "y": 380},
            {"casa": 24, "x": 896, "y": 437},
            {"casa": 25, "x": 818, "y": 571},
            {"casa": 26, "x": 878, "y": 704},
            {"casa": 27, "x": 1028, "y": 753},
            {"casa": 28, "x": 1197, "y": 777},
            {"casa": 29, "x": 1382, "y": 767},
            {"casa": 30, "x": 1556, "y": 742},
            {"casa": 31, "x": 1723, "y": 733},
            {"casa": 32, "x": 1724, "y": 845},
            {"casa": 33, "x": 1580, "y": 884},
            {"casa": 34, "x": 1401, "y": 897},
            {"casa": 35, "x": 1230, "y": 898},
            {"casa": 36, "x": 1054, "y": 897},
            {"casa": 37, "x": 881, "y": 888},
            {"casa": 38, "x": 732, "y": 876},
            {"casa": 39, "x": 582, "y": 820},
            {"casa": 40, "x": 568, "y": 678},
            {"casa": 41, "x": 659, "y": 574},
            {"casa": 42, "x": 532, "y": 381},
            {"casa": 43, "x": 434, "y": 480},
            {"casa": 44, "x": 397, "y": 634},
            {"casa": 45, "x": 390, "y": 765}
        ]
        return path_points

    def draw(self, screen):
        for point in self.path_points:
            rect = pygame.Rect(point["x"], point["y"], self.square_size, self.square_size)
            pygame.draw.rect(screen, (255, 255, 255), rect)  
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)      

    def get_square_center(self, index):
        if 0 <= index < len(self.path_points):
            point = self.path_points[index]
            return point["x"] + self.square_size // 2, point["y"] + self.square_size // 2
        return None

