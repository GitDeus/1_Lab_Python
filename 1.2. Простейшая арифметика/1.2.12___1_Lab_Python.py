#Пользователь вводит сторону квадрата. Найдите периметр и площадь квадрата.
#12
def square_area(side):
     return side*side
   
def p_area(side):
     return side*4

imput_number4 = int(input('Enter S: '))
imput_number5 = int(input('Enter P: '))
print('S = ',square_area(imput_number4))
print('P = ',p_area(imput_number5))