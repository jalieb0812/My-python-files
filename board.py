
game_board = [["x", "x", "x"],
              ["x", "x", "x"],
              ["x", "x", "x"]]

spots_on_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def tic_tac_toe():
    print"\n"
    print "Below is the game board. I drew it myself. Instructions for playing are below \n"

    print game_board[0][0:3]
    print game_board[1][0:3]
    print game_board[2][0:3]

    print """\n Welcome to my first programed game: Tic Tac Toe. The rules are as
    follows. You must enter a number 0, 1, 2 for the row and then 0, 1, 2
    for the column. If you enter any other numbers this game will stop
    Most of all i made this during work. ENJOY! \n

    P.S. NO MOKNEYING AROUND :) \n"""
    while quit != "enter":

        player_one_choice_row = int(raw_input("\nplayer one choose your row 0 - 2: "))
        while True:
            if player_one_choice_row == 1 or player_one_choice_row == 0 \
                or player_one_choice_row == 2:
                    break

            else:
                print "\nNo. you can only choose '0' '1' or '2'. choose again \n"
                player_one_choice_row = int(raw_input("\nplayer one choose your row 0 - 2: "))

        player_one_choice_column = int(raw_input("\nplayer one choose your column 0 - 2: "))

        while True:
            if player_one_choice_column == 1 or player_one_choice_column == 0 \
            or player_one_choice_column == 2:
                break

            else:
                print "\nNo. you can only choose '0' '1' or '2'. choose again \n"
                player_two_choice_row = int(raw_input("\nplayer two choose your row 0 - 2: "))

        while game_board[player_one_choice_row][player_one_choice_column] == "1" \
        or game_board[player_one_choice_row][player_one_choice_column] == "2":
            print "\nSorry, that spot was chosen already. pick again. \n"
            player_one_choice_row = int(raw_input("\nplayer one choose your row 0 - 2: "))
            player_one_choice_column = int(raw_input("\nplayer one choose your column 0 - 2: "))

        game_board[player_one_choice_row][player_one_choice_column] = "1"



        if game_board[0][0:3] == ["1", "1", "1"]:
            print "\nplayer one wins"
            break

        if game_board[1][0:3] == ["1", "1", "1"]:
            print "\nplayer one wins"
            break

        if game_board[2][0:3] == ["1", "1", "1"]:
            print "\nplayer one wins"
            break


        if game_board[0][0] == "1" and game_board[1][0] == "1" and \
        game_board[2][0] == "1":
            print "\nplayer one wins"
            break

        if game_board[0][1] == "1" and game_board[1][1] == "1" and \
        game_board[2][1] == "1":
            print "\nplayer one wins"
            break


        if game_board[0][2] == "1" and game_board[1][2] == "1" and \
        game_board[2][2] == "1":
            print "\nplayer one wins"
            break


        if game_board [0][0] == "1" and game_board[1][1] =="1" and \
        game_board[2][2] == "1":
            print "\nplayer one wins"
            break


        if game_board [0][2] == "1" and game_board[1][1] == "1" and \
        game_board[2][0] == "1":
            print "\nplayer one wins"
            break

        print "\n clever pick\n"

        print "the board looks as follows \n"
        print game_board[0][0:3]
        print game_board[1][0:3]
        print game_board[2][0:3]

        print "\nplayer two you are up!\n"



        player_two_choice_row = int(raw_input("\nplayer two choose your row 0 - 2: "))

        while True:
            if player_two_choice_row == 1 or player_two_choice_row == 0 \
            or player_two_choice_row == 2:
                break

            else:
                print "\nNo. you can only choose '0' '1' or '2'. choose again \n"
                player_two_choice_row = int(raw_input("\nplayer two choose your row 0 - 2: "))

        player_two_choice_column = int(raw_input("\nplayer two choose your column 0 - 2: "))

        while True:
            if player_two_choice_column == 1 or player_two_choice_column == 0 \
            or player_two_choice_column == 2:
                break

            else:
                print "\nNo. you can only choose '0' '1' or '2'. choose again \n"
                player_two_choice_column = int(raw_input("\nplayer two choose your column 0 - 2: "))



        while game_board[player_two_choice_row][player_two_choice_column] == "1" \
        or  game_board[player_two_choice_row][player_two_choice_column] == "2":

            print "\nSorry, that spot was chosen already. pick again. \n "

            player_two_choice_row = int(raw_input("\nplayer two choose your row 0 - 2: "))
            player_two_choice_column = int(raw_input("\nplayer two choose your column 0 - 2: "))


        game_board[player_two_choice_row][player_two_choice_column] = "2"
        if game_board[0][0:3] == ["2", "2", "2"]:
            print "\nplayer two wins\n"
            break

        if game_board[1][0:3] == ["2", "2", "2"]:
            print "\nplayer two wins\n"
            break

        if game_board[2][0:3] == ["2", "2", "2"]:
            print "\nplayer two wins\n"
            break


        if game_board[0][0] == "2" and game_board[1][0] == "2" and \
        game_board[2][0] == "2":
            print "\nplayer two wins\n"
            break

        if game_board[0][1] == "2" and game_board[1][1] == "2" and \
        game_board[2][1] == "2":
            print "\nplayer two wins\n"
            break

        if game_board[0][2] == "2" and game_board[1][2] == "2" and \
        game_board[2][2] == "2":
            print "player two wins"
            break


        if game_board [0][0] == "2" and game_board[1][1] == "2" and \
        game_board[2][2] == "2":
            print "\nplayer two wins\n"
            break

        if game_board [0][2] == "2" and game_board[1][1] == "2" and \
        game_board[2][0] == "2":
            print "\nplayer two wins\n"
            break

        print "\n clever pick\n"

        print "\nthe board looks as follows \n"

        print game_board[0][0:3]
        print game_board[1][0:3]
        print game_board[2][0:3]

tic_tac_toe()

play_again = raw_input("\nto quit the game type 'quit' or 'play' to keep playing: \n")
if play_again == "quit":
    print "\nok. peace\n"
else:
    if play_again =="play":
        tic_tac_toe()


print game_board[0][0:3]
print game_board[1][0:3]
print game_board[2][0:3]
