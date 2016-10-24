#Определите, является ли данное число простым.
#53
def isProst(n):
     for i in (2,n-1):
         if not n%i:
             return False
     return True

print(isProst(122))