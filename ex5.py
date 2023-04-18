numbers_amount = int(input())
number = int(input())
numbers = [int(input()) for _ in range(numbers_amount)]

i = 0
n = 0
while i < number:
    n = numbers.pop(0)
    numbers.extend([n]*n)
    i += 1

print(n)
