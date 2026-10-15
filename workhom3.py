numbers = [1, 2, 4, 7, 8, 9]

total = 0

for number in numbers:
    if number % 2 == 0:
        total = total + number

print("Sum of even numbers:", total)