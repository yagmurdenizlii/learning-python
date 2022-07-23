from random import Random
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:

    
    def __init__(self):
        #we'll initialize the board every time we create a new game
        self.board = [['_' for column in range(3)] for row in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))

    @staticmethod
    def print_board_nums():
        pass

    def available_moves(self):
        #return[] list of tuples

        moves = []
        for row in range(3):          
            for column in range(3):   
                if self.board[row][column] == '_':
                    moves.append((row, column))
        return moves

    def num_empty_squares(self):
        return len(self.available_moves())
        #we could also say self.board.count('_')
        


    def make_move(self, square_row, square_column, letter):
        if self.board[square_row][square_column] == '_':
            self.board[square_row][square_column] = letter
            if self.winner(square_row, square_column, letter):
                self.current_winner = letter
            return True
        return False

    
    def winner(self, square_row, square_column, letter):
        if all([letter == spot for spot in self.board[square_row]]):
            print('row')
            return True


        col = []
        for c in range(3):
            col.append(self.board[c][square_column])
        if all([letter == spot for spot in col]):
            print('col')
            return True  

        diag1 = []
        if square_row == square_column:         
            for i in range(3):
                diag1.append(self.board[i][i])
            if all([letter == spot for spot in diag1]):
                return True


        diag2 = []
        if square_row + square_column == 2: 
            for i in range(3):
                diag2.append(self.board[i][2 - i]) 

            if all([letter == spot for spot in diag2]):
                return True
        



def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board()
        
    letter = 'X'

    while game.num_empty_squares() > 0 and game.current_winner == None:
        
        if letter == 'O':
            square = o_player.get_move(game)  
        else:
            square = x_player.get_move(game)

        if game.make_move(square[0], square[1], letter):
            if print_game:
                print(letter + f' makes a move to square ({square[0]} , {square[1]})')
                game.print_board()
                print(' ')
            
            if game.current_winner != None:
                print(f'The winner is {letter} !')
                return letter

            #switching players
            letter = 'O' if letter == 'X' else 'X'

    #print('There is a tie!')
    return None

    
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)





