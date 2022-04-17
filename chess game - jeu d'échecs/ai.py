import board
import constants
import numpy
import pieces

class Heureistics: ### changer le nom
    
    pawn_table = numpy.array([
        [0 for _ in range(8)], 
        [5, 10, 10, -20, -20, 10, 10, 5], 
        [5, -5, -10, 0, 0, -10, -5, -5],
        [0, 0, 0, 20, 20, 0, 0, 0], 
        [5, 5, 10, 25, 25, 10, 5, 5], 
        [10, 10, 20, 30, 30, 20, 10, 10], 
        [50 for _ in range(8)], 
        [0 for _ in range(8)]
    ])


    knight_table = numpy.array([
        [-50, -40, -30, -30, -30, -30, -40, -50], 
        [-40, -20, 0, 0, 0, 0, -20, -40], 
        [-30, 5, 10, 15, 15, 10, 5, -30], 
        [-30, 0, 15, 20, 20, 15, 0, -30], 
        [-30, 5, 15, 20, 20, 15, 5, -30], 
        [-30, 0, 10, 15, 15, 10, 0, -30], 
        [-40, -20, 0, 5, 5, 0, -20, -40], 
        [-50, -40, -30, -30, -30, -30, -40, -50]
    ])


    bishop_table = numpy.array([
        [-20, -10, -10, -10, -10, -10, -10, -20], 
        [-10, 5, 0, 0, 0, 0, 5, -10], 
        [-10, 10, 10, 10, 10, 10, 10, -10], 
        [-10, 0, 10, 10, 10, 10, 0, -10], 
        [-10, 5, 5, 10, 10, 5, 5, -10], 
        [-10, 0, 5, 10, 10, 5, 0, -10], 
        [-10, 0, 0, 0, 0, 0, 0, -10], 
        [-20, -10, -10, -10, -10, -10, -10, -20]
    ])


    rook_table = numpy.array([
        [0, 0, 0, 5, 5, 0, 0, 0], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [-5, 0, 0, 0, 0, 0, 0, -5], 
        [5, 10, 10, 10, 10, 10, 10, 5], 
        [0, 0, 0, 0, 0, 0, 0, 0]
    ])


    queen_table = numpy.array([
        [-20, -10, -10, -5, -5, -10, -10, -20], 
        [-10, 0, 5, 0, 0, 0, 0, -10], 
        [-10, 5, 5, 5, 5, 5, 5, -10], 
        [0, 0, 5, 5, 5, 5, 0, -5], 
        [-5, 0, 5, 5, 5, 5, 0, -5], 
        [-10, 0, 5, 5, 5, 5, 0, -10], 
        [-10, 0, 0, 0, 0, 0, 0, -10], 
        [-20, -10, -10, -5, -5, -10, -10, -20]
    ])

    
    def evaluate(board):
        score = 0
        score += Heureistics.get_material_score(board)
        score += Heureistics.get_piece_position_score(board, pieces.Pawn.piece_type, Heureistics.pawn_table)
        score += Heureistics.get_piece_position_score(board, pieces.Knight.piece_type, Heureistics.knight_table)
        score += Heureistics.get_piece_position_score(board, pieces.Bishop.piece_type, Heureistics.bishop_table)
        score += Heureistics.get_piece_position_score(board, pieces.Rook.piece_type, Heureistics.rook_table)
        score += Heureistics.get_piece_position_score(board, pieces.Queen.piece_type, Heureistics.queen_table)

        return score

    
    @staticmethod
    def get_piece_position_score(board, piece_type, table):
        white, black = 0,0
        for x in range(constants.WIDTH):
            for y in range(constants.HEIGHT):
                piece = board.chess_pieces[x][y]
                if piece != 0:
                    if piece.piece_type == piece_type:
                        if piece.color == constants.WHITE:
                            white += table[x][y]
                        else:
                            black += table[7 - x][y]

        return white - black


    @staticmethod
    def get_material_score(board):
        white, black = 0,0
        for x in range(constants.WIDTH):
            for y in range(constants.HEIGHT):
                piece = board.chess_pieces[x][y]
                if piece != 0:
                    if piece.color == constants.WHITE:
                        white += piece.value
                    else:
                        black += piece.value

        return white - black

opening file
class AI:

    INFINTE = 100000000

    @staticmethod
    def get_ai_move(chessboard, invalid_moves, color):
        best_move = 0
        best_score = AI.INFINTE
        print(chessboard)
        for move in chessboard.get_possible_moves(color):
            if AI.is_invalid_move(move, invalid_moves):
                continue

            copy = board.Board.clone(chessboard)
            copy.move_piece(move)

            score = AI.alphabeta(copy, 2, -AI.INFINTE, AI.INFINTE, True)
        
            if score < best_score:
                best_move = move
                best_score = score
        
        if best_move == 0:
            return 0

        copy = board.Board.clone(chessboard)
        copy.move_piece(best_move)

        if copy.is_check(constants.BLACK):
            invalid_moves.append(best_move)
            return AI.get_ai_move(chessboard, invalid_moves, color)
        
        return best_move

    
    @staticmethod
    def is_invalid_move(move, invalid_moves):
        for invalid_move in invalid_moves:
            if invalid_move.equals(move):
                return True
        return False


    @staticmethod
    def minimax(board, depth, maximizing):
        if depth == 0:
            return Heureistics.evaluate(board)

        if maximizing:
            best_score = -AI.INFINTE
            for move in board.get_possible_moves(constants.WHITE):
                copy = board.Board.clone(board)
                copy.move_piece(move)

                score = AI.minimax(copy, depth - 1, False)
                if score > best_score:
                    best_score = score
            return best_score
        
        else:
            best_score = AI.INFINTE
            for move in board.get_possible_moves(constants.BLACK):
                copy = board.Board.clone(board)
                copy.move_piece(move)

                score = AI.minimax(copy, depth - 1, True)
                if score < best_score:
                    best_score = score
            return best_score


    @staticmethod
    def alphabeta(chessboard, depth, a, b, maximizing):
        if depth:
            return Heureistics.evaluate(chessboard)
        
        if maximizing:
            best_score = -AI.INFINTE
            for move in chessboard.get_possible_moves(constants.WHITE):
                copy = board.Board.clone(chessboard)
                copy.piece_move(move)

                best_score = max(best_score, AI.alphabeta(copy, depth - 1, a, b, False))
                a = max(a, best_score)

                if b <= a:
                    break
            return best_score
        
        else:
            best_score = -AI.INFINTE
            for move in chessboard.get_possible_moves(constants.BLACK):
                copy = board.Board.clone(chessboard)
                copy.move_piece(move)

                best_score = min(best_score, AI.alphabeta(copy, depth - 1, a, b, True))
                b = min(b, best_score)
                if b <= a:
                    break
            return best_score


class Move:

    def __init__(self, x, y, xx, yy, roque_move):
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy
        self.roque_move = roque_move

    
    def equals(self, other):
        return self.x == other.x and self.y == other.y and self.xx == other.xx and self.yy == other.yy


    def __str__(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        return f"({letters[self.x]}{str(8 - self.y)}) -> ({letters[self.xx]}{str( 8 -self.yy)})"