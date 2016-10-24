#Создать массив, каждый элемент которого равен квадрату своего номера.
#9
def array_rfg(l):
    res = [x*x for x in range(0, l)]
    return res

print(array_rfg(12))