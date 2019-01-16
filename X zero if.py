a=int (input('Podaj a='))
b=int (input('Podaj b='))
#print(a+'x+ ' + b + '=0')
a=float(a)
b=float(b)
if a!=0:
    x=-b/a
    print(x)
elif a==0 and b==0 :
    print('nieskonczenie wiele x')
elif a==0 and b!=0:
    print('brak x')