numbers = [8, 3, 12, 1, 6]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print("Smallest number:", minimum)