#Вывести квадрат 7 на 7 из случайных букв.
#3
import random
def new_str(d):
    a = 1
    str = ''
    while a < d:
        a+=1
        str += abc[random.randint(1,26)]
    return str


def paint(r,c):
    for i in range(1, r):
        print(new_str(c))
    
paint(7,7)