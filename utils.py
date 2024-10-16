def get_board_center(board):
    """Calcula o centro do tabuleiro com base nos pontos de caminho."""
    # Use 'path_points' em vez de 'board_positions'
    min_x = min(square["x"] for square in board.path_points)
    max_x = max(square["x"] for square in board.path_points)
    min_y = min(square["y"] for square in board.path_points)
    max_y = max(square["y"] for square in board.path_points)

    center_x = (min_x + max_x) // 2
    center_y = (min_y + max_y) // 2

    return center_x, center_y
