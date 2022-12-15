from board import *
import copy
import math

# main minimax method

def minimax(current_state, max_ply):
    
    # initialize the best move
    best_move = []

    # create a copy of teh custom object
    temp_state = copy.deepcopy(current_state)

    # start the search for best move with maximum
    value, best_move =maximum(temp_state, max_ply, 1, None, -math.inf, math.inf, 0)

    # return the best move 
    return best_move

# maximum method
def maximum(board, max_ply, current_ply, child, alpha, beta, current_total):

    # starting position for the max score
    max_score = -math.inf

    # ensure there is always a move to be returned
    move = child
    
    # check if there are any move left to be played and if so return the current total and the child passed down
    if not board.moves_left():
        return current_total, child

    #when the current ply is greater than max ply
    if current_ply > max_ply:
        temp_state = copy.deepcopy(board)

        #set the max_score to the current total
        max_score = current_total

        # return the max score and child
        return max_score, child

    # call to find all the children based on the current position of the board
    children = board.find_children()

    # iterate through all the children
    for child in children:
        
        # check if the move is none and that the child to be evaluated exists
        if move == None and not child == None:
            move = child

        # copy the board
        temp_state = copy.deepcopy(board)

        # get the score based on this move (child)
        temp_score = temp_state.player_move(child[0],child[1]) 

        # var to hold the total score to this point
        next_current_total = current_total + temp_score

        # call the minimum method and return its score
        result, action = minimum(temp_state, max_ply, current_ply+1, child, alpha, beta, next_current_total)

        # if the result is greater than the max score, then update that score and move 
        if (result) > max_score:

            max_score = (result)
            move = child

            # update alpha if it is less than max score
            if alpha < max_score:
                alpha = max_score

        # check to see if the max score is greater or equal to the beta
        # return the max score and move as this line of search is no longer required
        # as this score would never be picked by the minimum method 
        if max_score >= beta:
            return max_score, move

    # return the max score and best move
    return max_score, move

# minimum method 
def minimum(board, max_ply, current_ply, child, alpha, beta, current_total):

    # starting position for the min score
    min_score = math.inf
    
    # ensure there is always a move to be returned
    move = child

    # check if there are any move left to be played and if so return the current total and the child passed down
    if not board.moves_left():
        return current_total, child

    #when the current ply is greater than max ply
    if current_ply > max_ply:
        temp_state = copy.deepcopy(board)

        #set the min score to the current total
        min_score = current_total

        # return the min score and child
        return min_score, child

    # call to find all the children based on the current position of the board
    children = board.find_children()

    # iterate through all the children
    for child in children:

        # create a copy of the current board
        temp_state = copy.deepcopy(board)

        # get the resulting value of the move (child) 
        temp_score = temp_state.player_move(child[0],child[1])

        # var to hold the updated current total -
        # Since this is a min method, we subtract the score of the move from teh current total passed down 
        next_current_total = current_total - temp_score

        # call the max method and get the resulting value
        result, action = maximum(temp_state, max_ply, current_ply+1, child, alpha, beta, next_current_total)

        # update the min score and teh child if less than the current min score
        if (result ) < min_score:
            min_score = (result)
            move = child

            # update beta value if it is greater than the current min score
            if beta > min_score:
                beta = min_score
        # check to see if min score is less than or equal the current alpha
        # allows for an early return since it is not needed to continue searching 
        # since this score would never be picked by the max method  
        if min_score <= alpha:
            return min_score, move

    # return the min score and best move
    return min_score, move
        

