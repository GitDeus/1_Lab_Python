#В данной строке найти количество цифр.
#14
def get_count_dig_in_string(string):
    counter = 0;
    for index in string:
        if index in ('0','1','2','3','4','5','6','7','8','9'):
                counter+=1
        
    print(counter)

get_count_dig_in_string('deni1sprines2ivadipazha3luysta')