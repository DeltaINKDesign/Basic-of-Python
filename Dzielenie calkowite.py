n=int(input('Podaj liczbe'))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10     #to jest dzielenie calkowite
print('s=',s)
