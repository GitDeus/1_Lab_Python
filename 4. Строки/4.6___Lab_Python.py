#Дана строка. Показать третий, шестой, девятый и так далее символы.
#6
def get_string_1_3_6(string):
    i = 3
    while i < len(string)-1:
        print (string[i], i)
        i+=3

get_string_1_3_6('denisprinesivadipazhaluysta')