# Реализуйте RLE алгоритм: модуль сжатия и восстановления длины
# Идея в том, чтобы выполнить линейное санирование строки 
# и для каждого отдельного символа и его последовательное вхождение в выходную строку

s='AABBBBCDDDEEEEE'

def Shrink(s):
    counter=0
    simb=s[0]
    code=''
    for i in s:
        if i==simb:
            counter+=1
        else:
            code+=''.join(str(counter)+simb)
            counter=1
            simb=i
    code+=''.join(str(counter)+simb)
    return code

k=Shrink(s)

def Inflate(k):
    source=''
    mult=int(k[0])
    
    for i in k:
        if i.isalpha():
            source+=''.join(i*mult)
        else:
            mult=int(i)
    return source

print(k)
print(Inflate(k))



# Неудачные попытки реализовать кидировку повторяющихся групп символов

# result=''
# start=0
# i=1

# while i in range(1,len(s)//2+1-start):
#     print(f'Длина слова: {i}, Максимльная длина слова: {len(s)//2+1-start}')
#     counter=0
#     tryword=s[start:start+i]
#     print('Проверочное слово: '+tryword)
#     for x in range(start,len(s)-1,i):
#         print(f'Диапазон от {start} до {str(len(s)-1)} шаг {i}')
#         print(f'Сравниваем {tryword} с {s[x:x+len(tryword)]}')
#         if s[x:x+len(tryword)]!=tryword and counter<2:
#             i+=1
#             break
#         elif s[x:x+len(tryword)]!=tryword and counter>1:
#             result+=str(counter)+tryword
#             start+=counter*(i)
#             i=1
#             break
#         else:
#             counter+=1
# else:        
#     print(f'Длина слова: {len(tryword)} Макс длина слова: {len(s)//2-start}')
#     if len(tryword)==len(s)//2-start and counter<2:
#         result+=str(counter)+s[start]
#         i=1
#         start+=counter*(i)
#         # else:    
#         #     result+=str(counter)+tryword
#         #     i=len(s)//2-1
# print('Код: '+result)



# while i in range(len(s)-i):
#     first=s[start:start+1+i]
#     for x in range(start, len(s)-i):
#         if s[x : x + len(first)] != first and counter<2:
#             i+=1
#             break
#         elif s[x : x + len(first)] != first and counter>1:
#             result+=str(counter)+first
#             start+=counter*(i+1)
#             i=0
#             first=s[start:start+1+i]
#             counter=0
#             break
#         else:
#             counter+=1
#     if x==len(s)-1-i:
#         i=len(s)
#         break
# result+=str(counter)+first
# print(result)


# s='AAAFABCABCACBABWWAATTTTTTNN'

# res=''

# # for i in range(len(s)-1):
# #     if s[i]
# start=0
# i=0
# while i in range(int(len(s)//2-1)):
#     count =1
#     # expression=[s[x:x+(i+1)] for x in range(st,len(s) - i)] # 4(+4-3), 3(+3-2), 2(+2-1), 1(+1-0)
#     expression=[]
#     for x in range(start,len(s)- i,i+1):
#         expression.append(s[x:x+(i+1)])    
    
#     if len(expression)>1 and expression[0]!=expression[1]:
#         i+=1
#     else:
#         count=1
#         for j in range(1,len(expression)-1):
#             if expression[j]== expression[0]:
#                 count+=1
#             else:
#                 break
#         res+=''.join(str(count)+expression[0])
#         i=0
#         print(res)
#         start=count*len(expression[0])        

# print(res)