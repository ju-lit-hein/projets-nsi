import ai, board, constants

class Piece:

    def __init__(self, x, y, color, piece, value):
        self.x = x
        self.y = y
        self.color = color
        self.piece = piece
        self.value = value


    # Méthodes pour obtenir les mouvements valides

    def get_diagonal_moves(self, board):
        moves = []

        for i in range(1,8):
            if not board.in_bounds(self.x + i, self.y + i):
                break
            piece = board.get_piece(self.x + i, self.y + i)
            moves.append(self.get_move(board, self.x + i, self.y + i))

            if piece != 0:
                break

        for i in range(1,8):
            if not board.in_bounds(self.x + i, self.y - i):
                break
            piece = board.get_piece(self.x + i, self.y - i)
            moves.append(self.get_move(board, self.x + i, self.y - i))

            if piece != 0:
                break
        
        for i in range(1,8):
            if not board.in_bounds(self.x - i, self.y - i):
                break
            piece = board.get_piece(self.x - i, self.y -i)
            moves.append(self.get_move(board, self.x - i, self.y - i))

            if piece != 0:
                break
        
        for i in range(1,8):
            if not board.in_bounds(self.x - i, self.y + i):
                break
            piece = board.get_piece(self.x - i, self.y + i)
            moves.append(self.get_move(board, self.x - i, self.y + i))

            if piece != 0:
                break

        return self.remove_zero(moves)


    def get_line_moves(self, board):
        moves = []

        for i in range(1, 8 - self.x):
            piece = board.get_piece(self.x + i, self.y)
            moves.append(self.get_move(board, self.x + i, self.y))

            if piece != 0:
                break
        
        for i in range(1, self.x + 1):
            piece = board.get_piece(self.x - i, self.y)
            moves.append(self.get_move(board, self.x - i, self.y))

            if piece != 0:
                break

        for i in range(1, 8 - self.y):
            piece = board.get_piece(self.x, self.y + i)
            moves.append(self.get_move(board, self.x, self.y + i))

            if piece != 0:
                break

        for i in range(1, self.y + 1):
            piece = board.get_piece(self.x, self.y - i)
            moves.append(self.get_move(board, self.x, self.y - i))

            if piece != 0:
                break

        return self.remove_zero(moves)


    def get_move(self, board, xx, yy):
        move = 0
        if board.in_bounds(xx, yy):
            piece = board.get_piece(xx, yy)
            if piece != 0:
                if piece.color != self.color:
                    move = ai.Move(self.x, self.y, xx, yy, False)       # le booléen est là pour indiquer si le joueur faite un roque
                
            else:
                move = ai.Move(self.x, self.y, xx, yy, False)       # le booléen est là pour indiquer si le joueur faite un roque
        return move

    
    def remove_zero(self, tab):
        return [move for move in tab if move != 0]


    def __str__(self):
        return self.color + self.piece + ' '


class Rook(Piece):

    piece_type = 'R'
    value = constants.ROOK_VALUE

    def __init__(self,x, y, color):
        super(Rook, self).__init__(x, y, color, Rook.piece_type, Rook.value)


    def get_moves(self, board):
        return self.get_line_moves(board)


    def clone(self):
        return Rook(self.x, self.y, self.color)


class Knight(Piece):

    piece_type = 'C'
    value = constants.KNIGHT_VALUE

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color, Knight.piece_type, Knight.value)


    def get_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x + 2, self.y + 1))
        moves.append(self.get_move(board, self.x - 1, self.y + 2))
        moves.append(self.get_move(board, self.x - 2, self.y + 1))
        moves.append(self.get_move(board, self.x + 1, self.y - 2))
        moves.append(self.get_move(board, self.x + 2, self.y - 1))
        moves.append(self.get_move(board, self.x + 1, self.y + 2))
        moves.append(self.get_move(board, self.x - 2, self.y - 1))
        moves.append(self.get_move(board, self.x - 1, self.y - 2))

        return self.remove_zero(moves)

    
    def clone(self):
        return Knight(self.x, self.y, self.color)


