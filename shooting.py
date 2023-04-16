#Richie
import time
def shoot(playerPos, direction, Map, bulletcount): #PlayerPos is tuple, enemycolor = {'yellow' : (1,2)}
    direction = direction.upper() #direction2
    bullet = playerPos
    row, column = bullet[0], bullet[1]
    while True:
        if direction == 'W': 
            if Map[row][column] == 'Q':
                Map[row][column] = '.'
                return [row,column],None,bulletcount
            elif Map[row][column] == '-':
                Map[row][column] = '.'
                return None,[row,column],bulletcount-2
            elif Map[row][column] == 'A': 
                return None,None,bulletcount-1
            row -= 1    
        elif direction == 'A':
            if Map[row][column] == 'Q':
                Map[row][column] = '.'
                return [row,column],None,bulletcount
            elif Map[row][column] == '-':
                Map[row][column] = '.'
                return None,[row,column],bulletcount-2
            elif Map[row][column] == '|': 
                return None,None,bulletcount-1
            column -= 1
        elif direction == 'S':
            if Map[row][column] == 'Q':
                Map[row][column] = '.'
                return [row,column],None,bulletcount
            elif Map[row][column] == '-':
                Map[row][column] = '.'
                return None,[row,column],bulletcount-2
            elif Map[row][column] == 'A': 
                return None,None,bulletcount-1
            row += 1
        elif direction == 'D':
            if Map[row][column] == 'Q':
                Map[row][column] = '.'
                return [row,column],None,bulletcount
            elif Map[row][column] == '-':
                Map[row][column] = '.'
                return None,[row,column],bulletcount-2
            elif Map[row][column] == '|': 
                return None,None,bulletcount-1
            column += 1
