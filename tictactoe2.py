board = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
winner = None


def play():
    global winner
    print("Start the game!")
    see_board()
    for i in range(5):
        print("player 1 turn - X")
        value = "X"
        #empiezan a jugar - Jugador1
        match(value)
        winner_is()
        if winner != "X" and i < 4:
            for j in range(3):
                print("player 2 turn - O")
                value = "O"
                match(value)
                winner_is()
                if winner == "O":
                    print("Congratulations!!! Player 2 WINNER of TICTACTOE")
                break
        elif winner == "X":
            print("Congratulations!!! Player 2 WINNER of TICTACTOE")
            break
        else:
            print("You tied the TICTACTOE")


def winner_is():
    global winner
    line_control()
    Verticalcontrol()
    Diagonalcontrol()


def line_control():
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]


def Verticalcontrol():
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]


def Diagonalcontrol():
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]


def match(value):
    point = False
    while point == False:
        posision = int(input("choose a posicion from 1 to 9: "))
        posision -= 1
        if board[posision] == "-":
            point = True
        else:
            print("THE POSISION IS OCCUPIED")
    board[posision] = value
    see_board()


def see_board():
    print("\n")
    print(board[0] + " | " + board[1] +
          " | " + board[2] + "       1 | 2 | 3")
    print(board[3] + " | " + board[4] +
          " | " + board[5] + "       4 | 5 | 6")
    print(board[6] + " | " + board[7] +
          " | " + board[8] + "       7 | 8 | 9")
    print("\n")


play()



