print "welcome to my board"


def print_horiz_line():
    print " ---" * board_size

def print_vert_line():
    print ("|   " * (board_size + 1))

board_size = int(raw_input("enter size of board:"))

def create_board():

    for index in range(board_size):

        print_horiz_line()
        print_vert_line()
    print_horiz_line()

create_board()
