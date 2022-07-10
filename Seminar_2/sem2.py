# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

set1 = 'Привет, Мир и все его окресности!'
set2 = 'ти'

# def strCount(set1, set2):
#    print(set1.count(set2))

count =0
for i in range(len(set1)-len(set2)):
    if set1[i : i + len(set2)] == set2:
        count+=1

print(count)