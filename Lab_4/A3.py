packets = input("Введите последовательность пакетов (0 и 1): ")

if len(packets) < 5:
        print("Ошибка: Длина строки должна быть не меньше 5 символов!")

if not all(char in '01' for char in packets):
        print("Ошибка: Используйте только символы '0' и '1'!")