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

    def get_available_moves(self, board, check_square = None):
        if self.last_moves_check != board.move_count or board.move_count == 0 or check_square is not None:
            self.available_moves = []
            current_x, current_y = self.x, self.y

            # Up
            for n in range(1, 8):
                if current_y - n > -1:
                    up_column = board.get_square((current_x, current_y - n))
                    if check_square is not None and up_column.x == check_square.x and up_column.y == check_square.y:
                        self.available_moves.append(up_column)
                    if up_column.occupying_piece is not None:
                        if up_column.occupying_piece.isWhite != self.isWhite: self.available_moves.append(up_column)
                        break
                    else:
                        self.available_moves.append(up_column)

            # Down
            for n in range(1, 8):
                if current_y + n < 8:
                    down_column = board.get_square((current_x, current_y + n))
                    if check_square is not None and down_column.x == check_square.x and down_column.y == check_square.y:
                        self.available_moves.append(down_column)
                    if down_column.occupying_piece != None:
                        if down_column.occupying_piece.isWhite != self.isWhite: self.available_moves.append(down_column)
                        break
                    else:
                        self.available_moves.append(down_column)

            # Left
            for n in range(1, 8):
                if current_x - n > -1:
                    left_row = board.get_square((current_x - n, current_y))
                    if check_square is not None and left_row.x == check_square.x and left_row.y == check_square.y:
                        self.available_moves.append(left_row)
                    if left_row.occupying_piece is not None:
                        if left_row.occupying_piece.isWhite != self.isWhite: self.available_moves.append(left_row)
                        break
                    else:
                        self.available_moves.append(left_row)

            # Right
            for n in range(1, 8):
                if current_x + n < 8:
                    right_row = board.get_square((current_x + n, current_y))
                    if check_square is not None and right_row.x == check_square.x and right_row.y == check_square.y:
                        self.available_moves.append(right_row)
                    if right_row.occupying_piece is not None:
                        if right_row.occupying_piece.isWhite != self.isWhite: self.available_moves.append(right_row)
                        break
                    else:
                        self.available_moves.append(right_row)

            # Top right diagonal
            for n in range(1, 8):
                if current_x + n < 8 and current_y - n > -1:
                    topright_diagonal = board.get_square((current_x + n, current_y - n))
                    if check_square is not None and topright_diagonal.x == check_square.x and topright_diagonal.y == check_square.y:
                        self.available_moves.append(topright_diagonal)
                    if topright_diagonal.occupying_piece is not None:
                        if topright_diagonal.occupying_piece.isWhite != self.isWhite: self.available_moves.append(topright_diagonal)
                        break
                    else:
                        self.available_moves.append(topright_diagonal)

            # Bottom right diagonal
            for n in range(1, 8):
                if current_x + n < 8 and current_y + n < 8:
                    bottomright_diagonal = board.get_square((current_x + n, current_y + n))
                    if check_square is not None and bottomright_diagonal.x == check_square.x and bottomright_diagonal.y == check_square.y:
                        self.available_moves.append(bottomright_diagonal)
                    if bottomright_diagonal.occupying_piece is not None:
                        if bottomright_diagonal.occupying_piece.isWhite != self.isWhite: self.available_moves.append(bottomright_diagonal)
                        break
                    else:
                        self.available_moves.append(bottomright_diagonal)

            # Bottom left diagonal
            for n in range(1, 8):
                if current_x - n > -1 and current_y + n < 8:
                    bottomleft_diagonal = board.get_square((current_x - n, current_y + n))
                    if check_square is not None and bottomleft_diagonal.x == check_square.x and bottomleft_diagonal.y == check_square.y:
                        self.available_moves.append(bottomleft_diagonal)
                    if bottomleft_diagonal.occupying_piece is not None:
                        if bottomleft_diagonal.occupying_piece.isWhite != self.isWhite: self.available_moves.append(bottomleft_diagonal)
                        break
                    else:
                        self.available_moves.append(bottomleft_diagonal)

            # Top left diagonal
            for n in range(1, 8):
                if current_x - n > -1 and current_y - n > -1:
                    topleft_diagonal = board.get_square((current_x - n, current_y - n))
                    if check_square is not None and topleft_diagonal.x == check_square.x and topleft_diagonal.y == check_square.y:
                        self.available_moves.append(topleft_diagonal)
                    if topleft_diagonal.occupying_piece is not None:
                        if topleft_diagonal.occupying_piece.isWhite != self.isWhite: self.available_moves.append(topleft_diagonal)
                        break
                    else:
                        self.available_moves.append(topleft_diagonal)

            self.last_moves_check = board.move_count

        return self.available_moves