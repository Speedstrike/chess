class Piece:
    def __init__(self, pos, isWhite, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.isWhite = isWhite
        self.available_moves = []
        self.last_moves_check = 0.0

    # Gets the available moves for a piece.
    # MUST OVERRIDE BY CLASSES THAT EXTEND IT!
    def get_available_moves(self, board, is_in_check):
        pass
    
    def move(self, new_square, board, is_pawn = False, en_passant = False, is_capture = False):
        if is_capture:
            new_square.occupying_piece = None
        if is_pawn:
            self.last_moved_two = (abs(new_square.y - self.y) == 2)
        board.set_pawn_movement(board.get_square((self.x, self.y)))
        self.x, self.y = new_square.pos
        new_square.occupying_piece = self
        if en_passant:
            board.get_square((new_square.x, new_square.y + 1 if board.white_turn else new_square.y - 1)).occupying_piece = None
        board.move_count += 0.5
        board.checking_piece = None

    def can_move(self, new_square):
        return new_square.occupying_piece is None

    # Checks if the piece can capture a different piece on a different square
    def can_capture(self, new_square):
        return new_square.occupying_piece is not None and self.isWhite != new_square.occupying_piece.isWhite
