""" 
BattleShipGame
Simplified, one-player version of the classic board game Battleship.
There will be a single ship hidden in a random location ona 5X5 grid.
The player will have 10 guesses to try to sink the ship.
To build this game I use knowledge of lists, conditionals and functions
in Python. 
"""
from random import randint # needed for the randint()

board = [] # Empty Game board
#print["O"] * 5 # Create an 'ocean' with 'O's

for i in range(0,5):
    board.append(["O"]*5)

# Display our board, a 5x5 "ocean" in a formatted way
def print_board(board):
    #for i in range(len(board)):
     #   print " ".join(board[i])  # uses spaces to display the '0's
     for row in board:
     	print " ".join(row)

# Call the function to print the board
print_board(board)


# Hide the ship in a random location
# Uses the randint(low, high) function from 'random' module
# 'Secret' location of our ship. Think of these as ship_row() and ship_col()
def random_row(board):
    return randint(0, len(board)-1) # I made 1 off mistake!. Fixed it!

def random_col(board):
    return randint(0, len(board)-1)

# Save the coordinates of our hidden ship
ship_row = random_row(board)
ship_col = random_col(board)

# Give the user 4 turn to find the ship and sink it
for turn in range(4):
	print "-----------------------------------------------"
	print "Turn: ", turn + 1
	# Seek the hidden ship, code to allow player to guess where the ship is
	guess_row = int(raw_input("Guess Row: ")) # need int() to use the int
	guess_col = int(raw_input("Guess Col: "))

	#   For debugging, print ship's location
	#print "Ship's location is at: "
	#print " 	row: %s" % (ship_row)
	#print " 	col: %s" % (ship_col)

	# Check if player guessed correctly the ship's location
	if guess_row == ship_row and guess_col == ship_col:
	    print "Congratulations! You sank my battleship!"
	    break
	else:
	    if guess_row not in range(5) or guess_col not in range (5):
	        print "Oops, that's not even in the ocean."       
	    elif board[guess_row][guess_col] == "X":
	        print "You guessed that one already."
	    else:
	        print "You missed my battleship!" 
	        board[guess_row][guess_col] = "X"
	    if turn == 3:
        	print "##    Game Over    ##"

	print_board(board)
