#Пользователь вводит номер месяца, вывести название месяца.
#4
months_of_the_year = {'1' : 'January', '2' :'February', '3': 'March', '4': 'April', '5':'May', '6':'June', '7': 'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}
imput_number6 = input('Enter number of the month: ')
print(imput_number6 + ' month of year -',months_of_the_year.get(imput_number6))