class Bishop(Piece):

    piece_type = 'B'
    value = constants.BISHOP_VALUE

    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, Bishop.piece_type, Bishop.value)


    def get_moves(self, board):
        return self.get_diagonal_moves(board)

    
    def clone(self):
        return Bishop(self.x, self.y, self.color)


class Queen(Piece):

    piece_type = 'Q'
    value = constants.QUEEN_VALUE

    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, Queen.piece_type, Queen.value)

    
    def get_moves(self, board):
        diagonal = self.get_diagonal_moves(board)
        line = self.get_line_moves(board)
        return diagonal + line

    
    def clone(self):
        return Queen(self.x, self.y, self.color)


class King(Piece):

    piece_type = 'K'
    value = constants.KING_VALUE

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, King.piece_type, King.value)


    def get_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x + 1, self.y))
        moves.append(self.get_move(board, self.x + 1, self.y + 1))
        moves.append(self.get_move(board, self.x, self.y + 1))
        moves.append(self.get_move(board, self.x - 1, self.y + 1))
        moves.append(self.get_move(board, self.x - 1, self.y))
        moves.append(self.get_move(board, self.x - 1, self.y - 1))
        moves.append(self.get_move(board, self.x, self.y - 1))
        moves.append(self.get_move(board, self.x + 1, self.y - 1))

        moves.append(self.get_left_roque(board))
        moves.append(self.get_right_roque(board))

        return self.remove_zero(moves)


    def get_left_roque(self, board):
        if self.color == constants.WHITE and board.white_king_moved:
            return 0
        if self.color == constants.BLACK and board.black_king_moved:
            return 0


        piece = board.get_piece(0, self.y)

        if piece != 0:
            if piece.color == self.color and piece.piece_type == Rook.piece_type:
                if board.get_piece(self.x - 1, self.y) == 0 and board.get_piece(self.x - 2, self.y) == 0 and board.get_piece(self.x - 3, self.y) == 0:
                    return ai.Move(self.x, self.y, self.x - 2, self.y, True)

        return 0

    def get_right_roque(self, board):
        if self.color == constants.WHITE and board.white_king_moved:
            return 0
        if self.color == constants.BLACK and board.black_king_moved:
            return 0


        piece = board.get_piece(self.x + 3, self.y)

        if piece != 0:
            if piece.color == self.color and piece.piece_type == Rook.piece_type:
                if board.get_piece(self.x + 1, self.y) == 0 and board.get_piece(self.x + 2, self.y) == 0:
                    return ai.Move(self.x, self.y, self.x + 2, self.y, True)

        return 0

    
    def clone(self):
        return King(self.x, self.y, self.color)


class Pawn(Piece):

    piece_type = 'P'
    value = constants.PAWN_VALUE

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, Pawn.piece_type, Pawn.value)


    def is_starting_position(self):
        if self.color == constants.BLACK:
            return self.y == 1
        else:
            return self.y == 6

        
    
    def get_moves(self, board):
        moves = []

        direction = -1
        if self.color == constants.BLACK:
            direction = 1

        
        # avancée d'une case
        if board.get_piece(self.x, self.y + direction) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction))

        # avancée de deux cases au départ
        if self.is_starting_position() and board.get_piece(self.x, self.y + direction) == 0 and board.get_piece(self.x, self.y + direction * 2) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction * 2))

        # Manger d'autres pièces
        piece = board.get_piece(self.x + 1, self.y + direction)
        if piece != 0:
            moves.append(self.get_move(board, self.x + 1, self.y + direction))

        piece = board.get_piece(self.x - 1, self.y + direction)
        if piece != 0:
            moves.append(self.get_move(board, self.x - 1, self.y + direction))


        return self.remove_zero(moves)

    
    def clone(self):
        return Pawn(self.x, self.y, self.color)