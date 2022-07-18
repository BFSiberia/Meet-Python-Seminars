# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def FindMaxMinDif (list):
    l_dec = []
    for i in list:
        if i%1==0:
            continue
        else:
            l_dec.append(float(str(i)[str(i).find('.'):]))
    result = max(l_dec)-min(l_dec)
    return result

list = [-1.1, 1.2, -3.1, 5, 10.01]

print(f'Разница между макимальным и минимальное значением дробной части: {FindMaxMinDif (list)}')