#Вывести англ. алфавит по 5 букв в строке.
#2
abc = "abcdefghijklmnopqrstuvwxyz"

def alphabet_en(n):
    i=0
    str = ''
    tmp = ''
    while i < 26:
          str += abc[i]
          i+=1
          if i % n == 0:
             tmp = str
             print(tmp)
             str = ''

alphabet_en(5)