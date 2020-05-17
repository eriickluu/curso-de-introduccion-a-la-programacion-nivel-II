numbers = [1 ,2, 3, 4, 5]
even = []

for value in numbers:
    if value % 2 == 0:
        even.append(value)

print(even)

def isEven(number):
    return number % 2 == 0

print(list(filter(isEven, numbers)))

print(list(filter((lambda number: number % 2 == 0), numbers)))