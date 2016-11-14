#Дана строка. Показать третий, шестой, девятый и так далее символы.
#6
def get_string_1_3_6(string,step):
    start = step;
    while start < len(string):
        print (string[start], start)
        start+=step

get_string_1_3_6('denisprinesivadipazhaluysta1',3)