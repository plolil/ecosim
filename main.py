from random import randint
from sys import exit

#random names for the people
def randname():
    with open("names", "rt") as namefile:
        x = namefile.read().splitlines()
        name = x[randint(0, len(x) - 1)]
    return name


#a person!
class person:
    def __init__(self, balance=10, name=randname(), x = randint(0, 7), y = randint(0, 7)):
        self.pos = {"x": x, "y": y}
        self.bal = balance
        self.name = name
        self.mode = "idle"

    def step(self):
        #temporary code
        self.pos = {"x": randint(0, 7), "y": randint(0, 7)}
        

def GetNextAction(entity): #entity is any person
    pass                   #entity will be an array including an ID and other factors such as held money, coords, etc.

def GetNextTrades(market): #Will retrieve all trades that will be performed at a given market
    pass

def GetMarketPriceChange(market, itemID): #Will calculate the change in price of an item based on supply/demand at a given market
    pass

#hardcoded map
grid = [['-','-','-','-','-','-','-','-'],
       ['-','-','-','-','-','-','-','-'],
       ['-','-','-','-','-','-','-','-'],
       ['-','-','-','-','-','-','-','-'],
       ['-','-','-','-','-','-','-','-'],
       ['-','-','-','-','-','-','-','-'],
       ['-','-','-','-','-','-','-','-'],
       ['-','-','-','-','-','-','-','-']]

#module checking
if __name__ == "__main__":
    people = []
    #awful bad code here for testing
    people.append(person(x = randint(0, 7), y = randint(0, 7)))
    people.append(person(x = randint(0, 7), y = randint(0, 7)))
    people.append(person(x = randint(0, 7), y = randint(0, 7)))
    people.append(person(x = randint(0, 7), y = randint(0, 7)))
    people.append(person(x = randint(0, 7), y = randint(0, 7)))

    #main loop
    command = ""
    while True:
        #python reference bullshit
        tempgrid = [None] * 8
        for num, arr in enumerate(grid):
            tempgrid[num] = arr[:]

        #add each of the people to the array
        for i in people:
            tempgrid[i.pos['x']][i.pos['y']] = "i"

        #draw the array
        head = "  "
        for num in range(0, len(tempgrid)):
            head += str(num) + ' '
        print(head)
        for num, i in enumerate(tempgrid):
            tmpstr = str(num) + " "
            for n in i:
                tmpstr += n + " "
            print(tmpstr)
        
        #simple cli-like-interface
        io = input("what next?: ")
        command = (command if io == "" else io)
        if command == "step":
            for i in people:
                i.step()
        elif command == "exit":
            exit(0)
