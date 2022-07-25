# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    # *Пример:* 
    # 2+2 => 4; 
    # 1+2*3 => 7; 
    # 1-2*3 => -5;
    # - Добавьте возможность использования скобок, меняющих приоритет операций.    
    # *Пример:*    
    # 1+2*3 => 7;   
    # (1+2)*3 => 9;


from ast import While


def Breckets(x):
    def Calc(x):
        while "*" in x:
            ind = x.index('*')
            x[ind-1]=x[ind-1]*x[ind+1]
            del x[ind:ind+2]
        while "/" in x:
            ind = x.index('/')
            x[ind-1]=x[ind-1]/x[ind+1]
            del x[ind:ind+2]
        while "-" in x:
            ind = x.index('-')
            x[ind-1]=x[ind-1]-x[ind+1]
            del x[ind:ind+2]
        while '+' in x:
            ind = x.index('+')
            x[ind-1]=x[ind-1]+x[ind+1]
            del x[ind:ind+2]
        return x[0]
    
    while ')' in x:
        bClose=x.index(')')
        bOpen = len(x[:bClose])-x[bClose::-1].index('(')
        temp=x[bOpen+1:bClose]
        while temp.count('*')>0 and temp.count('/')>0:
            a=temp.index('/')
            b=temp.index('*')
            if a<b:
                temp[a-1]=Calc(temp[a-1:a+2])
                del temp[a:a+2]
            else:
                temp[b-1]=Calc(temp[b-1:b+2]) 
                del temp[b:b+2]

        x[bOpen]=Calc(temp)
        del x[bOpen+1:bClose+1]  
    return Calc(x)

s1 = '5*(3-6*(2+1)/(15-5))'
y=''.join(map(lambda i: i if i.isdigit() else ' '+i+' ', s1))
x=[int(i) if i.isdigit() else i for i in y.split()]

print(Breckets(x))
print(eval(s1))