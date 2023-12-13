'''Game begins'''
import random
the_board = {"top_L": ' ', "top_M": ' ', "top_R": ' ',
             "mid_L": ' ', "mid_M": ' ', "mid_R": ' ',
             "low_L": ' ', "low_M": ' ', "low_R": ' '}


def print_board(board):
    '''This function prints the board'''
    print(f"{board['top_L']} | {board['top_M']} | {board['top_R']}")
    print("--+---+--")
    print(f"{board['mid_L']} | {board['mid_M']} | {board['mid_R']}")
    print("--+---+--")
    print(f"{board['low_L']} | {board['low_M']} | {board['low_R']}")


turn = 'X'
for i in range(9):
    print_board(the_board)
    board_rec = []
    temp_board = the_board.copy()
    player_move = input(f"Turn for {turn}. Move on to which space?")
    temp_board[player_move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    temp_board.pop(player_move)
    comp_move = random.choice(list(temp_board))
    temp_board[comp_move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    temp_board.pop(comp_move)

    if temp_board['top_L'] == 'X' and temp_board['top_M'] == 'X' and temp_board['top_R'] == 'X':
        print('X won')
        print_board(temp_board)
        break

    elif temp_board['mid_L'] == 'X' and temp_board['mid_M'] == 'X' and temp_board['mid_R'] == 'X':
        print_board(temp_board)
        print('X won')
        break

    elif temp_board['low_L'] == 'X' and temp_board['low_M'] == 'X' and temp_board['low_R'] == 'X':
        print_board(temp_board)
        print('X won')
        break
    elif temp_board['top_L'] == 'X' and temp_board['mid_M'] == 'X' and temp_board['low_R'] == 'X':
        print_board(temp_board)
        print('X won')
        break
    elif temp_board['top_R'] == 'X' and temp_board['mid_M'] == 'X' and temp_board['low_L'] == 'X':
        print_board(temp_board)
        print('X won')
        break

    elif temp_board['top_L'] == 'O' and temp_board['top_M'] == 'O' and temp_board['top_R'] == 'O':
        print('O won')
        print_board(temp_board)
        break

    elif temp_board['mid_L'] == 'O' and temp_board['mid_M'] == 'O' and temp_board['mid_R'] == 'O':
        print_board(temp_board)
        print('O won')
        break

    elif temp_board['low_L'] == 'O' and temp_board['low_M'] == 'O' and temp_board['low_R'] == 'O':
        print_board(temp_board)
        print('O won')
        break
    elif temp_board['top_L'] == 'O' and temp_board['mid_M'] == 'O' and temp_board['low_R'] == 'O':
        print_board(temp_board)
        print('O won')
        break
    elif temp_board['top_R'] == 'O' and temp_board['mid_M'] == 'O' and temp_board['low_L'] == 'O':
        print_board(temp_board)
        print('Owon')
        break
print("It's a draw!")
