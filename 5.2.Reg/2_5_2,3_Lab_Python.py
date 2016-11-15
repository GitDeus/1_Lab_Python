import re
#3
p = re.compile('\d+')

print(p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))

#2
str = re.compile('-?[0-9]+.?[0-9]*')
for i in str.findall("10 lords a-leaping"):
    print("Real number:",i)
