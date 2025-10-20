previous = int(input())
current = int(input())

if current >= previous:
    volume = current - previous
else:
    volume = 10000 - previous + current