import random
import time

n = int(input("Введите количество примеров: "))
number = 1
all_time = 0
counter = 0

for i in range(n):
    print(f"Вопрос ({number}/{n})")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_result = a * b

    while True:
        try:
            start_time = time.time()
            answer = int(input(f"{a} × {b} = "))
            time_spend = time.time() - start_time

            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    if answer == correct_result:
        print(f"Верно! Время: {time_spend:.1f} сек")
        counter += 1
        number += 1
        all_time += time_spend
    else:
        number += 1
        print(f"Неверно! Правильный ответ: {correct_result} Время: {time_spend:.1f} сек")
        all_time += time_spend

percentage = counter / n * 100
average = all_time / n

print("="*50)
print("СТАТИСТИКА \n")
print("="*50)
print(f"Общее время: {all_time:.1f} секунд \n",
      f"Среднее время на вопрос: {average:.1f} сек \n",
      f"Правильных ответов: {counter}/{n} \n",
      f"Процент правильных: {percentage:.1f}%")
