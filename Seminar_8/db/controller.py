import functions as fun
import input_data as ip

def button_click():
    while True:
        button=input('Введите цифру операции: 1- Вввод новых данных;\n \
            2- Поиск ученика или вывод всего списка; 3- Удаление записи в базе: ')
        if button in ['1','2','3']:
            break
    if button=='1':
         return ip.data_in()
    elif button=='2':
        return fun.search()
    else:
        return '!'