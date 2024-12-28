import pygame

from piece import Piece

class Pawn(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if self.isWhite:
            self.img = pygame.image.load('imgs/w_pawn.png')
        else:
            self.img = pygame.image.load('imgs/b_pawn.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
           
    def get_available_moves(self, board):
        available_moves = []
        
        direction = -1 if self.isWhite else 1
        current_x, current_y = self.x, self.y
        
        default_move = board.get_square((current_x, current_y + direction))
        if 0 <= current_y + direction <= 7:
            if self.can_move(default_move):
                available_moves.append(default_move)
                if current_y == 6 or current_y == 1:
                    direction = direction - 1 if self.isWhite else direction + 1
                    extra_move = board.get_square((current_x, current_y + direction))
                    if 0 <= current_y + direction <= 7:
                        if self.can_move(extra_move):
                            available_moves.append(extra_move)
        
        temp_y = current_y - 1 if self.isWhite else current_y + 1
        
        available_captures = []
        if 0 < current_x <= 7 and 0 <= temp_y <= 7:
            available_captures.append(board.get_square((current_x - 1, temp_y)))
        if 0 <= current_x < 7 and 0 <= temp_y <= 7:
            available_captures.append(board.get_square((current_x + 1, temp_y)))

        for capture in available_captures:
            if self.can_capture(capture):
                available_moves.append(capture)
        
        return available_moves

