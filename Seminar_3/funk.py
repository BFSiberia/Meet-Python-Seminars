def Presence (list, n):
    for item in list:
        if n in item:
            print(item)

def Find_Second (list, item):
    count = 0
    for i,value in enumerate(list): # enumerate - возвращает индекс и значение списка
        if value == item:
            count+=1
        if count==2:
            print('ответ:',i)
            break

    if count<2:
            print('ответ:',-1)