import pygame

from piece import Piece

class King(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if self.isWhite:
            self.img = pygame.image.load('imgs/w_king.png')
        else:
            self.img = pygame.image.load('imgs/b_king.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        self.available_moves = []
        self.last_moves_check = 0.0
        self.has_moved = False
        
    def get_available_moves(self, board):
        if self.last_moves_check != board.move_count or board.move_count == 0:
            self.available_moves = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if 0 <= self.x + i <= 7 and 0 <= self.y + j <= 7:
                        square = board.get_square((self.x + i, self.y + j))
                        if (square.occupying_piece is None or square.occupying_piece.isWhite != self.isWhite) and not board.is_in_check(board.white_turn, square):
                            self.available_moves.append(square)

            self.last_moves_check = board.move_count
                
        return self.available_moves