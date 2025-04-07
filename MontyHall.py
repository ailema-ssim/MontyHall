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

def main(): 
    prizeDoor = PrizeDoor()
    prizeDoor.assignPrizeDoor()
    print(prizeDoor)
    
if __name__ == "__main__": 
    main() 