from board import *
from minimax import *

# human player agent
def player(game_board, my_score, agent_score, max_ply):

    move_valid = False

    # while loop to ensure a valid entry by the player
    while not move_valid:
        row_move = input("please enter a row number: ")
        col_move = input("Please enter a column number: ")

        # ensure it is numeric
        if row_move.isnumeric() and col_move.isnumeric():
            row_move = int(row_move)
            col_move = int(col_move)
        
        if isinstance(row_move, int) or isinstance(col_move,int):

            # check that the move is valid
            if game_board.valid_move(col_move, row_move):

                # update the board and score with the move 
                my_score = my_score + game_board.player_move(col_move, row_move)

                # print the new state of the board
                game_board.draw_board()
                print("You made a move. Current Scores:\nPlayer: {} \nAgent: {} ".format(my_score, agent_score))
                move_valid = True
            else:
                print("Invalid move. Please try again.")
        else:
            print("Invalid move. Please try again.")
    
    return my_score
    
# AI agent
def agent(game_board, agent_score, my_score, max_ply):
    
    # call the minimax to detirmine the next move
    moves = minimax(game_board, max_ply)
    print("AI move: ", moves)

    #update the board state and score
    agent_score = agent_score + game_board.player_move(moves[0], moves[1])

    # show the new board state
    game_board.draw_board()
    print("AI made a move. Current Scores:\nPlayer: {} \nAgent: {} ".format(my_score, agent_score))
    
    return agent_score

#compare score and print out who won
def winner(my_score, agent_score):
    if my_score > agent_score:
        print("Congrats! You won with a final score of {} and the agent with {}".format(my_score, agent_score))
    elif agent_score > my_score:
        print("Unfortunately, you lost to the computer with a score of {} and you had {}".format(agent_score, my_score))
    else:
        print("Looks like this is a stalemate. Your score: {} Agent score: {}".format(my_score, agent_score))

# Start the game and ask the human player for dims of the board and how many levels of ply
def start_game():
    
    ply = 0

    #initializing the main vars
    rows = int(input("Please enter the number of rows of boxes: "))
    cols = int(input("Please enter the number of columns of boxes: "))

    # ensure that the min ply is 2
    while ply < 2:
        ply = int(input("Please enter the max ply for the AI agent: "))
        if ply < 2:
            print("Minimum ply is 2. Please try again.")

    # construct board obj and return it and the ply
    game = Board(rows,cols, None)

    return game, ply