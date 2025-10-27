packets = input("Введите последовательность пакетов (0 и 1): ")

if len(packets) < 5:
        print("Ошибка: Длина строки должна быть не меньше 5 символов!")

if not all(char in '01' for char in packets):
        print("Ошибка: Используйте только символы '0' и '1'!")

total_packets = len(packets)

lost_packets = packets.count('0')

max_streak = 0
streak = 0

for packet in packets:
    if packet == '0':
        streak += 1
        max_streak = max(max_streak, streak)
    else:
        streak = 0

print(f"Общее число пакетов: {total_packets}")
print(f"Число потерянных пакетов: {lost_packets}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_streak}")
