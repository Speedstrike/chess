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
        self.available_moves = []
        self.last_moves_check = 0.0
        self.last_moved_two = False

    def get_available_moves(self, board, is_in_check, check_square = None):
        if self.last_moves_check != board.move_count or board.move_count == 0 or check_square is not None:
            self.available_moves = []
            direction = -1 if self.isWhite else 1
            current_x, current_y = self.x, self.y

            if not is_in_check:
                default_move = board.get_square((current_x, current_y + direction))
                if 0 <= current_y + direction <= 7:
                    if self.can_move(default_move):
                        self.available_moves.append(default_move)
                        if current_y == 6 or current_y == 1:
                            direction = direction - 1 if self.isWhite else direction + 1
                            extra_move = board.get_square((current_x, current_y + direction))
                            if 0 <= current_y + direction <= 7:
                                if self.can_move(extra_move):
                                    self.available_moves.append(extra_move)

            temp_y = current_y - 1 if self.isWhite else current_y + 1

            available_captures = []
            if 0 < current_x <= 7 and 0 <= temp_y <= 7:
                if not is_in_check:
                    available_captures.append(board.get_square((current_x - 1, temp_y)))
                elif board.checking_piece is not None:
                    if board.get_square((current_x - 1, temp_y)).x == board.checking_piece.x and board.get_square((current_x - 1, temp_y)).y == board.checking_piece.y:
                        available_captures.append(board.get_square((current_x - 1, temp_y)))
            if 0 <= current_x < 7 and 0 <= temp_y <= 7:
                if not is_in_check:
                    available_captures.append(board.get_square((current_x + 1, temp_y)))
                elif board.checking_piece is not None:
                    if board.get_square((current_x + 1, temp_y)).x == board.checking_piece.x and board.get_square((current_x + 1, temp_y)).y == board.checking_piece.y:
                        available_captures.append(board.get_square((current_x - 1, temp_y)))

            for capture in available_captures:
                if (self.can_capture(capture)) or (check_square is not None and capture.x == check_square.x and capture.y == check_square.y):
                    self.available_moves.append(capture)

            if not is_in_check:
                available_special_captures = []
                if 3 <= current_y <= 4:
                    if board.white_turn:
                        if current_x > 0 and isinstance(board.get_square((current_x - 1, current_y)).occupying_piece, Pawn) and board.get_square((current_x - 1, current_y)).occupying_piece.isWhite != self.isWhite:
                            if board.get_square((current_x - 1, current_y)).occupying_piece.last_moved_two:
                                available_special_captures.append(board.get_square((current_x - 1, current_y - 1)))

                        if current_x < 7 and isinstance(board.get_square((current_x + 1, current_y)).occupying_piece, Pawn) and board.get_square((current_x + 1, current_y)).occupying_piece.isWhite != self.isWhite:
                            if board.get_square((current_x + 1, current_y)).occupying_piece.last_moved_two:
                                available_special_captures.append(board.get_square((current_x + 1, current_y - 1)))
                    else:
                        if current_x > 0 and isinstance(board.get_square((current_x - 1, current_y)).occupying_piece, Pawn) and board.get_square((current_x - 1, current_y)).occupying_piece.isWhite != self.isWhite:
                            if board.get_square((current_x - 1, current_y)).occupying_piece.last_moved_two:
                                available_special_captures.append(board.get_square((current_x - 1, current_y + 1)))

                        if current_x < 7 and isinstance(board.get_square((current_x + 1, current_y)).occupying_piece, Pawn) and board.get_square((current_x + 1, current_y)).occupying_piece.isWhite != self.isWhite:
                            if board.get_square((current_x + 1, current_y)).occupying_piece.last_moved_two:
                                available_special_captures.append(board.get_square((current_x + 1, current_y + 1)))

                for capture in available_special_captures:
                    self.available_moves.append(capture)

            self.last_moves_check = board.move_count

        return self.available_moves

