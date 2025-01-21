import pygame

from piece import Piece

class Knight(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if self.isWhite:
            self.img = pygame.image.load('imgs/w_knight.png')
        else:
            self.img = pygame.image.load('imgs/b_knight.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        self.img = pygame.transform.flip(self.img, True, False)
        self.available_moves = []
        self.last_moves_check = 0.0

    def get_available_moves(self, board, is_in_check, check_square = None):
        if self.last_moves_check != board.move_count or board.move_count == 0 or check_square is not None:
            self.available_moves = []
            current_x, current_y = self.x, self.y

            # Lower Side L shapes: left side and right side
            if current_x - 2 > -1 and current_y + 1 < 8:
                lower_side_left_square = board.get_square((current_x - 2, current_y + 1))
                if not is_in_check:
                    if self.can_move(lower_side_left_square) or self.can_capture(lower_side_left_square):
                        self.available_moves.append(lower_side_left_square)
                    if check_square is not None and lower_side_left_square.x == check_square.x and lower_side_left_square.y == check_square.y:
                        self.available_moves.append(lower_side_left_square)
                elif board.checking_piece is not None and lower_side_left_square.x == board.checking_piece.x and lower_side_left_square.y == board.checking_piece.y:
                    self.available_moves.append(lower_side_left_square)
            if current_x + 2 < 8 and current_y + 1 < 8:
                lower_side_right_square = board.get_square((current_x + 2, current_y + 1))
                if not is_in_check:
                    if self.can_move(lower_side_right_square) or self.can_capture(lower_side_right_square):
                        self.available_moves.append(lower_side_right_square)
                    if check_square is not None and lower_side_right_square.x == check_square.x and lower_side_right_square.y == check_square.y:
                        self.available_moves.append(lower_side_right_square)
                elif board.checking_piece is not None and lower_side_right_square.x == board.checking_piece.x and lower_side_right_square.y == board.checking_piece.y:
                    self.available_moves.append(lower_side_right_square)

            # Upper Side L shapes: left side and right side
            if current_x - 2 > -1 and current_y - 1 > -1:
                upper_side_left_square = board.get_square((current_x - 2, current_y - 1))
                if not is_in_check:
                    if self.can_move(upper_side_left_square) or self.can_capture(upper_side_left_square):
                        self.available_moves.append(upper_side_left_square)
                    if check_square is not None and upper_side_left_square.x == check_square.x and upper_side_left_square.y == check_square.y:
                        self.available_moves.append(upper_side_left_square)
                elif board.checking_piece is not None and upper_side_left_square.x == board.checking_piece.x and upper_side_left_square.y == board.checking_piece.y:
                    self.available_moves.append(upper_side_left_square)
            if current_x + 2 < 8 and current_y - 1 > -1:
                upper_side_right_square = board.get_square((current_x + 2, current_y - 1))
                if not is_in_check:
                    if self.can_move(upper_side_right_square) or self.can_capture(upper_side_right_square):
                        self.available_moves.append(upper_side_right_square)
                    if check_square is not None and upper_side_right_square.x == check_square.x and upper_side_right_square.y == check_square.y:
                        self.available_moves.append(upper_side_right_square)
                elif board.checking_piece is not None and upper_side_right_square.x == board.checking_piece.x and upper_side_right_square.y == board.checking_piece.y:
                    self.available_moves.append(upper_side_right_square)

            # Lower L shapes: left and right
            if current_x - 1 > -1 and current_y + 2 < 8:
                lower_left_square = board.get_square((current_x - 1, current_y + 2))
                if not is_in_check:
                    if self.can_move(lower_left_square) or self.can_capture(lower_left_square):
                        self.available_moves.append(lower_left_square)
                    if check_square is not None and lower_left_square.x == check_square.x and lower_left_square.y == check_square.y:
                        self.available_moves.append(lower_left_square)
                elif board.checking_piece is not None and lower_left_square.x == board.checking_piece.x and lower_left_square.y == board.checking_piece.y:
                    self.available_moves.append(lower_left_square)
            if current_x + 1 < 8 and current_y + 2 < 8:
                lower_right_square = board.get_square((current_x + 1, current_y + 2))
                if not is_in_check:
                    if self.can_move(lower_right_square) or self.can_capture(lower_right_square):
                        self.available_moves.append(lower_right_square)
                    if check_square is not None and lower_right_square.x == check_square.x and lower_right_square.y == check_square.y:
                        self.available_moves.append(lower_right_square)
                elif board.checking_piece is not None and lower_right_square.x == board.checking_piece.x and lower_right_square.y == board.checking_piece.y:
                    self.available_moves.append(lower_right_square)

            # Upper L shapes: left and right
            if current_x - 1 > -1 and current_y - 2 > -1:
                upper_left_square = board.get_square((current_x - 1, current_y - 2))
                if not is_in_check:
                    if self.can_move(upper_left_square) or self.can_capture(upper_left_square):
                        self.available_moves.append(upper_left_square)
                    if check_square is not None and upper_left_square.x == check_square.x and upper_left_square.y == check_square.y:
                        self.available_moves.append(upper_left_square)
                elif board.checking_piece is not None and upper_left_square.x == board.checking_piece.x and upper_left_square.y == board.checking_piece.y:
                    self.available_moves.append(upper_left_square)
            if current_x + 1 < 8 and current_y - 2 > -1:
                upper_right_square = board.get_square((current_x + 1, current_y - 2))
                if not is_in_check:
                    if self.can_move(upper_right_square) or self.can_capture(upper_right_square):
                        self.available_moves.append(upper_right_square)
                    if check_square is not None and upper_right_square.x == check_square.x and upper_right_square.y == check_square.y:
                        self.available_moves.append(upper_right_square)
                elif board.checking_piece is not None and upper_right_square.x == board.checking_piece.x and upper_right_square.y == board.checking_piece.y:
                    self.available_moves.append(upper_right_square)

            self.last_moves_check = board.move_count

        return self.available_moves