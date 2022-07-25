# Напишите программу, удаляющую из текста все слова, содержащие "абв".

s= 'Оабо нрапабв, рлорлвл абв-лллл. дл аб абв:оо аор! 13абв аабв14'

import re
s0=''.join(map(lambda i: i if i.isalnum() else  ' '+i+' ', s))
s1=re.findall(r'(\d+|\D+)',s0) # Не знаю, как получить корректную разбивку

s2=[]
for i in s1:
    if i.isdigit():
        s2.append(i)
    else:
        temp=i.split()
        for j in temp:
            s2.append(j)

s3=' '.join(list((filter(lambda i: not 'абв' in i, s2))))
print(s3)      

# Попытка №1 обойтись без re.findall. Не смог "склеить" цифры

# s1=''.join(map(lambda i: i if i.isalpha() else  ' '+i+' ', s))
# print(s1)
# s2=list((filter(lambda i: not 'абв' in i, s1.split())))
# print(s2) 

# Попытка №2 обойтись без цикла for. Ошибка при сплите вложенной строки

# print(list(map(lambda j: j,s1[0].split()))) # вложенная строка
# s3=' '.join(map(lambda i:i if i.isdigit() \
# else (map(lambda j: j,s1[i].split()))),s1)