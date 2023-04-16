#Richie
#This program is only for me to make the mazes for each levels and get the arrays. DON'T USE THIS PROGRAM IN THE MAIN CODE
from MapFunc import *
#length, breadth = 13, 13
#lvl1 = makeEmptyMap(13,13)
#mapArrayMaker(lvl1)
#print(lvl1)

##############
def declareEmptySpaces(Map):
    empty = []
    for row in range(len(Map)):
        for column in range(len(Map[0])):
            if Map[row][column] == '.':
                empty.append([row,column])
    return empty



def bulletcount(bullet):
    if bullet > 1:
        print(colored(f'Bullets left: {bullet}', 'green'))
    elif bullet > 0:
        print(colored(f'Bullets left: {bullet}', 'yellow'))
    elif bullet == 0:
        print(colored(f'Bullets left: {bullet}', 'red'))

def numsteps(steps):
    if steps > 3:
        print(colored(f'Steps remaining: {steps}', 'green'))
    elif steps > 0:
        print(colored(f'Steps remaining: {steps}', 'yellow'))
    elif steps == 0:
        print(colored(f'Steps remaining: {steps}', 'red'))

"""bulletcount()
numsteps()"""
