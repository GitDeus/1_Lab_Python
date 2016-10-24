#Дана строка. Определить, содержит ли строка только символы 'a', 'b', 'c' или нет.
#15
def string_a_b_c(string):
    for index in string:
        if index not in ('a','b','c'):
            return False
    return True