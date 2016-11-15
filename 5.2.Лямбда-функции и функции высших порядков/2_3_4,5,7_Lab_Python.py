#print(set(map(lambda x: x*2.54, [1,2,3,4,5,6,7,8,9])))

#5
def duim_cm(set):
    print(list(map(lambda x: x, set)))
    print(list(map(lambda x: x*2.54, set)))
    for r in (list(map(lambda x: x, set))):
        print("Value of Duim {0:2,d}".format(r), "value is CM {0:2,f}".format(r*2.54))

print("\n[5]")    
duim_cm([1,2,3,4,5,6,7,8,9])

#4
def sq(set):
    print("\n[4]")
    print(list(map(lambda x: x**2, set)))

    
sq([1,2,3,4,5,6,7,8,9])

#7
def sq(set):
    print("\n[7]")
    print(list(map(lambda x: len(x),set)))
    
sq(["One","Two","Three","Four","Five","Six","Seven","Floccinaucinihilipilification","Pneumonoultramicroscopicsilicovolcanoconiosis"])
#Pneumonoultramicroscopicsilicovolcanoconiosis (forty-five letters)
#Floccinaucinihilipilification (twenty-nine letters) 