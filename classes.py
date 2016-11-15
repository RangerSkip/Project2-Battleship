from battleship import clear_screen
import pdb
import re
import sys

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

SHIP_INFO_MOD = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

class Player(object):


    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.score = 0
        self.ships_sunk = 0
        self.guesses = []

    def guess(self, Board, Ship):
        Board.print_board()
    # Validating for guesses
        guess = self.target_check()
        x = ord(guess[:1])-97
        y = int(guess[1:])-1
        hit = 0

        clear_screen()

    # Hit or Miss
        for item in Ship.ships:
            if guess in Ship.ships[item]["Coordinates"]:
                hit = 1
                Board.board[y][x] = "*"
                Ship.ships[item]["Coordinates"][guess] = '*'
                Board.print_board()
                print("You hit the {} at {}!".format(item, guess))
                if all(value == '*' for value in Ship.ships[item]["Coordinates"].values()):
                    sunk = list(Ship.ships[item]["Coordinates"].keys())
                    for a in Ship.ships[item]["Coordinates"]:
                        Ship.ships[item]["Coordinates"][a] = '#'
                    for b in sunk:
                        y = int(b[1:])-1
                        x = ord(b[:1])-97
                        Board.board[y][x] = '#'
                    print("You sunk their {}!".format(item))
                    self.ships_sunk += 1
                    Board.print_board()
        if hit == 0:
            Board.board[y][x] = '.'
            Board.print_board()
            print("Miss!")

    # Win Condition
        if self.ships_sunk == len(SHIP_INFO):
            self.victory()



    def target_check(self):
    # target needs to be between a1 and j10
        target = input("{}, please pick a target: ".format(self.name)).lower().replace(" ","")
        x = ord(target[:1])-97
        y = int(target[1:2])-1
    # checking in bounds
        while x >= 10 or y >= 10:
            print("{} is an invalid target.".format(target))
            self.target_check()
    # checking if already guessed
        if target in self.guesses:
            print("{}, you have already guessed {}.".format(self.name, target))
            self.target_check()
        else:
            self.guesses.append(target)
        return target


    def victory(self):
        print("Congratulations {}! You sunk all of your opponents ships!".format(self.name))
        print("{} is Victorious!!".format(self.name))
        VICTORY = True




class Ship(object):

    def __init__(self):
        self.ships = {}
        self.coordbank = []

    def make_ships(self, name, length, position, orientation, Board):
        self.ships[name] = {"length": length, "Coordinates": {}}
        x = ord(position[:1])
        y = int(position[1:])
        coords = {}

        if orientation.lower() == "y":
            for i in range(0, length):
                place = ''.join([chr(x), str(y)])
                coords[place] = "-"
                x = x + 1
        elif orientation.lower() == "n":
            for i in range(0, length):
                place = ''.join([chr(x), str(y)])
                coords[place] = "|"
                y = y + 1
        # Validating for ship overlap
        names = []
        for item in self.ships:
            names.append(item)
        for var in names:
            for item in coords.keys():
                while item in list(self.ships[var]["Coordinates"].keys()) and self.ships[name] != self.ships[var]:
                    Board.print_board()
                    new_position = input("There is an overlap at {}. Please enter a different starting position: ".format(item)).replace(" ","")
                    new_orientation = input("Is it horizontal? (Y/N): ").replace(" ","")
                    clear_screen()
                    self.make_ships(name, length, new_position, new_orientation, Board)
                    return
        for item in self.ships[name]["Coordinates"]:
            self.coordbank.append(item)
            print(self.coordbank)

        self.ships[name]["Coordinates"] = coords

    def clear_ships(self):
        for item in self.ships:
            self.ships[item] = {"length": 0, "Coordinates": {}}


class Board(object):
    def __init__(self):
        self.board = [[EMPTY for x in 'abcdefghij'] for y in range(BOARD_SIZE)]

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

    def print_board(self):
        self.print_board_heading()

        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1


    def update_board(self, Ship):
        # k = x, v = y
        for item in Ship.ships:
            for k,v in Ship.ships[item]["Coordinates"].items():
                x = ord(k[:1])-97
                y = int(k[1:])-1

                self.board[y][x] = v

        clear_screen()
        self.print_board()

    def make_ships(self, Ship, Player):
        for item in SHIP_INFO:
            position = input("{}, Place the location of the {} ({} spaces): "
                            .format(Player.name, item[0], item[1])).lower().replace(" ","")
            x = ord(position[:1])-97
            y = int(position[1:3])-1
            while x >= 10 or y >= 10:
                position = input("{}, {} will not work, please pick a new location: ".format(Player.name, position))
                x = ord(position[:1])-97
                y = int(position[1:2])-1
            orientation = input("Is it horizontal? (Y/N): ").lower().replace(" ","")
            orientation = orientation[:1]

        # Validating for out of bounds ship placement

            while x + int(item[1]) >= 10 and orientation == 'y':
                clear_screen()
                self.print_board()
                position = input("{}, {} is invalid (out of bounds). Place the location of the {} ({} spaces): "
                                .format(Player.name, position, item[0], item[1])).lower().replace(" ","")
                orientation = input("Is it horizontal? (Y/N): ").lower().replace(" ","")
            while y + int(item[1]) >= 10 and orientation == 'n':
                clear_screen()
                self.print_board()
                position = input("{}, {} is invalid (out of bounds). Place the location of the {} ({} spaces): "
                                .format(Player.name, position, item[0], item[1])).lower().replace(" ","")
                orientation = input("Is it horizontal? (Y/N): ").lower().replace(" ","")
            while orientation != 'y' and orientation != 'n':
                orientation = input("{} is not a valid input. Is it horizontal? (Y/N): ").lower().replace(" ","")
            orientation = orientation[:1]

            Ship.make_ships(item[0], item[1], position, orientation, self)
            self.update_board(Ship)
