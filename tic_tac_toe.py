# TIC-TAC-TOE

def display_board(the_board):
    #display the 3X3 TIC-TAC-TOE Board
    from IPython.display import clear_output
    clear_output()
    
    print (f'{the_board[6]} |  {the_board[7]} | {the_board[8]}')
    print ('--  ' + '--  ' + '-- ')
    print (f'{the_board[3]} |  {the_board[4]} | {the_board[5]}')
    print ('--  ' + '--  ' + '-- ')
    print (f'{the_board[0]} |  {the_board[1]} | {the_board[2]}')


def choose_turn():
    #Random number to pick who goes firstm, if 0 player 1 goes first
    
    import random
    num = random.randint(0,1)
    if num == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def select_marker():
    # player selects marker

    set_marker = False
    
    while(not set_marker):
        pl1 = input('Player 1: Please select your marker 0 or X ')

        if pl1 == '0':
            pl2 = 'X'
            set_marker = True
        elif pl1 == 'X':
            pl2 = '0'
            set_marker = True
        else:
            print('Please enter correct marker!')
    return(pl1,pl2)


   
def check_slot_availability(position, the_board):
    #check if the position on the board is empty
    return (the_board[position] != '0') and (the_board[position] != 'X')
       

def place_marker_on_board(marker, position, the_board):
    #code to place the marker on board
    the_board[position] = marker
      
    
def win_check(marker, the_board):
    # Check if the player has won
    
    #check the three rows, then 3 colums, then 2 diag
    return (the_board[0] == the_board[1] == the_board[2] == marker or
        the_board[3] == the_board[4] == the_board[5] == marker or
        the_board[6] == the_board[7] == the_board[8] == marker or
        the_board[0] == the_board[3] == the_board[6] == marker or
        the_board[1] == the_board[4] == the_board[7] == marker or
        the_board[2] == the_board[5] == the_board[8] == marker or
        the_board[0] == the_board[4] == the_board[8] == marker or
        the_board[2] == the_board[4] == the_board[6] == marker)
        
     
def reset_board(the_board):
    the_board = [' ']*9
    return the_board

def is_board_full(the_board):
    #check the stalemate condition
    
    for item in range(0,9):
        if the_board[item] != 'X' and the_board[item] != '0':
            return False
        
    return True
        

#################



# GamePlay

the_board = [' ']*9
play_game = True
game_complete = False
#correct_slot = False
want_to_play = input('Welcome to TIC-TAC-TOE! Do you want to Play (Y/N)')

if want_to_play == 'Y':
    while(play_game):
        pl1_marker, pl2_marker = select_marker() 
        
        
        turn = choose_turn()
        if turn == 'Player 1':
            print(f'{turn} Goes First, Your Marker is {pl1_marker}')
            player = 1
        else:
            print(f'{turn} Goes First, Your Marker is {pl2_marker}')
            player = 2

        input("Press any Key to Begin the Game")
        
        while(not game_complete):
            if player == 1:
                correct_slot = False
                while(not correct_slot):
                    display_board(the_board)
                    pos = int(input("Enter the Postiion on board [1-9]"))
                    correct_slot = check_slot_availability(pos-1, the_board)
                    if(not correct_slot):
                        print('Wrong Slot!! Try Again!')
                place_marker_on_board(pl1_marker, pos-1, the_board)
                display_board(the_board)
                if(win_check(pl1_marker, the_board)):
                    print('Player 1 has Won')
                    game_complete = True
                    break
                elif not is_board_full(the_board):
                    player = 2
                else:
                    print("GameOver It's a Tie")
                    break
            else:
                correct_slot = False
                while(not correct_slot):
                    display_board(the_board)
                    pos = int(input("Enter the Postiion on board [1-9]"))
                    correct_slot = check_slot_availability(pos-1, the_board)
                    if(not correct_slot):
                        print('Wrong Slot!! Try Again!')
                place_marker_on_board(pl2_marker, pos-1, the_board)
                display_board(the_board)
                if(win_check(pl2_marker, the_board)):
                    print('Player 2 has Won')
                    game_complete = True
                    break
                elif not is_board_full(the_board):
                    player = 1
                else:
                    print("GameOver It's a Tie")
                    break

        play_again = input ('Do you want to play again!! [Y/N]')

        if play_again == 'N':
            play_game = False
            print('Bye')
            break
        else:
            game_complete = False
            the_board = reset_board(the_board)
else:
    print('Bye')
            
    