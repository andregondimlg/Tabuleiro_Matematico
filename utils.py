def get_board_center(board):
    min_x = min(square.x for square in board.board_positions)
    max_x = max(square.x for square in board.board_positions)
    min_y = min(square.y for square in board.board_positions)
    max_y = max(square.y for square in board.board_positions)
    
    board_center_x = min_x + (max_x - min_x) // 2 + board.square_size // 2
    board_center_y = min_y + (max_y - min_y) // 2 + board.square_size // 2
    
    return board_center_x, board_center_y
