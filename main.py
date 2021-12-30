import time


class Board():
    '''Creating game grid.'''
    def __init__(self):
        self.variables = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

    def __str__(self):
        self.structure = "     1|    2|    3\n" \
                         f"   {self.variables[0]}  |  {self.variables[1]}  |  {self.variables[2]}" \
                         f"\n" \
                         f" _____|_____|_____\n     4|    5|    6\n" \
                         f"   {self.variables[3]}  |  {self.variables[4]}  |  {self.variables[5]}" \
                         f"\n " \
                         f"_____|_____|_____\n     7|    8|    9\n" \
                         f"   {self.variables[6]}  |  {self.variables[7]}  |  {self.variables[8]}" \
                         f"\n" \
                         f"      |     |"
        return self.structure
    def change_variable(self,mark,place):
        self.variables[place-1] = mark

class Player():
    '''Creating player with all his methods.'''
    def __init__(self,number):
        self.number = number
        self.mark = ""
    def __str__(self):
        return f"Player {self.number}"
    def get_mark(self):
        '''Input method for selecting player mark.'''
        while True:
            result = input("Do you want to have Xs or Os? (Enter X/O): ")
            result = result.upper()
            if (result == "X" or result == "O"):
                self.mark = str(result)
            else:
                print("You entered something wrong, please enter X or O! ")
                continue
            print(f"Ok, you will have {result}s.")
            break
    def turn(self,board):
        '''Input method for selecting playing field in a grid.'''
        print(f"Player {self.number} is on turn... ")
        while True:
            try:
                place = int(input("Enter a number of space in the grid (1-9): "))
            except:
                print("You did not enter number! ")
            else:
                if (place > 9) or (place < 1):
                    print("Wrong number! You must enter number between 1 and 9. ")
                    continue
                elif is_occupied(place, board):
                    print("Wrong number! This place is already occupied! ")
                    continue
                else:
                    board.change_variable(self.mark, place)
                    print(board)
                    break

    def win_check(self,board):
        if (board.variables[0:7:3]) == [self.mark, self.mark, self.mark]:
            print(f"Player {self.number} has won!")
            return True
        if (board.variables[1:8:3]) == [self.mark, self.mark, self.mark]:
            print(f"Player {self.number} has won!")
            return True
        if (board.variables[2:9:3]) == [self.mark, self.mark, self.mark]:
            print(f"Player {self.number} has won!")
            return True
        if (board.variables[0:9:4]) == [self.mark, self.mark, self.mark]:
            print(f"Player {self.number} has won!")
            return True
        if (board.variables[2:7:2]) == [self.mark, self.mark, self.mark]:
            print(f"Player {self.number} has won!")
            return True
        if (board.variables[0:3]) == [self.mark, self.mark, self.mark]:
            print(f"Player {self.number} has won!")
            return True
        if (board.variables[3:6]) == [self.mark, self.mark, self.mark]:
            print(f"Player {self.number} has won!")
            return True
        if (board.variables[6:9]) == [self.mark, self.mark, self.mark]:
            print(f"Player {self.number} has won!")
            return True
        return False





def second_player_mark(player1, player2):
    '''Method for giving second player remaining mark.'''
    if player1.mark == "O":
        player2.mark = "X"
    if player1.mark == "X":
        player2.mark = "O"
    print(f"Game is starting up! {player1} have {player1.mark}s and {player2} "
          f"have {player2.mark}s." )
def is_occupied(number, board):
    if board.variables[number-1] == "-":
        return False
    else:
        return True
def play_again():
    while True:
        try:
            play = input("Do you wanna play again with a new board? (Y/N) ")
            play = play.upper()
        except:
            print("Please type Y or N. ")
        else:
            if play == "Y":
                return True
            elif play == "N":
                print("Thanks for playing!")
                return False
            else:
                print("You typed bad character! ")
def tie_check(board):
    '''Checking if the grid is full.'''
    board_full = True
    for number in range(len(board.variables)):
        if not is_occupied(number,board):
            board_full = False
    if board_full:
        print("Board if full! It's a tie! ")
    return board_full



print("Welcome to Tic-Tac-Toe for two players! ")
playing = True
player1 = Player(1)
player2 = Player(2)
player1.get_mark()
time.sleep(2)
while playing:
    new_board = Board()
    print(new_board)
    second_player_mark(player1, player2)
    game_on = True
    while game_on:
        player1.turn(new_board)
        if player1.win_check(new_board):
            break
        if tie_check(new_board):
            break
        player2.turn(new_board)
        if player2.win_check(new_board):
            break


    playing = play_again()
