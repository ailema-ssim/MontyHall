from random import randint

class PrizeDoor:
    def __init__(self):
        self.value = 1
    def assignPrizeDoor(self):
        self.value = randint(1,3)
    def getValue(self):
        return self.value
    def __str__(self):
        return str(self.getValue())


def turn(door):
    validMove = False
    while validMove == False:                      #(row < 1 or row > 3):
        door = int(input("User, choose Door 1, 2 or 3"))            #should i add player to this
        if (door < 1  or door > 3):
            print("The choice must be between 1 and 3")
    
class NotPrizeDoor:
    def __init__(self):
        self.value = 1
    def assignNotPrizeDoor(self):
        self.value = randint(1,3)
    def getValue(self):
        return self.value
    def __str__(self):
        return str(self.getValue())
    
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


def main():
    prizeDoor = PrizeDoor()
    prizeDoor.assignPrizeDoor()
    
    notPrizeDoor = NotPrizeDoor()
    notPrizeDoor.assignNotPrizeDoor()

   # while prizeDoor = notPrizeDoor
    #
    print(prizeDoor)
    print(notPrizeDoor)

if __name__ == "__main__": 
    main() 