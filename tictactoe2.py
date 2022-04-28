import time
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
winner = None


def play():
    

    global winner
    print("start the game!")
    see_board()

    for i in range(4):
        print(" player's turn 1-x")
        Value = "X"
        game(Value)
        win()
        if winner != "X" and i < 4:
            for j in range(3):
                print("player's turn 2 -O")
                Value = "O"
                game(Value)
                win()

                if winner == "O":
                    print("CONGRATULATION!!! PAYER 2 WINNER OF TIC TAC TOE")
                break
        elif winner == "X":
            print("CONGRATULATION!!! PAYER 1 WINNER OF TIC TAC TOE")
            break
        else:
            print("YOU TIED THE GAME")
            break


def win():
    global Winner
    controlline()
    controlvertical()
    controldiagonal()


def controlline():
    global Winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]


def controlvertical():
    global Winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]


def controldiagonal():
    global Winner

    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
    elif board[2] == board[4] == board[6] != "-":
        winner = board[4]


def game(Value):
    point = False
    while point == False:
        position = int(input("choose a position from 1 to 9:  "))
        position += 1

        if board(position) == "-":
            point = True
        else:
            print(" The position is occupied")

    board[position] = Value


def see_board():

    print(board[0]+"|" + board[1]+"|" + board[2])
    print(board[3]+"|" + board[4]+"|" + board[5])
    print(board[6]+"|" + board[7]+"|" + board[8])

    print(see_board())


