import random, time
from turtle import *

def setup_grid():
    for x in range(0, treasures): # place the treasures into the grid 
        treasure_number = starting_square # set value to illegal value so that a new position is picked
        while treasure_number == starting_square or grid[treasure_number] != -1: # run loop if picked square is initial starting square or already occupied by treasure / bandit
            treasure_number = random.randint(0, grid_size ** 2 - 1)
        grid[treasure_number] = 3 # set to 3 because so that every time it is landed, 1 is taken away from that number, and when it reaches a 0 It turns into a bandit

    for x in range(0, bandits): # place the bandits into the grid 
        bandit_number = starting_square # set value to illegal value so that a new position is picked
        while bandit_number == starting_square or grid[bandit_number] != -1:# run loop if picked square is initial starting square or already occupied by treasure / bandit
            bandit_number = random.randint(0, grid_size ** 2 - 1)
        grid[bandit_number] = 0

def display_grid():
    delay(0)
    speed(0) # to make the grid drawing quicker
    square_size = 50 # amount of pixels for 1 side of a square
    penup() # reposition the turtle to make board at the centre of the screen
    for x in range(0, 2): 
        left(90)
        forward(grid_size * square_size / 2)
    right(180) # makes turtle face correct direction
    pendown() # start drawing the grid
    for x in range(0, grid_size): # for number of rows
        for x in range(0, grid_size): # for number of columns
            for x in range(0, 4): # for number of sides in a square
                forward(square_size) # go forwards 1 length side of the square
                right(90)# turn the amount of degrees at a corner of a square
            forward(square_size) # go across to next column 
        backward(grid_size * square_size) # going to the beginning of the row
        right(90) # go down and reposition the turtle to make a new row
        forward(square_size)
        left(90)
    penup()
    forward(square_size / 2) # position the turtle in the centre of the starting square
    left(90)
    forward(square_size / 2)
    color("blue") # make player colour different to the grid colour
    return square_size


def menu():
    is_valid = False # set variable to an invalid state to force the while loop to do at least 1 run
    while is_valid == False: # to make the program more robust (from silly user comments)
        menu = input("Do you want to play or quit? Press ‘p’ to play and ‘q’ to quit: ")# stores the input of the user inside the variable menu to see if the user wants to play or quit
        menu = menu.lower()
        if menu == 'q': # python automatically closes if the user wants to quit
            print("Program is now closing, press ENTER to accept")
            time.sleep(2)
            exit()
        elif menu == 'p': # python starts the game by setting the treasure chests and the bandits places and displays the 8 by 8 grid using turtle graphics to show the user their position at any given time. 
            is_valid = True
        else:
            print("Option chosen is not valid, please try again") # if menu does not equal to ‘p’ or menu does not equal to ‘q’ then repeat the question until the user inputs a valid answer (because the computer cannot predict whether the user wants to play or quit)

def win_or_lose(coins, treasures):
    gameover = False # "gameover" variable is set to false unless the user finds 100 coins or if there are 0 treasures on the board
    if coins == 100: # player wins if he has 100 coins
        print("You Won!!!")
        gameover = True # if the player wins then the game finishes
    elif treasures == 0: # when you have less than 100 coins and all the treasures turned to bandits, then the player lost 
        print("You Lost…")
        gameover = True # if the player loses then the game finishes 
    return gameover # returns if the game is over


