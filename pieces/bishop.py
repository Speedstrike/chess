import pygame

from piece import Piece

class Bishop(Piece):
    def __init__(self, pos, is_white, board):
        super().__init__(pos, is_white, board)
        if self.isWhite:
            self.img = pygame.image.load('imgs/w_bishop.png')
        else:
            self.img = pygame.image.load('imgs/b_bishop.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        self.available_moves = []
        self.last_moves_check = 0.0

    def get_available_moves(self, board, is_in_check, check_square = None):
        if self.last_moves_check != board.move_count or board.move_count == 0 or check_square is not None:
            self.available_moves = []
            current_x, current_y = self.x, self.y

            # Top right diagonal
            for n in range(1, 8):
                if current_x + n < 8 and current_y - n > -1:
                    topright_diagonal = board.get_square((current_x + n, current_y - n))
                    if check_square is not None and topright_diagonal.x == check_square.x and topright_diagonal.y == check_square.y:
                        if not is_in_check:
                            self.available_moves.append(topright_diagonal)
                    elif topright_diagonal.occupying_piece is not None:
                        if topright_diagonal.occupying_piece.isWhite != self.isWhite:
                            if not is_in_check:
                                self.available_moves.append(topright_diagonal)
                        if board.checking_piece is not None and board.checking_piece.x == topright_diagonal.x and board.checking_piece.y == topright_diagonal.y:
                            self.available_moves.append(topright_diagonal)
                        break
                    elif not is_in_check:
                        self.available_moves.append(topright_diagonal)

            # Bottom right diagonal
            for n in range(1, 8):
                if current_x + n < 8 and current_y + n < 8:
                    bottomright_diagonal = board.get_square((current_x + n, current_y + n))
                    if check_square is not None and bottomright_diagonal.x == check_square.x and bottomright_diagonal.y == check_square.y:
                        if not is_in_check:
                            self.available_moves.append(bottomright_diagonal)
                    elif bottomright_diagonal.occupying_piece is not None:
                        if bottomright_diagonal.occupying_piece.isWhite != self.isWhite:
                            if not is_in_check:
                                self.available_moves.append(bottomright_diagonal)
                        if board.checking_piece is not None and board.checking_piece.x == bottomright_diagonal.x and board.checking_piece.y == bottomright_diagonal.y:
                            self.available_moves.append(bottomright_diagonal)
                        break
                    elif not is_in_check:
                        self.available_moves.append(bottomright_diagonal)

            # Bottom left diagonal
            for n in range(1, 8):
                if current_x - n > -1 and current_y + n < 8:
                    bottomleft_diagonal = board.get_square((current_x - n, current_y + n))
                    if check_square is not None and bottomleft_diagonal.x == check_square.x and bottomleft_diagonal.y == check_square.y:
                        if not is_in_check:
                            self.available_moves.append(bottomleft_diagonal)
                    elif bottomleft_diagonal.occupying_piece is not None:
                        if bottomleft_diagonal.occupying_piece.isWhite != self.isWhite:
                            if not is_in_check:
                                self.available_moves.append(bottomleft_diagonal)
                        if board.checking_piece is not None and board.checking_piece.x == bottomleft_diagonal.x and board.checking_piece.y == bottomleft_diagonal.y:
                            self.available_moves.append(bottomleft_diagonal)
                        break
                    elif not is_in_check:
                        self.available_moves.append(bottomleft_diagonal)

            # Top left diagonal
            for n in range(1, 8):
                if current_x - n > -1 and current_y - n > -1:
                    topleft_diagonal = board.get_square((current_x - n, current_y - n))
                    if check_square is not None and topleft_diagonal.x == check_square.x and topleft_diagonal.y == check_square.y:
                        if not is_in_check:
                            self.available_moves.append(topleft_diagonal)
                    elif topleft_diagonal.occupying_piece is not None:
                        if topleft_diagonal.occupying_piece.isWhite != self.isWhite:
                            if not is_in_check:
                                self.available_moves.append(topleft_diagonal)
                        if board.checking_piece is not None and board.checking_piece.x == topleft_diagonal.x and board.checking_piece.y == topleft_diagonal.y:
                            self.available_moves.append(topleft_diagonal)
                        break
                    elif not is_in_check:
                        self.available_moves.append(topleft_diagonal)

            self.last_moves_check = board.move_count
        return self.available_moves