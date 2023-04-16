#YANG ZILING's program
from termcolor import colored
import random as ran
def enemy(empty): #[(1,2),(2,3)
    enemies = [0 for i in range(4)] 
    colororder = ['magenta','yellow','green','blue']
    for i in range(4):
        enemies[i] = empty[:][ran.randint(0,len(empty)-1)]#produce enemies in empty space
    return enemies,colororder

def killinorder(killed,enemies,killnumber,colororder):# killnumber means the number player killed
    for i in range(4):
        if killed == enemies[i]:
            enemies[i] = 0
            keep = i
            break
    if colororder[killnumber] == colororder[keep]:#whether kill in the correct order
        return True
    else:
        return False