def move_and_validation(player_position, grid_size, square_size, moves):
    player_y = int(player_position / grid_size) # to find the y coordinate of the player
    player_x = int(player_position - player_y * grid_size) # to find the x coordinate of the player
    is_valid = False # set variable to an invalid state to force the while loop to do at least 1 run
    while is_valid == False: # to make the program more robust (from silly user comments)
        x_direction = input("Do you want to go left, right or neither? Press ‘l’ to go left, ‘r’ to go right and ‘n’ for neither: ")
        x_direction = x_direction.lower()
        if x_direction != 'r' and x_direction != 'l' and x_direction != 'n': # to make the program more robust (from silly user comments)
            print("That is not a valid option, please try again")
        elif player_x == 0 and x_direction == 'l' or player_x == grid_size - 1 and x_direction == 'r': # if player is at the boundary of the grid, they cannot move more in that direction 
            print("You must stay within the grid’s boundaries")
        else:
            is_valid = True # if the user entered a valid input, the program stops repeating the while loop
    x_multiplier = 0 # set a default value of 0 so that if the user chose neither, the calculations in the end of the function will still work
    if x_direction == 'r':
        x_multiplier = 1 # to do calculations without having to do different calculations depending on which direction the player is going
        right(90)  
    if x_direction == 'l':
        x_multiplier = -1 # to do calculations without having to do different calculations depending on which direction the player is going
        left(90)
    if x_direction == 'n':
        steps_x = 0 # if you go not left nor right, you will always go 0 steps and so no input needs to be done by the player
    else:
        is_valid = False # set variable to an invalid state to force the while loop to do at least 1 run
        while is_valid == False:
            steps_x = input("How many steps will you like to move? ")
            if not steps_x.isdigit(): # if the user input is not an integer then the steps taken is not a valid input
                print("Please enter a NUMBER: ")
            elif grid_size - 1 < int(steps_x) * x_multiplier + player_x or int(steps_x) * x_multiplier + player_x < 0: # makes sure that a number was entered and that it is in boundaries 
                print("Please try to stay within the grid's boundries")
            else:
                is_valid = True # if the user entered a valid input, the program stops repeating the while loop
        steps_x = int(steps_x) # to make the calculation part, python needs the number as an integer
        forward(steps_x * square_size) # move turtle to player’s request
    if x_direction == 'r': 
        left(90)  # return turtle facing upwards again
    if x_direction == 'l':
        right(90) # return turtle facing upwards again
    is_valid = False # set variable to an invalid state to force the while loop to do at least 1 run
    while is_valid == False: # to make the program more robust (from silly user comments)
        y_direction = input("Do you want to go up, down or neither? Press ‘u’ to go up, ‘d’ to go down and ‘n’ for neither: ")
        y_direction = y_direction.lower()
        if y_direction != 'u' and y_direction != 'd' and y_direction != 'n': # to make the program more robust (from silly user comments)
            print("That is not a valid option, please try again")
        elif player_y == 0 and y_direction == 'u' or player_y == grid_size - 1 and y_direction == 'd': # if player is at the boundary of the grid, they cannot move more in that direction 
            print("You must stay within the grid’s boundaries")
        else:
            is_valid = True # if the user entered a valid input, the program stops repeating the while loop
    y_multiplier = 0 # set a default value of 0 so that if the user chose neither, the calculations in the end of the function will still work
    if y_direction == 'd':
        y_multiplier = 1 # to do calculations without having to do different calculations depending on which direction the player is going
        right(180)  
    if y_direction == 'u':
        y_multiplier = -1 # to do calculations without having to do different calculations depending on which direction the player is going
    if y_direction == 'n':
        steps_y = 0 # if you go not up nor down, the player will always go 0 steps and so no input needs to be done by the player
    else:
        is_valid = False # set variable to an invalid state to force the while loop to do at least 1 run
        while is_valid == False:
            steps_y = input("How many steps will you like to move? ")
            if not steps_y.isdigit(): # if the user input is not an integer then the steps taken is not a valid input
                print("Please enter a NUMBER: ")
            elif grid_size - 1 < int(steps_y) * y_multiplier + player_y or int(steps_y) * y_multiplier + player_y < 0: # makes sure that a number was entered and that it is in boundaries 
                print("Please try to stay within the grid's boundaries")
            else:
                is_valid = True # if the user entered a valid input, the program stops repeating the while loop
        steps_y = int(steps_y) # to make the calculation part, python needs the number as an integer
        forward(steps_y * square_size) # move turtle to player’s request
    if y_direction == 'd': 
        left(180)  # return turtle facing upwards again
    player_position = player_position + steps_x * x_multiplier + steps_y * y_multiplier * grid_size # update the player’s position in the grid (list)
    return player_position

