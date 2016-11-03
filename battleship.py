import classes
import sys

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

VICTORY = False

def clear_screen():
    print("\033c", end="")








if __name__ =='__main__':

# Player 1 setup
    name = input("Player 1, what is your name? ")
    p1 = classes.Player(name, 1)
    name = input("Player 2, what is your name? ")
    p2 = classes.Player(name, 2)

    p1_board = classes.Board()
    p1_guess_board = classes.Board()
    p1_board.print_board()
    p1_ships = classes.Ship()
    p2_board = classes.Board()
    p2_guess_board = classes.Board()
    p2_ships = classes.Ship()

    clear_screen()

    p1_board.make_ships(p1_ships)
    input("{}, when you are ready, press Enter and pass me to {}.".format(p1.name, p2.name))
    clear_screen()
    input("{}, press Enter when you are ready.".format(p2.name))

    clear_screen()

    p2_board.print_board()
    p2_board.make_ships(p2_ships)
    clear_screen()


# Begin the game

    while VICTORY == False:

        input("{}, when you are ready, press Enter and pass me to {}.".format(p2.name, p1.name))
        clear_screen()
        input("{}, press Enter when you are ready.".format(p1.name))

        print("Your board:")
        p2_guess_board.print_board()
        print("{}'s board:".format(p2.name))
        p1.guess(p1_guess_board, p2_ships)

        input("{}, when you are ready, press Enter and pass me to {}.".format(p1.name, p2.name))
        clear_screen()
        input("{}, press Enter when you are ready.".format(p2.name))

        print("Your board:")
        p1_guess_board.print_board()
        print("{}'s board:".format(p1.name))
        p2.guess(p2_guess_board, p1_ships)

    print("{}'s board: ".format(p1.name))
    p1_board.print_board()
    print("{}'s board: ".format(p2.name))
    p2_board.print_board()
    input("Press Enter to quit.".format())
