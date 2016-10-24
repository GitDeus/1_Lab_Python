#Заполните массив случайным образом нулями и единицами так, чтобы количество единиц было больше количества нулей.
#14
import random
func = lambda x: x**x
def arr_rnd():

    arr = []
    for i in range(0,100):
        arr.append(random.randint(0,1))
        func(arr[i])
        
    return (arr)


print(arr_rnd())