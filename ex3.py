import time

first_number = int(input())
second_number = int(input())

start_time = time.time()

length = 0
for i in range(first_number, second_number+1):
    length += len(str(i))

print(length)
print(time.time() - start_time)
