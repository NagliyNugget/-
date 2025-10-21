import random
import time

n = int(input("Введите количество примеров: "))

for i in range(n):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_result = a * b

    start_time = time.time()
    answer = int(input(f"{a} × {b} = "))
    time_spend = time.time() - start_time