#Найдите сумму четных чисел массива
#6
def sum_array_f(arr):
        sum = 0
        for i in range(len(arr)):
            if arr[i] % 2:
                sum += arr[i]
                print(arr[i])

        return sum

     
arr = [34,25,18,15,11,9,8,5]
res = sum_array_f(arr)
print(res, 'SUM')