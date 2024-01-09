import time
clock = time.localtime()
y = clock.tm_hour
k = clock.tm_min
print(f'Es ist {y} Uhr {k}.')