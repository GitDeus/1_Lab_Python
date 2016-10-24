#Найти наиболее часто встречающийся элемент в массиве целых чисел.
#30
def dfdfd(array):

    maxval = max(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    
    kolvo = max(count)
    chislo = 0;
    for a in range(len(count)): 
        if count[a] == kolvo:
             chislo = a+1
        
    
        
    return (array,count,kolvo,chislo)

x = dfdfd([1, 4, 4, 7, 9, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1, 5, 6, 8, 3, 5, 6, 7, 9, 3, 9, 12, 1, 7])
print(x[0])
print(x[2], 'raz, chislo' , x[3])