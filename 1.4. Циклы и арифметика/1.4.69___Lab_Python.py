#Вывести 3 случайных числа от 0 до 100 без повторений.
#69
import random
def rnd_gen(count, start, end):
    c = 0;
    lst = []
    while c < count:
        lst.append(random.randint(start , end))
        c+=1
    return lst

x = rnd_gen(3,1,100)