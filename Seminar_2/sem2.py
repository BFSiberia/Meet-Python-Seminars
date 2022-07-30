# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

s = 'Привет, Мир и всети его окресности!'
first = 'ти'

# def strCount(set1, set2):
#    print(set1.count(set2))

count =0
for i in range(len(s)-len(first)):
    if s[i : i + len(first)] == first: # Если в set1 отрезок от i 
        # до i+длина set2(не включительно)равен set2
        count+=1

print(count)