#Дана строка. Вывести первый, последний и средний (если он есть)) символы.
#2
def get_string(string):
    print('first', string[0])
    
    if len(string) % 2:
       print('mid',string[len(string)//2])

    print('last',string[len(string)-1])

get_string('denis')