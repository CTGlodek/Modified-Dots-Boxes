# Student: Corey Glodek
# Class: CSC 480 
# Assignment 2: Modified Dots and Boxes
# 
# Board Class

import random
import copy

class Board:

    # define the attributes
    def __init__(self, rows, cols, board_state):
        self.rows = (rows*2)+1
        self.cols  = (cols*2)+1
        self.boxes = (rows) * (cols)
        board_state = board_state

    #construct the board based on the rows and columns
    def build_board(self): 
        self.board_state = []

        for i in range(0, self.rows):
            temp = []
            for j in range(0, self.cols):
                # assign a random number between 1 and 5
                if i % 2 == 1 and j % 2 ==1:
                    temp.append(random.randint(1,5))
                # insert an * if the location is an intersection
                elif i % 2 == 0 and j % 2 == 0:
                    temp.append('*')
                # leave everything else blank
                else:
                    temp.append(' ')
            self.board_state.append(temp)


    # draw the board 
    def draw_board(self):

        print("   ", end='')

        #print the column numbers with spacing
        for i in range(0, self.cols):
            print(str(i), end='  ')
        print()

        #print a straight line
        for i in range(0, self.cols):
            print("___", end='')    
        print()

        # print row wise through the list
        for j in range(self.rows):
            print(str(j) + "| ", end='')

            for k in range(self.cols):
                print(str(self.board_state[j][k]), end='  ')
            print()

        print("  ", end='')

        # close off the bottom of the board
        for i in range(0, self.cols):
            print("___", end='')
        print('\n')

    # Check to see if the move results in a completed box and if there are two boxes that are completed and return the score 
    def update_score(self, col, row):
        score = 0
        # horizontal check 
        if self.board_state[row][col] == '-':

            #first check if a box is completed away from the bottom board edge - checking up
            if row <= self.rows-2:
                if self.board_state[row+2][col] == '-' and self.board_state[row+1][col+1] =='|' and self.board_state[row+1][col-1] == '|':
                    score = score + self.board_state[row+1][col]

            #next check to see if a box was completed below the move made - checking down
            if row > 0:
                if self.board_state[row-2][col] == '-' and self.board_state[row-1][col+1] == '|' and self.board_state[row-1][col-1] == '|':
                    score = score + self.board_state[row-1][col]
        
        # Vertical check
        if self.board_state[row][col] == '|':

            # first check to see if the move completed a box to the right without exceeding the right edge of the board 
            if col <= self.cols - 2:
                if self.board_state[row][col+2] == '|' and self.board_state[row+1][col+1] =='-' and self.board_state[row-1][col+1] == '-':
                    score = score + self.board_state[row][col + 1]
            
            # next check to see if the move completed a box to the left without exceeding the left edge of the board
            if col >= 2:
                if self.board_state[row][col-2] == '|' and self.board_state[row + 1][col - 1] == '-' and self.board_state[row - 1][col -1] == '-':
                    score = score + self.board_state[row][col - 1]

        return score

    # Update the board with the players's move and return the updated score
    # rows are the y axis cols are the x axis
    def player_move(self, col, row):
        score = 0

        if col % 2 == 1 and row % 2 ==0:
            self.board_state[row][col] = '-'

        elif col % 2 == 0 and row % 2 == 1:
            self.board_state[row][col] = '|'

        # check to see if the move resulted in points
        score = self.update_score(col, row)

        return score
    
    # checking to ensure that the move requested is valid
    def valid_move(self, col, row):
        # check to ensure that teh move is not where an * or point number is located
        if col % 2 == 1 and row % 2 == 1: return False
        if col % 2 == 0 and row % 2 == 0: return False

        # ensure that the move is inside the bounds of the board
        if col > self.cols or col < 0: return False
        if row > self.rows or row < 0: return False

        # check to see if this move has already been performed
        if self.board_state[row][col] == '-' or self.board_state[row][col] == '|': return False

        return True
    
    # check to see if there are moves remaining to be played
    def moves_left(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board_state[i][j] == ' ':
                    return True
        return False

    # iterate through the board and see what moves are available for the current state and return the list of children
    def find_children(self):
        children = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.valid_move(j,i):
                    children.append([j,i])
        return children






