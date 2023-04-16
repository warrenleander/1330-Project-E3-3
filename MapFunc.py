#Richie
#This file is for making levels
#All walls in the maze will be '-' in the array even though some walls may look different in the interface.
from termcolor import colored
import os
def makeEmptyMap(length, breadth):
    wallsHor = '-'
    wallsVert = '|'
    space = '.'
    corner = 'O'
    Map = [[space for i in range(length)] for j in range(breadth)] 
    for row in range(length):
        for column in range(breadth):
            if row == 0 or row == breadth - 1:
                if column == 0 or column == length - 1:
                    Map[row][column] = corner
                else:
                    Map[row][column] = wallsHor
            else:
                if column == 0 or column == length - 1:
                    Map[row][column] = wallsVert
    return Map

def printMap(Map,enemies,colororder):
    for row in range(len(Map)):
        count = 0
        for column in range(len(Map[0])):
            count += 1
            if 'O' in Map[row] and count != len(Map[0]) : 
                if Map[row][column] == 'A':
                    print(colored('-','grey'), end = colored('----','grey'))
                else:
                    print(colored(Map[row][column],'grey'), end = colored('----','grey'))
            else:
                if Map[row][column] == 'Q':
                    for i in range(len(enemies)):
                        if [row,column] == enemies[i]:
                            print(colored(Map[row][column], colororder[i]),end = '    ')
                elif Map[row][column] == '.':
                    print(colored(Map[row][column],'red'), end = '    ')
                elif Map[row][column] == 'P':
                    print(colored(Map[row][column],'cyan', attrs=['bold']), end = '    ')
                elif Map[row][column] == 'X':
                    print(colored(Map[row][column],'red', attrs = ['bold']), end = '    ')
                else:
                    print(colored(Map[row][column],'grey'), end = '    ')
                
        print()

def mapArrayMaker(Map): #This is for me to make walls in the maze, used in Level Maker.py
    def labelMap():
        print('    ', end='')
        for i in range(1,len(Map[0])-1): 
            print(str(i).rjust(2), end = '   ')
        print('Column')
        countA = 0
        for row in Map:
            count = 0
            for i in row:
                count += 1
                if 'O' in row and count != len(Map[0]) : 
                    print(i, end = '----')
                else:
                    print(i, end = '    ')
            if countA == 0:
                print('Row', end= '')
            else:   
                if countA == len(Map) - 1:
                    break
                else:
                    print(countA,end= '')
            countA += 1
            print()
    def makeWalls(row,column):
        Map[row][column] = 'A'
    list1 = []
    while True:
        labelMap()
        print()
        a = input('Row Column (e to end, u to undo): ')
        if a == 'e':
            for i in range(len(Map)):
                for j in range(len(Map[i])):
                    if Map[i][j] == 'A':
                        Map[i][j] = '-'
            break
        elif a == 'u':
            if len(list1) != 0:
                Map[list1[-1][0]][list1[-1][1]] = '.'
                list1.pop(-1)
            continue
        elif a == '':
            continue
        
        row, column = tuple(map(int,a.split(' ')))
        list1.append((row,column))
        makeWalls(row,column)
        os.system('cls')
    



        
        

#########################################################        
sampleMap =[['O','-','-','-','-','-','-','-','-','-','O'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['|','.','.','.','.','.','.','.','.','.','|'],
            ['O','-','-','-','-','~','~','~','~','~','O']]
            
#########################################################
#a = makeEmptyMap(length,breadth) - declare length and breadth when making maps
#mapArrayMaker(a) - makes the array for editing maps
#printMap(a) - prints the map nicely
