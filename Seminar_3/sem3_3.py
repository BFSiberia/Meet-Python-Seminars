#  Реализуйте алгоритм задания случайных чисел без использования 
#  встроенного генератора псевдослучайных чисел.

from cmath import sqrt
import datetime

now = datetime.datetime.now()

n = now.pop((str(sqrt(now.second)),[0,1]))



print(n)

list1 = [1,2,3]
list2 = [4,5,6]

list3= set(list1)
print(list3)