#YANG ZILING's program
import time
import random as ran
def born(empty):#produce player
    initial = empty[:]
    return initial[ran.randint(0,len(empty)-1)]

def pickbullet(empty):
    bullets = []
    for i in range(2):
        bullets.append(empty[:][ran.randint(0,len(empty)-1)])
    return bullets

def pick(a,bullets,bulletcount):
    if a in bullets:
        bullets.pop(bullets.index(a))
        return bulletcount+1
    else:
        return bulletcount

def movement(empty,direction,initial,enemy,bullets,bulletcount):#initial is the current position of player
    keep = initial[:]
    if direction == 'W' or direction == 'w':
        initial = [initial[0]-1,initial[1]]
        newbulletcount = pick(initial,bullets,bulletcount)
        B = True
    elif direction == 'A' or direction == 'a':
        initial = [initial[0],initial[1]-1]
        newbulletcount = pick(initial,bullets,bulletcount)
        B = True
    elif direction == 'S' or direction == 's':
        initial = [initial[0]+1,initial[1]]
        newbulletcount = pick(initial,bullets,bulletcount)
        B = True
    elif direction == 'D' or direction == 'd':
        initial = [initial[0],initial[1]+1]
        newbulletcount = pick(initial,bullets,bulletcount)
        B = True
    if initial not in empty or initial in enemy:
        print(f'The "{direction}" direction is blocked, Please Enter Again.')
        time.sleep(2)
        B = False
    if B:
        keep = initial[:]
    return keep,newbulletcount#movement in four direction
#position of player
