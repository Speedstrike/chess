import pygame

from piece import Piece

class Queen(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if self.isWhite:
            self.img = pygame.image.load('imgs/w_queen.png')
        else:
            self.img = pygame.image.load('imgs/b_queen.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        self.available_moves = []
        self.last_moves_check = 0.0
        
    def get_available_moves(self, board):
        if self.last_moves_check != board.move_count or board.move_count == 0:
            self.available_moves = []
            current_x, current_y = self.x, self.y

            # Up
            for n in range(1, 8):
                if current_y - n > -1:
                    up_column = board.get_square((current_x, current_y - n))
                    if up_column.occupying_piece is not None:
                        if up_column.occupying_piece.isWhite != self.isWhite: self.available_moves.append(up_column)
                        break
                    else: self.available_moves.append(up_column)

            # Down
            for n in range(1, 8):
                if current_y + n < 8:
                    down_column = board.get_square((current_x, current_y + n))
                    if down_column.occupying_piece != None:
                        if down_column.occupying_piece.isWhite != self.isWhite: self.available_moves.append(down_column)
                        break
                    else: self.available_moves.append(down_column)

            # Left
            for n in range(1, 8):
                if current_x - n > -1:
                    left_row = board.get_square((current_x - n, current_y))
                    if left_row.occupying_piece is not None:
                        if left_row.occupying_piece.isWhite != self.isWhite: self.available_moves.append(left_row)
                        break
                    else: self.available_moves.append(left_row)

            # Right
            for n in range(1, 8):
                if current_x + n < 8:
                    right_row = board.get_square((current_x + n, current_y))
                    if right_row.occupying_piece is not None:
                        if right_row.occupying_piece.isWhite != self.isWhite: self.available_moves.append(right_row)
                        break
                    else: self.available_moves.append(right_row)

            # Top right diagonal
            for n in range(1, 8):
                if current_x + n < 8 and current_y - n > -1:
                    topright_diagonal = board.get_square((current_x + n, current_y - n))
                    if topright_diagonal.occupying_piece is not None:
                        if topright_diagonal.occupying_piece.isWhite != self.isWhite: self.available_moves.append(topright_diagonal)
                        break
                    else: self.available_moves.append(topright_diagonal)

            # Bottom right diagonal
            for n in range(1, 8):
                if current_x + n < 8 and current_y + n < 8:
                    bottomright_diagonal = board.get_square((current_x + n, current_y + n))
                    if bottomright_diagonal.occupying_piece is not None:
                        if bottomright_diagonal.occupying_piece.isWhite != self.isWhite: self.available_moves.append(bottomright_diagonal)
                        break
                    else: self.available_moves.append(bottomright_diagonal)

            # Bottom left diagonal
            for n in range(1, 8):
                if current_x - n > -1 and current_y + n < 8:
                    bottomleft_diagonal = board.get_square((current_x - n, current_y + n))
                    if bottomleft_diagonal.occupying_piece is not None:
                        if bottomleft_diagonal.occupying_piece.isWhite != self.isWhite: self.available_moves.append(bottomleft_diagonal)
                        break
                    else: self.available_moves.append(bottomleft_diagonal)

            # Top left diagonal
            for n in range(1, 8):
                if current_x - n > -1 and current_y - n > -1:
                    topleft_diagonal = board.get_square((current_x - n, current_y - n))
                    if topleft_diagonal.occupying_piece is not None:
                        if topleft_diagonal.occupying_piece.isWhite != self.isWhite: self.available_moves.append(topleft_diagonal)
                        break
                    else: self.available_moves.append(topleft_diagonal)

            self.last_moves_check = board.move_count
        
        return self.available_moves