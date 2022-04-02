from asyncio import constants
import ai
import board
import constants
import pieces


###
### A convertir pour l'interface graphique
###
def get_user_move():
    print("Example move : A2 A4")
    move_str = input('Your Move : ')
    move_str = move_str.replace(' ', '')

    try:
        xfrom = letter_to_xpos(move_str[0])
        yfrom = 8 - int(move_str[1])
        xto = letter_to_xpos(move_str[2])
        yto = 8 - int(move_str[3])
        return ai.Move(xfrom, yfrom, xto, yto, False)
    except ValueError:
        print("Invalid Format. Example Move : A2 A4")
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
            print('Invalid Move')
    return move


def letter_to_xpos(letter):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    letter = letter.upper()
    if letter in letters:
        return letters.index(letter)
    raise ValueError('Invalid Letter.')
    


#
# Entry point
#


var_board = board.Board.new()
print(var_board)

while True:
    move = get_valid_user_move(var_board)
    if move == 0:
        if var_board.is_check(constants.WHITE):
            print("Checkmate. Black wins.")
            break
        else:
            print('Stalemate.')
            break

    var_board.move_piece(move)

    print(f'User Move: + {str(move)}')
    print(var_board)    # mise à jour du plateau

    ai_move = ai.AI.get_ai_move(var_board, [])
    if ai_move == 0:
        if var_board.is_check(constants.BLACK):
            print("Checkmate. White wins.")
            break
        else:
            print('Stalemate.')
            break

    var_board.move_piece(ai_move)
    print(f"AI move: {str(ai_move)}")
    print(var_board) # mise à jour du plateau