#Удалить в массиве все числа, которые повторяются более двух раз.
#7
def del_all_number_if_r_2(array):

    maxval = max(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    for a in count:
        if count[a] > 2:
                count[a] = 0
    newarr = []
    for a in range(m): 
            for c in range(count[a]):
                if c < 2:
                    newarr.append(a)
        
    return (newarr,array,count)

print(dell_al_number_if_r_2( [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1, 5, 6, 8, 3, 5, 6, 7, 9, 3, 9, 12, 1, 7]))