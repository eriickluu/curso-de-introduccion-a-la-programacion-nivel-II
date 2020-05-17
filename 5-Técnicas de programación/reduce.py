import functools

numbers = [1, 2, 3, 4, 5]
result = 0

for number in numbers:
    result = result + number    

print(result)

print(str(functools.reduce((lambda x, y: x + y), numbers)))