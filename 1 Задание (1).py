a=int(input('Введите первое число'))
b=input('Введите опцию(+,-,*,/)')
c=int(input('Введите второе числло'))
s=0
if b=='+':
    s=a+c;
if b=='-':
    s=a-c;
if b=='*':
    s=a*c;
if b=='/':
    s=a/c;
print(s)