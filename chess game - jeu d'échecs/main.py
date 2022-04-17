from asyncio import constants
import time
import ai
import board
import constants
import pieces


###
### A convertir pour l'interface graphique
###
def get_user_move():
    print("Example move : A2 A4")                       # to be removed when the user interface is created
    move_str = input('Your Move : ')
    move_str = move_str.replace(' ', '')

    try:
        xfrom = letter_to_xpos(move_str[0])
        yfrom = 8 - int(move_str[1])
        xto = letter_to_xpos(move_str[2])
        yto = 8 - int(move_str[3])
        return ai.Move(xfrom, yfrom, xto, yto, False)
    except ValueError:
        print("Invalid Format. Example Move : A2 A4")   # to be removed when the user interface is created
        return get_user_move()


def get_valid_user_move(var_board):
    while True:
        move = get_user_move()
        valid = False
        possible_moves = var_board.get_possible_moves(constants.WHITE)
        if not possible_moves:
            return 0

        for possible_move in possible_moves:
            try:
                if move.equals(possible_move):
                    move.roque_move = possible_move.roque_move
                    valid = True
                    break
            except:
                pass
        if valid:
            break
        else:
            print('Invalid Move')                       # to be removed when the user interface is created
    return move

#
# Probably useless when the user interface is created
#
def letter_to_xpos(letter):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    letter = letter.upper()
    if letter in letters:
        return letters.index(letter)
    raise ValueError('Invalid Letter.')
    


#
# Entry point
#

def PvE():
    """Player VS AI mode"""

    var_board = board.Board.new()
    print(var_board)                                        # show the beggining board (new game)

    while True:
        move = get_valid_user_move(var_board)
        if move == 0:
            if var_board.is_check(constants.WHITE):
                print("Checkmate. Black wins.")             # show the end of the game (checkmate - black wins)
                break
            else:
                print('Stalemate.')                         # show the end of the game (stalemate)
                break

        var_board.move_piece(move)

        print(f'User Move: + {str(move)}')                  # show the move (will be replace a color where the piece is moved)
        print(var_board)                                    # show the updated board after the player move

        ai_move = ai.AI.get_ai_move(var_board, [])
        if ai_move == 0:
            if var_board.is_check(constants.BLACK):
                print("Checkmate. White wins.")             # show the end of the game (checkmate - white wins)
                break
            else:
                print('Stalemate.')                         # show the end of the game (stalemate)
                break

        var_board.move_piece(ai_move)
        print(f"AI move: {str(ai_move)}")                   # show the move (will be replace a color where the piece is moved)
        print(var_board)                                    # show the updated board after the AI move

def PvP():
    """Player VS Player mode"""

    var_board = board.Board.new()
    print(var_board)                                        # show the beggining board (new game)

    while True:
        user_1_move = get_valid_user_move(var_board)
        if user_1_move == 0:
            if var_board.is_check(constants.WHITE):
                print("Checkmate. Black wins.")             # show the end of the game (checkmate - black wins)
                break
            else:
                print('Stalemate.')                         # show the end of the game (stalemate)
                break

        var_board.move_piece(user_1_move)

        print(f'User_1 Move: + {str(user_1_move)}')           # show the move (will be replace a color where the piece is moved)
        print(var_board)                                    # show the updated board after the player move

        user_2_move = get_valid_user_move(var_board)
        if user_2_move == 0:
            if var_board.is_check(constants.BLACK):
                print("Checkmate. White wins.")             # show the end of the game (checkmate - white wins)
                break
            else:
                print('Stalemate.')                         # show the end of the game (stalemate)
                break

        var_board.move_piece(user_2_move)
        print(f"User_2 move: {str(user_2_move)}")                   # show the move (will be replace a color where the piece is moved)
        print(var_board)                                    # show the updated board after the AI move

def EvE():
    """AI VS AI mode"""

    var_board = board.Board.new()
    print(var_board)                                        # show the beggining board (new game)

    while True:
        ai_1_move = ai.AI.get_ai_move(var_board, [], constants.BLACK)
        if ai_1_move == 0:
            if var_board.is_check(constants.WHITE):
                print("Checkmate. Black wins.")             # show the end of the game (checkmate - black wins)
                break
            else:
                print('Stalemate.')                         # show the end of the game (stalemate)
                break

        var_board.move_piece(ai_1_move)

        print(f'AI_1 Move: + {str(ai_1_move)}')             # show the move (will be replace a color where the piece is moved)
        print(var_board)                                    # show the updated board after the player move

        #time.sleep(1)

        ai_2_move = ai.AI.get_ai_move(var_board, [], constants.WHITE)
        if ai_2_move == 0:
            if var_board.is_check(constants.BLACK):
                print("Checkmate. White wins.")             # show the end of the game (checkmate - white wins)
                break
            else:
                print('Stalemate.')                         # show the end of the game (stalemate)
                break

        var_board.move_piece(ai_2_move)
        print(f"AI_2 move: {str(ai_2_move)}")                 # show the move (will be replace a color where the piece is moved)
        print(var_board)                                    # show the updated board after the AI move

        #time.sleep(1)

EvE()