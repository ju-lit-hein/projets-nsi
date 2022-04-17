import ai
import constants
import pieces


class Board:
    WIDTH = constants.WIDTH
    HEIGHT = constants.HEIGHT

    def __init__(self, pieces, white_king_moved, black_king_moved):
        self.chess_pieces = pieces
        self.white_king_moved = white_king_moved
        self.black_king_moved = black_king_moved


    @classmethod
    def clone(cls, chessboard):
        cloned_chess_pieces = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = chessboard.chess_pieces[x][y]
                if piece != 0:
                    cloned_chess_pieces[x][y] = piece.clone()
        return cls(cloned_chess_pieces, chessboard.white_king_moved, chessboard.black_king_moved)

    
    @classmethod
    def new(cls):
        chess_pieces = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]

        for x in range(Board.WIDTH):
            chess_pieces[x][Board.HEIGHT - 2 ] = pieces.Pawn(x, Board.HEIGHT - 2, constants.WHITE)
            chess_pieces[x][1] = pieces.Pawn(x, 1, constants.BLACK)

        chess_pieces[0][Board.HEIGHT - 1] = pieces.Rook(0, Board.HEIGHT - 1, constants.WHITE)
        chess_pieces[Board.WIDTH - 1][Board.HEIGHT - 1] = pieces.Rook(Board.WIDTH - 1, Board.HEIGHT - 1, constants.WHITE)
        chess_pieces[0][0] = pieces.Rook(0, 0, constants.BLACK)
        chess_pieces[Board.WIDTH - 1][0] = pieces.Rook(Board.WIDTH - 1, 0, constants.BLACK)

        chess_pieces[1][Board.HEIGHT - 1] = pieces.Knight(1, Board.HEIGHT - 1, constants.WHITE)
        chess_pieces[Board.WIDTH - 2][Board.HEIGHT - 1] = pieces.Knight(Board.WIDTH - 2, Board.HEIGHT - 1, constants.WHITE)
        chess_pieces[1][0] = pieces.Knight(1, 0, constants.BLACK)
        chess_pieces[Board.WIDTH - 2][0] = pieces.Knight(Board.WIDTH - 2, 0, constants.BLACK)

        chess_pieces[2][Board.HEIGHT - 1] = pieces.Bishop(2, Board.HEIGHT - 1, constants.WHITE)
        chess_pieces[Board.WIDTH - 3][Board.HEIGHT - 1] = pieces.Bishop(Board.WIDTH - 3, Board.HEIGHT - 1, constants.WHITE)
        chess_pieces[2][0] = pieces.Bishop(2, 0, constants.BLACK)
        chess_pieces[Board.WIDTH - 3][0] = pieces.Bishop(Board.WIDTH - 3, 0, constants.BLACK)

        chess_pieces[4][Board.HEIGHT - 1] = pieces.King(4, Board.HEIGHT - 1, constants.WHITE)
        chess_pieces[3][Board.HEIGHT - 1] = pieces.Queen(3, Board.HEIGHT - 1, constants.WHITE)
        chess_pieces[4][0] = pieces.King(4, 0, constants.BLACK)
        chess_pieces[3][0] = pieces.Queen(3, 0, constants.BLACK)

        return cls(chess_pieces, False, False)


    def get_possible_moves(self, color):
        moves = []
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = self.chess_pieces[x][y]
                if piece != 0:
                    if piece.color == color:
                        moves += piece.get_moves(self)

        return moves
    

    def move_piece(self, move):
        piece = self.chess_pieces[move.x][move.y]
        piece.x = move.xx
        piece.y = move.yy
        self.chess_pieces[move.xx][move.yy] = piece
        self.chess_pieces[move.x][move.y] = 0

        if piece.piece_type == pieces.Pawn.piece_type:
            if piece.y == 0 or piece.y == Board.HEIGHT  - 1:
                self.chess_pieces[piece.x][piece.y] = pieces.Queen(piece.x, piece.y, piece.color)

        if move.roque_move:
            if move.xx < move.x:    # left roque
                rook = self.chess_pieces[move.x - 4][move.y]
                rook.x = move.x - 1
                self.chess_pieces[move.x - 1][move.y] = rook
                self.chess_pieces[move.x - 4][move.y] = 0
            
            if move.xx > move.x:    # right roque
                rook = self.chess_pieces[move.x + 3][move.y]
                rook.x = move.x - 1
                self.chess_pieces[move.x + 1][move.y] = rook
                self.chess_pieces[move.x + 3][move.y] = 0

        if piece.piece_type == pieces.King.piece_type:
            if piece.color == constants.WHITE:
                self.white_king_moved = True
            else:
                self.black_king_moved = True


    def is_check(self, color):
        other_color = constants.WHITE
        if color == other_color:
            other_color = constants.BLACK

        for move in self.get_possible_moves(other_color):
            copy = Board.clone(self)
            copy.move_piece(move)

            king_in_move = False
            for x in range(constants.WIDTH):
                for y in range(constants.HEIGHT):
                    piece = copy.chess_pieces[x][y]
                    if piece != 0:
                        if piece.color == color and piece.piece_type == pieces.King.piece_type:
                            king_in_move = True

        return not king_in_move


    def get_piece(self, x, y):
        if not self.in_bounds(x, y):
            return 0
        return self.chess_pieces[x][y]

    
    def in_bounds(self, x, y):
        return x >= 0 and y >= 0 and x < constants.WIDTH and y < constants.HEIGHT

    ###
    ### A retirer après la création de l'interface graphique
    ###
    def __str__(self):
        string =  "    A  B  C  D  E  F  G  H\n"
        string += "    ----------------------\n"

        for y in range(constants.HEIGHT):
            string += str(8 - y) + " | "
            for x in range(constants.WIDTH):
                piece = self.chess_pieces[x][y]
                if piece != 0:
                    string += str(piece)
                else:
                    string += ".. "
            string += "\n"
        return string + "\n"