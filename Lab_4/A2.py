n = int(input('Введите число строк: '))
m = int(input('Введите число столбцов: '))

print(f"ПРЯМОУГОЛЬНИК {n}x{m}:")
for i in range(n):
    for j in range(m):
        print('#', end='')
    print()

print(f"ПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(n):
    for j in range(i+1):
        print('#', end='')
    print()

print(f"РАМКА {n}*{m}:")
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("#", end='')
        else:
            print(" ", end='')
    print()
