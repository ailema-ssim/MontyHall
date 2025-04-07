#This game shows how the Monty Hall problem works.
#User will choose 1 of 3 doors, looking for the prize.
#A second door will open, showing that it doesn't have the prize.
#User has the choice of sticking to their original door, or choosing the third.
#Results will be accumulated to show the probability of winning between the two options.
#The more times played, the more accurate the results.



doors = ["-","-","-"]

#printing the doors
def printDoors (doors):
    print("\n")
    print("\t {} | {} | {}".format(doors[1],[2],[3]))
    print("\n")


def checkWinner(doors):
    #Checking for winner
    for row in range (1,3):
        
        print("You are a winner")
    else print("You did not find the prize")


#imports module randint
from random import randint

#the class prizeDoor to select a random door
class prizeDoor:
    

    def __init__(self):
        self.value = 1   
    
    def roll(self):
        self.value = randint(1,3)

    def getValue(self):
        return self.value
    


#This function is created to play a single game and print the results after each game.
def playGame():
    #Initializing variables
    winsNoSwitch = 0
    lossesNoSwitch = 0
    winsSwitch = 0
    lossesSwitch = 0
    gamesWon = 0
    
    #Calculating averages
    print("The total number of Wins No Switch is :", winsNoSwitch)
    print("The total number of Wins Switch is :", winsSwitch)
    if winsNoSwitch > 0:
        print("The percentage to win without a switch is : ", 100 * (winsNoSwitch / gamesWon), "%")
    if winsSwitch > 0:
        print("The percentage to win with a switch is : ", 100 * (winsSwitch / gamesWon), "%")


#Main function of the simulation
def main():
    playGame()


