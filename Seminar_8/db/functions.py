def search():
    answer=input('Что хоите вывести на экран: 1- весь класс; 2- одного ученика: ')
    if answer=='1':
        with open ('student.txt', 'r', encoding='utf-8') as f:
            result=f.read()
    else:
        person=input('Введите ФИО ученика: ')
        with open ('student.txt', 'r', encoding='utf-8') as f:
            tmp=f.readlines()
            for i in tmp:
                if person in i:
                    result =i
                    return result

    return result