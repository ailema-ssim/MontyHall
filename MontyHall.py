from random import randint



winsNoSwitch = 0
lossesNoSwitch = 0
winsSwitch = 0
lossesSwitch = 0
gamesWon = 0
    
def statistics():
    global winsNoSwitch
    global lossesNoSwitch
    global winsSwitch
    global lossesSwitch
    global gamesWon
    print("The total number of Wins No Switch is :", winsNoSwitch)
    print("The total number of Wins Switch is :", winsSwitch)
    print("Total wins all together:", gamesWon )
    if winsNoSwitch > 0:
        print("The percentage to win without a switch is : ", 100 * (winsNoSwitch / gamesWon), "%")
    if winsSwitch > 0:
        print("The percentage to win with a switch is : ", 100 * (winsSwitch / gamesWon), "%")

def getResult(doorSelect):
    global winsNoSwitch
    global lossesNoSwitch
    global winsSwitch
    global lossesSwitch
    global gamesWon
    if doorSelect.prizeDoor == doorSelect.usersChoice:
        print("You found the prize!")
        gamesWon += 1
        if doorSelect.stayOrSwitch == "yes":
            winsSwitch += 1
        elif doorSelect.stayOrSwitch == "no":
            winsNoSwitch +=1
    elif doorSelect.prizeDoor != doorSelect.usersChoice:
            print("You did not find the prize.")
            if doorSelect.stayOrSwitch == "yes":
                lossesSwitch += 1
            elif doorSelect.stayOrSwitch == "no":
                lossesNoSwitch +=1

class DoorSelect:
    
    def pickPrizeDoor(self):
        self.prizeDoor = randint(1,3)
    def showLosingDoor(self):
        self.losingDoor = randint(1,3)
        while self.losingDoor == self.prizeDoor or self.losingDoor == self.usersChoice:  
            self.losingDoor = randint(1,3)
        print("This is a losing door. ->", self.losingDoor)
    def getUsersChoice(self):
        self.usersChoice = int(input("User, choose Door 1, 2 or 3\n"))
        if (self.usersChoice < 1  or self.usersChoice > 3):
            print("The choice must be between 1 and 3")
            self.usersChoice = int(input("User, choose Door 1, 2 or 3\n")) 
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
        doorSelect.pickPrizeDoor()
        doorSelect.getUsersChoice()
        doorSelect.showLosingDoor()
        doorSelect.getStayOrSwitch()
        print(doorSelect.usersChoice)
        getResult(doorSelect)
        statistics()
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
    