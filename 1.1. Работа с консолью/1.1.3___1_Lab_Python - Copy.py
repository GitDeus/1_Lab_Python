
#Вывести на экран пять строк из нулей, причем количество нулей в каждой строке равно номеру строки.
#3


def print_str_num() :
    imput_number = int(input('Write number: '))

    n = 0 ;
    while n < imput_number :
            n += 1
            print(n, "0"*n)
print_str_num()