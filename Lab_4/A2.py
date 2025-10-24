n = int(input('Введите число строк: '))
m = int(input('Введите число столбцов: '))

print(f"ПРЯМОУГОЛЬНИК {n}x{m}:")
for i in range(n):
    for j in range(m):
        print('#', end='')
    print()