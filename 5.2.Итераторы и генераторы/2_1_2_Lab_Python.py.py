def Generator(list) :
    for i in list :
            yield int((i**2)**0.5)

mygenerator = Generator([1,-2,3,4,5,-6,7,8,9,-1,2,3,4,5,-6])

for i in mygenerator:
     print(i)