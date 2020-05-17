matriz1 = [[1, 2, 3],[7, 8, 9],[13, 14, 15]]
matriz2 = [[4, 5, 6],[10, 11, 12],[14, 15, 16]]
matriz3 = [[1, 2, 3],[7, 8, 9],[13, 14, 15]]

print(matriz1[0][0])
print(matriz2[0][0])

for rowPosition, value in enumerate(matriz1):
    for columPosition, value2 in enumerate(value):
        matriz3[rowPosition][columPosition] = value2 + matriz2[rowPosition][columPosition]

print(matriz3[0][0])