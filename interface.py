#Warren
import MapFunc
from termcolor import colored, cprint
def welcome():
    print("""
    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ██╔════╝░██╔══██╗████╗░████║██╔════╝
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██║░░██╗░███████║██╔████╔██║█████╗░░
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")

def bulletcount(bullet):
    if bullet > 1:
        print(colored(f'Bullets left: {bullet}', 'green'),end='')
    elif bullet > 0:
        print(colored(f'Bullets left: {bullet}', 'yellow'),end='')
    elif bullet == 0:
        print(colored(f'Bullets left: {bullet}', 'red'),end='')

def remainingTime(timeLeft):
    if timeLeft > 100:
        print(colored(f'Time remaining: {timeLeft}s', 'green'),end='')
    elif timeLeft > 50:
        print(colored(f'Time remaining: {timeLeft}s', 'yellow'),end='')
    elif timeLeft > 0:
        print(colored(f'Time remaining: {timeLeft}s', 'red'),end='')

def orderColor(colororder):
    print(colored('Order: ','green'),end = '')
    for i in colororder:
        print(colored('Q',i),end = '  ')

def stats(bullet,timeLeft,colororder):
    bulletcount(bullet)
    print('       ',end='')
    remainingTime(timeLeft)
    print('      ',end='')
    orderColor(colororder)
    print('')
