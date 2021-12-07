
import random
def initialiseGrid():
    grid = ["O" * 4] * 4  #4 rows by 5 columns grid for battleship
    for i in range(4):      #to avoid aliasing
            grid[i] = ["O"] * 4
    return grid

def displayGrid(grid):
    for row in grid:
        print("\t".join(row)+"\n")
        
def PresenceCheck(input_sofar, coord):
    #inputsofar is the list containing [row,col] lists that have been keyed in by the player before
    if coord in input_sofar and 0<=coord[0]<=3 and 0<=coord[1]<=3:
        return False
    return True

def validate(playercoord):
    if 0<=playercoord[0]<=3 and 0<=playercoord[1]<=3:
        return True
    return False 
    
def getInput(): #returns list of inputted row,col
    row = int(input("Enter row number (0 to 3):"))
    col = int(input("Enter col number (0 to 3):"))
    return [row,col]

def checkResult(playerCoord,Pirateship,won):
    if playerCoord in Pirateship : #player guessed correctly
        grid[playerCoord[0]][playerCoord[1]]= "P"
        for i in Pirateship:
            grid[i[0]][i[1]] = "P"  
        won = True
    else:
        grid[playerCoord[0]][playerCoord[1]] = "X" #player guessed wrongly
        won = False
    return won

def get_Pirateship(grid):#code randomly generates the pirate ship that the player is supposed to guess
    coordlst = []
    for row in range(4):
        for col in range(4):
            if 1<=row<=3 and 0<=col<=2:
                coord = row , col
                coordlst.append(list(coord))#nested list of coordinate lists
    rand_index = random.randint(0,(len(coordlst)-1))
    main_coord = coordlst[rand_index] #random [row, col] in strings 
    pirate_ship_lst = []
    pirate_ship_lst.append(main_coord)
    for i in pirate_ship_lst:
        main_coord2 =[(main_coord[0]-1),main_coord[1]]
        main_coord3 =[(main_coord[0]-1),(main_coord[1]+1)]
        main_coord4 =[main_coord[0],(main_coord[1]+1)]
    pirate_ship_lst.append(main_coord2)
    pirate_ship_lst.append(main_coord3)
    pirate_ship_lst.append(main_coord4)
    return pirate_ship_lst
    #returns list of 4 lists which are the coordinates forming the ship

def GAME(grid):#returns whether the person won or loss
    won = False
    number_guesses = 0
    pirate_ship = get_Pirateship(grid)
    check_lst = []
    input_sofar = []

    while number_guesses < 3: #player makes up to three guesses
        displayGrid(grid)
        InputCoord = getInput() #coordinates input by the player 
        #validating part
        check = False
        while check == False:
            if PresenceCheck(input_sofar,InputCoord) == True and validate(InputCoord)== True:
                input_sofar.append(InputCoord)
                check = True
                break
            if PresenceCheck(input_sofar,InputCoord) == False :
                print("you have entered these coordinates before , please enter again")
                InputCoord  = getInput()
            if validate(InputCoord)== False:
                print("The coordinates entered are out of range, pleaser enter again")
                InputCoord  = getInput()
                
        checkResult(InputCoord,pirate_ship, won)
        won = checkResult(InputCoord,pirate_ship, won)  
        if won == True:
            displayGrid(grid)
            print("YOU WON!")
            break  
        number_guesses += 1

    if won == False:
        displayGrid(grid)
        print("GAME OVER...")



#MAIN PROGRAM
print("\t")
print("""\tNow, u have entered the final stage of the game which is BATTLESHIP.
        4 Os on the board form the pirate's ship.Guess a coordinate, out of 4 coordinates that form the pirate's ship.
        Damage the whole ship by guessing a the location of a single O out of the 4 possible Os and win against the pirates.
        ALL THE BEST\t

        HINT: The 4 Os that form the pirate ship are located such that they form a square. Guess the locations within 2 tries  and try
        forming the possible squares that could be the pirate's ship by the last try """)
print("\t")


grid = initialiseGrid()
print("welcome to battleship!")

GAME(grid)

while True:
    play_again = input("play again? Y/N: ")
    if play_again == "Y":
        grid = initialiseGrid()
        GAME(grid)
    elif play_again == "N":
        break
    else:
        continue
        

