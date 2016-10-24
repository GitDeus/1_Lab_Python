#Найдите сумму чисел массива, которые стоят на четных местах.
#9
def sum_array(arr):
        sum = 0
        for i in range(len(arr)):
            if i % 2:
                sum += arr[i]
                print(arr[i])
        return sum 

arr = [34,25,18,15,11,9,8,5]
res = sum_array(arr)
print(res, 'SUM')