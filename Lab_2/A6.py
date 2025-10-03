N = int(input('Введите количество секунд'))

hours = int(N/3600)
mins = int(N%3600/60)
secs = int(N%3600%60)

print(f"{hours}:{mins:02d}:{secs:02d}")
