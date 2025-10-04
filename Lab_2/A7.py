x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

color1 = 'white' if (x1+y1)%2==0 else 'black'
color2 = 'white' if (x2+y2)%2==0 else 'black'

if color1==color2: print('Yes', color1)
else: print('No')
