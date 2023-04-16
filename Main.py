import MapFunc
import shooting
import enemy
import interface
import movement
import shooting
import os
import timer
import LevelMaker
import time
global Map
lvl1=[['O', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'O'], 
      ['|', '.', '.', '.', '.', '.', '-', '.', '.', '.', '.', '.', '|'],
      ['|', '.', '-', '-', '-', '.', '-', '.', '-', '-', '-', '.', '|'],
      ['|', '.', '-', '.', '.', '.', '-', '.', '.', '.', '-', '.', '|'],
      ['|', '.', '-', '-', '-', '-', '-', '-', '-', '.', '-', '.', '|'],
      ['|', '.', '.', '.', '-', '.', '.', '.', '.', '.', '-', '.', '|'],
      ['|', '-', '-', '.', '-', '.', '-', '-', '-', '-', '-', '.', '|'],
      ['|', '.', '.', '.', '.', '.', '-', '.', '.', '.', '.', '.', '|'],
      ['|', '-', '-', '.', '-', '-', '-', '.', '-', '-', '-', '-', '|'],
      ['|', '.', '.', '.', '-', '.', '-', '.', '.', '.', '-', '.', '|'],
      ['|', '.', '-', '-', '-', '.', '-', '.', '-', '.', '-', '.', '|'],
      ['|', '.', '.', '.', '.', '.', '-', '.', '-', '.', '.', '.', '|'],
      ['O', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'O']]
Map = lvl1
empty = LevelMaker.declareEmptySpaces(Map)
enemies, colororder = enemy.enemy(empty)#enemy store the position, colororder store the order need to be killed in
enemycolor = {} #dict to store colors of all enemies
bulletcount = 5
steps = 30
for i in range(len(enemies)):
    Map[enemies[i][0]][enemies[i][1]] = 'Q'
starttime = time.strftime('%H:%M:%S',time.localtime())#get the time game start
empty = LevelMaker.declareEmptySpaces(Map) #updates empty spaces after enemies are put in
bulletPos = movement.pickbullet(empty)
for i in range(len(bulletPos)):
    Map[bulletPos[i][0]][bulletPos[i][1]] = 'X'
spawn = movement.born(empty)
Map[spawn[0]][spawn[1]] = 'P'
killnumber = 0
output = ''
#########################################
interface.welcome()
time.sleep(1)
os.system('cls')
while True:
    timeleft = 200 - timer.reciprocal(starttime)[0]#time limit
    if timeleft <= 0:
        output = (''' - You ran out of Time -
█▄█ █▀█ █░█   █░░ █▀█ █▀ ▀█▀
░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ░█░''')
        break
    MapFunc.printMap(Map,enemies,colororder)
    interface.stats(bulletcount, timeleft, colororder)
    move = input(''' - Choose your Move - 
(M to Move, S to Shoot): ''')
    if move.lower() == 'm':
        direction = input('''- Direction -
(W ,A ,S ,D): ''')
        if direction.lower() not in ['w','a','s','d']:
            continue
        Map[spawn[0]][spawn[1]] = '.'
        spawn, bulletcount = movement.movement(empty,direction,spawn,enemies,bulletPos,bulletcount)
        Map[spawn[0]][spawn[1]] = 'P'
    elif move.lower() == 's':
        direction = input('''- Direction -
(W ,A ,S ,D): ''')
        if direction.lower() not in ['w','a','s','d']:
            continue
        killedEnemy,wallbreak,bulletcount = shooting.shoot(spawn, direction, Map, bulletcount)
        if killedEnemy != None:empty.append(killedEnemy)
        elif wallbreak != None:empty.append(wallbreak)
        if killedEnemy != None:
            check = enemy.killinorder(killedEnemy,enemies,killnumber,colororder)#check whether enemy is correct
            if check == True:
                killnumber += 1
            elif check == False:
                output = ('''- Oops! Shot the wrong enemy -
 █▄█ █▀█ █░█   █░░ █▀█ █▀ ▀█▀
 ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ░█░''')
                break
        else:
            print('do not kill enemy')
        steps -= 1
        if killnumber == 4:
            output = ('''   - CONGRATULATIONS! -            
█▄█ █▀█ █░█   █░█░█ █ █▄░█
░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█''')
            break
        elif bulletcount == 0:
            output = (''' - You ran out of Bullets -
█▄█ █▀█ █░█   █░░ █▀█ █▀ ▀█▀
░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ░█░''')
            break
    os.system('cls')
print(output)
