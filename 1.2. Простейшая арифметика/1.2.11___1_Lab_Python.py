#Пользователь вводит три числа. Найдите среднее арифметическое этих чисел, а также разность удвоенной суммы первого и третьего чисел и утроенного второго числа.
#11
def fl(lst):
     s, llen = 0, 0
     for i in lst:
         s += int(i)
         llen += 1
     return s / llen
     
def fl2(lst):
    f, s, p = 0, 0, 0
    for i in lst:
        p+=1
        if p % 2:
            s -= int(i)*2
        else :
            f += int(i)*3
    return f - s

x = []
num = input('Enter number(s1): ')
x = num.split(',')
print(fl(x))
print(fl2(x))