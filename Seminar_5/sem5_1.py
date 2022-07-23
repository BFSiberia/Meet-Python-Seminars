# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

with open('test.txt','r') as f:
    file = f.read().split()
    for i in range(1,len(file)-1):
        if int(file[i])-1 != int(file[i-1]):
            print(i+1)
