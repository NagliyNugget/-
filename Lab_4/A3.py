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

loss_percent = (lost_packets / total_packets) * 100

if loss_percent <= 1:
    quality = "Отличное качество"
elif loss_percent <= 5:
    quality = "Хорошее качество"
elif loss_percent <= 10:
    quality = "Удовлетворительное качество"
elif loss_percent <= 20:
    quality = "Плохое качество"
elif loss_percent > 20:
    quality = "Критическое состояние сети"

print(f"Общее число пакетов: {total_packets}")
print(f"Число потерянных пакетов: {lost_packets}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_streak}")
print(f"Процент потерь: {loss_percent:.1f}%")
print(f"Качество связи: {quality}")
