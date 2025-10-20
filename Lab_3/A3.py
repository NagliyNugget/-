previous = int(input())
current = int(input())

if current >= previous:
    volume = current - previous
else:
    volume = 10000 - previous + current
    
if volume <= 300:
    payment = 21.0
elif volume <= 600:
    payment = 21 + (volume - 300) * 0.06
elif volume <= 800:
    payment = 21 + 300 * 0.06 + (volume - 600) * 0.04
else:
    payment = 21 + 300 * 0.06 + 200 * 0.04 + (volume - 800) * 0.025
