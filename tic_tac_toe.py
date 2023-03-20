import random

board = [' '] * 10
secondplayer = 'X'
firstplayer = 'O'


def display_board(board):
    print(f'{board[1]} | {board[2]} |{board[3]}')
    print(f'{board[4]} | {board[5]} |{board[6]}')
    print(f'{board[7]} | {board[8]} |{board[9]}')
    print('-' * 10)


def check_win():
    if board[1] == board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def check_draw():
    if board.count(' ') < 2:
        return True
    else:
        return False


def is_available(pos):
    return True if board[pos] == ' ' else False


def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        display_board(board)
        if check_win():
            if letter == 'X':
                print("Second Player Wins")
                print('*'*50)
                exit()
            else:
                print("First player wins")
                print('*'*50)
                exit()
        if check_draw():
            print("Draw")
            exit()
    else:
        if letter == 'O':
            pos = int(input("Not Free! Please re-enter a position: "))
        else:
            pos = random.randint(1, 9)
        insert(letter, pos)


def first_player(letter):
    pos = int(input("First player enter the position to insert:"))
    insert(letter, pos)
    print('-'*50)

def second_player(letter):
    pos = int(input("Second player enter the position to insert:"))
    insert(letter, pos)
    print('-'*50)

def secondplayer_move(letter):
    pos = random.randint(1, 9)
    insert(letter, pos)
    print('-'*50)


# main loop
print("1.2 players")
print("2.play with computer")
ch = int(input("Enter your choise: "))
print('-'*50)

if ch == 1:
    while not check_win():
        first_player(firstplayer)
        second_player(secondplayer)
        
elif ch == 2:
    while not check_win():
        # display_board(board)
        first_player(firstplayer)
        secondplayer_move(secondplayer)