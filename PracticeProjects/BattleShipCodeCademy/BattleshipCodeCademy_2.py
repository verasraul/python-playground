from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#Debugger starts
#Prints ship coordinates.Remove hashtag
#print (ship_row)
#print (ship_col)
#Debugger ends

# Everything from here on should go in your for loop!
for turn in range(3):
        print ("Turn", turn + 1)
        break
# Be sure to indent four spaces!
guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))

if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")

else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print ("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
        print ("You guessed that one already.")
    else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
    #for turn in range(3):
    #    print ("Turn", turn + 1)
    #    break#
print_board(board)
