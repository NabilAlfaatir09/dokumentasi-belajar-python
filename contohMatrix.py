# matrix dengan ukuran 2 x 2
matrixA = [[1, 0], [0, 1]]
print(matrixA)

# matrix dengan ukuran 3 x 3
matrixB = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
print(matrixB)

# matrix dengan ukuran 4 x 4
matrixC = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
print(matrixC)

# penjumlahan 2 matrix
mat1 = [
    [9, 0],
    [3, 6],
]

mat2 = [
    [6, 0],
    [7, 2],
]

for x in range(0, len(mat1)):
    for y in range(0, len(mat1[0])):
        print(mat1[x][y] + mat2[x][y], end=" "),
        print

# perulangan 2 matrix

matrix1 = [
    [9, 0],
    [3, 6],
]

matrix2 = [
    [6, 0],
    [7, 2],
]

for x in range(0, len(matrix1)):
    for y in range(0, len(matrix1[0])):
        print(matrix1[x][y] - matrix2[x][y], end=" "),
        print

# perkalian 2 matrix
rix1 = [
    [9, 0],
    [3, 6],
]

rix2 = [
    [6, 0],
    [7, 2],
]

rix3 = []

for x in range(0, len(rix1)):
    row = []
    for y in range(0, len(rix1[0])):
        total = 0
        for z in range(0, len(rix1)):
            total = total + (rix1[x][z] * rix2[z][y])
        row.append(total)
    rix3.append(row)

for x in range(0, len(rix3)):
    for y in range(0, len(rix3[0])):
        print(rix3[x][y], end=" ")
    print()
