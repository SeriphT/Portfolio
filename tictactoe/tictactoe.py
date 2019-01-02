
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
X = "X"
O = "O"
def display_instructions():
    ###Displays instructions###
    
    print("Welcome to  Tic-Tac-Toe")
    print("Have you come to beat me?\n Well you can certainly try...")

    print("\nInstructions:")
    print(" Enter a choice of if you start first or the computer.\n Enter a move by using numbers 0-8 \n Continue until you win, lose, or tie with the computer")
    print(
        """\n\nHERE IS THE BOARD
                    0|1|2
                    -----
                    3|4|5
                    -----
                    6|7|8
                    """)
    print("Let's see what you can do, human...")


def ask_yes_no(question):
    ###asks yes or no question###
    response = None
    while response not in ("yes" , "no"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    ###asks for a number 0-8 from user###
    response = None
    while response not in range(low, high):
        response = input(question)
        if response.isdigit():
            response = int(response)
            return response

def pieces():
    ###defines who goes first###
    human = None
    computer = None
    go_first = ask_yes_no("Do you want to go first?")
    if go_first == "yes":
            human = X
            computer = O
    else:
             human = O
             computer = X
    return human, computer
    
def new_board():
    ###makes a blank board for a new game###
    board =[]
    for sqr in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    ###displays current state of board###
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print(" \t-----------")
    print("\n\t",board[3],"|",board[4],"|",board[5])
    print("\t-----------")
    print("\n\t",board[6],"|",board[7],"|",board[8],"\n")

def legal_move(board):
        ###defines all legal moves/free spaces on the board###
        moves = []
        for sqr in range(NUM_SQUARES):
            if board[sqr] == EMPTY:
                moves.append(sqr)
        return moves

def winner(board):
    ###defines winner###
    winner = "i"
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def human_move(board, human):
    ###defined human turn###
    legal = legal_move(board)
    move = None
    while move not in legal:
        move = ask_number("Where do you want to play? Enter 0-8", 0, NUM_SQUARES)
        if move not in legal:
            print("You dumb human, that's not a legal move. Try again.")
    print("Well done...")
    return move
        
def computer_move(board, computer, human):
    ###defines computer move###
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I will take square",end=" ")
    for move in legal_move(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_move(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
        for move in BEST_MOVES:
            if move in legal_move(board):
                print(move)
                return move
            
def next_turn(turn):
    ###makes turn switches###
    if turn == X:
        return O
    else:
        return X
    
def grats_winner(winner, computer, human):
    ###congratulates winner###
    if winner != TIE:
        print("The winner is:",winner,"!")
    else:
        print("It was a tie!")
        
    if winner == computer:
        print("You couldn't beat me if you tried!")
    elif winner == human:
        print("I bet you couldn't do it again...")
    elif winner == TIE:
        print("Lucky... celebrate while you can, human... I'll be back.")

def main():
    display_instructions()
    turn = X
    h,c = pieces()
    board = new_board()
    while EMPTY in board and winner == "i":
        if h == X:
                display_board(board)        
                move = human_move(board, h)
                board[move] = h
                next_turn(turn)
        else:
                move = computer_move(board, c, h)
                display_board(board)
                board[move] = c 
                next_turn(turn)
        winner(board)
    if EMPTY not in board:
        grats_winner(winner, c, h)

main()
