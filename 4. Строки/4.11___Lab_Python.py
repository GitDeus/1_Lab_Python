#Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов, иначе дополнить строку символами 'o' до длины 12.
#11
def sert(string):
    if len(string) > 10:
        return string[:6:]
    else:
        x = string+'o'*(12-len(string))
        return x, len(x)

print(sert('abcdefw'))