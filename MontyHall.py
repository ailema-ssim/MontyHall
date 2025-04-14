# This program plays a simulation of the Monty Hall Problem.
# Over many runs, the probability of winning will get closer to 2/3 chance winning with a switch of doors 
# and a 1/3 chance of winning without a switch of doors.
# A Prize Door is chosen and the user must find it.
# The user selects a door, then a different door is shown not to have the Prize.
# The user has the chance to stay with their original choice or swap to the last unopened door.
# The purpose oif this simulation is to prove or disprove the MOnty Hall Problem.

from random import randint

# Initializing the global variables to zero
winsNoSwitch = 0
lossesNoSwitch = 0
winsSwitch = 0
lossesSwitch = 0
gamesWon = 0
    
# Calculating statistics from variables
def statistics():
    # Intoducing global variables
    global winsNoSwitch
    global lossesNoSwitch
    global winsSwitch
    global lossesSwitch
    global gamesWon
    print("The total number of Wins No Switch is :", winsNoSwitch)
    print("The total number of Wins Switch is :", winsSwitch)
    print("Total wins all together:", gamesWon )
    # Prints probability of winning without switching Doors
    if winsNoSwitch > 0:
        print("The percentage to win without a switch is : ", 100 * (winsNoSwitch / gamesWon), "%")
    # Prints Porbability of winning with switching Doors
    if winsSwitch > 0:
        print("The percentage to win with a switch is : ", 100 * (winsSwitch / gamesWon), "%")

# Tracking wins/losses and switch/no switch and adding to variables when called for
def getResult(doorSelect):
    # Intoducing global variables
    global winsNoSwitch
    global lossesNoSwitch
    global winsSwitch
    global lossesSwitch
    global gamesWon
    # If prize is found, print winning and add one to gamesWon
    if doorSelect.prizeDoor == doorSelect.usersChoice:
        print("You found the prize!")
        gamesWon += 1
        # If switched doors, add one to winsSwitch
        if doorSelect.stayOrSwitch == "yes":
            winsSwitch += 1
        # If did not switch doors, add one to winsNoSwitch
        elif doorSelect.stayOrSwitch == "no":
            winsNoSwitch +=1
    # Else if prize not found, print losing
    elif doorSelect.prizeDoor != doorSelect.usersChoice:
            print("You did not find the prize.")
            # If switched doors, add one to lossesSwitch
            if doorSelect.stayOrSwitch == "yes":
                lossesSwitch += 1
            # If did not switch doors, add one to lossesNoSwitch
            elif doorSelect.stayOrSwitch == "no":
                lossesNoSwitch +=1

# Class that holds all Door choices made throughout a run
class DoorSelect:
    # Door that will have the Prize is chosen
    def pickPrizeDoor(self):
        self.prizeDoor = randint(1,3)
    # Door that is NOT the door with the prize or the door the user chose is picked and shown to the user
    def showLosingDoor(self):
        self.losingDoor = randint(1,3)
        while self.losingDoor == self.prizeDoor or self.losingDoor == self.usersChoice:  
            self.losingDoor = randint(1,3)
        print("This is a losing door. ->", self.losingDoor)
    # Asks user for their choice of Door, and saves that choice
    def getUsersChoice(self):
        self.usersChoice = int(input("User, choose Door 1, 2 or 3\n"))
        # If user types in number that is not 1,2, or 3 or not an integer, ask again
        if (self.usersChoice < 1  or self.usersChoice > 3):
            print("The choice must be between 1 and 3")
            self.usersChoice = int(input("User, choose Door 1, 2 or 3\n")) 
    # Asks user if they want to stay with their original door or swap to the third unopened Door
    # Changes choice if needed
    def getStayOrSwitch(self):
        self.stayOrSwitch = input("Do you want to switch doors, yes or no?\n")
        if self.stayOrSwitch == "yes":
            originalUsersChoice = self.usersChoice
            self.usersChoice = randint(1,3)
            while self.usersChoice == originalUsersChoice or self.losingDoor == self.usersChoice:
                self.usersChoice = randint(1,3)
        elif self.stayOrSwitch == "no":
            return 
        else:
            print("Answer must be yes or no.")
            self.stayOrSwitch = input("Do you want to switch doors, yes or no?\n")

    

def main():

    while True:
        doorSelect = DoorSelect()
        # Prize Door chosen
        doorSelect.pickPrizeDoor()
        # User's choice selected
        doorSelect.getUsersChoice()
        # A losing door shown to user
        doorSelect.showLosingDoor()
        # User chooses to keep their door or switch
        doorSelect.getStayOrSwitch()
        # Prints users choice door, in case of switch
        print(doorSelect.usersChoice)
        # Shows winning or losing
        getResult(doorSelect)
        # Shows probabilities so far
        statistics()
        # Asks the user if they would like to play again
        playAgain = input("Do you want to play again?\n")
        if playAgain == "yes":
            continue
        if playAgain =="no":
            break
        else:
            print("Answer must be yes or no.")
            playAgain = input("Do you want to play again?\n")


if __name__ == "__main__": 
    main() 
    