def update_game_state(player_position, coins, treasures, bandits):
    if grid[player_position] > 0: # checks if the square is a chest or not
        coins = coins + 10 # adds 10 coins to your coin counter since you found a treasure chest
        print("You have stepped on a treasure chest square, you found 10 coins") # prints appropriate message
        grid[player_position] = grid[player_position] - 1 # decreases number of times one can step on that specific chest before it turns into a bandit
        print("You may visit this chest", grid[player_position], "times before it turns into a bandit") # prints appropriate message
        if grid[player_position] == 0: # if the treasure just turned into a bandit by the player’s current move
            treasures = treasures - 1 # decrease number of treasures by 1
            bandits = bandits + 1 # increase number of bandits by 1
    elif grid[player_position] == 0: # checks if the square is a bandit
        coins = 0 # takes away all your coins since you stepped on a bandit
        print("You have stepped on a bandit, you have lost all of your coins") # prints appropriate message
    else: # if square is not treasure chest or bandit
        print("You have stepped on a neutral square") # prints appropriate message
    return coins, treasures, bandits

def display_status(coins, moves, treasures, bandits):
    print("You have", coins, "coins") # displays amount of coins player currently has
    print("You made", moves, "moves") # displays amount of moves player has made
    print("There are", treasures, "treasure chests on the grid") # displays amount of treasure chest squares on the grid
    print("There are", bandits, "bandits on the grid") # displays amount of bandits on the grid

menu() # runs the menu function to ask user if they want to start the game or quit
while True:
    is_all_valid = False # set to false to force the while loop to run at least once
    while is_all_valid == False: # to make the program more robust (from silly user comments)
        is_all_valid = True # set to true until and invalid input is made
        is_valid = False # set to false to force the while loop to run at least once
        while is_valid == False: # to make the program more robust (from silly user comments)
            grid_size = input("What do you want the grid size to be? Any option between 5 and 14 is valid: ") # user can input the grid size they want 
            if not grid_size.isdigit() or int(grid_size) < 5 or int(grid_size) > 14: # checks if the user input is an integer between 5 and 14
                print("Please enter a NUMBER between 5 and 14: ")
            else:
                is_valid = True # breaks out of the while loop
        is_valid = False # set to false to force the while loop to run at least once
        while is_valid == False: # to make the program more robust (from silly user comments)
            is_valid = True # set to true until and invalid input is made
            treasures = input("How many treasures do you want there to be? ")
            if not treasures.isdigit() or int(treasures) < 4: # checks if the user input is an integer over 3
                print("Please enter a NUMBER over 3: ")
                is_valid = False # repeats while loop until the user inputs a valid input
        is_valid = False # set to false to force the while loop to run at least once
        while is_valid == False: # to make the program more robust (from silly user comments)
            is_valid = True # set to true until and invalid input is made
            bandits = input("How many bandits do you want there to be? ")
            if not bandits.isdigit(): # checks if the user input is an integer
                print("Please enter a NUMBER: ")
                is_valid = False # repeats while loop until the user inputs a valid input
        grid_size = int(grid_size) # turns grid size variable into an integer
        treasures = int(treasures) # turns treasures variable into an integer
        bandits = int(bandits) # turns bandits variable into an integer
        if grid_size ** 2 -1 < treasures + bandits: # if number of chests + number of bandits is more than grid size squared -1 (otherwise will go into an infinate loop because cannot fit the treasures and bandits into the grid) 
            print("The number of treasures and bandits added together must be smaller than", grid_size**2 - 1)
            is_all_valid = False # set to false until a valid input is made
    coins = 0 # resets number of coins 
    moves = 0 # resets number of moves made
    grid = [-1 for i in range(0,grid_size ** 2)] # make a list (to represent the grid) full of -1s to represent the empty spaces in the grid
    starting_square = grid_size ** 2 - grid_size # the grid list begins its representation of the grid from the top left square and with each row in order, set the starting square to the bottom left square 
    player_position = starting_square # player starts on the starting square
    setup_grid() # sets up the grid
    square_size = display_grid() # displays the grid using turtle
    display_status(coins, moves, treasures, bandits) # displays the player's status
    gameover = False # gameover variable is set to false
    while gameover == False: # while the game is not finished
        print()
        player_position = move_and_validation(player_position, grid_size, square_size, moves) # changes player position according to user's inputs in the function "move_and_validation"
        moves = moves + 1 # increase number of moves by 1 after the move has been made
        coins, treasures, bandits = update_game_state(player_position, coins, treasures, bandits) # updates the coin number, treasure number and bandits number
        display_status(coins, moves, treasures, bandits) # displays the player's and game's status 
        gameover = win_or_lose(coins, treasures) # checks if the game is over
        print()
    reset() # once the game is over, it resets the turtle again
    menu() # asks the user whether they want to play again or not
