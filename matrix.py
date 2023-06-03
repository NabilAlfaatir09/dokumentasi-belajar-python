print("KELOMPOK 7")
print("NO   |   NAMA            |   NIM     |   KELAS   |")
print("1    |   Nabil Alfaatir  | 17220451  |   17.1A.12|")
print("2    |   Muhammad Alfi   | 17220381  |   17.1A.12|")
print("3    |   Muhammad Farhan | 17221074  |   17.1A.12|")
print("4    |   Romy Naufal Azra| 17220861  |   17.1A.12|")

matrix1 = [
    [1, 7, 4],
    [2, 6, 5],
    [3, 9, 6]
]
matrix2 = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]
print('\nmatrix 1 :')
print('', matrix1[0], '\t\n', matrix1[1], '\t\n', matrix1[2])
print('\nmatrix 2 :')
print('', matrix2[0], '\t\n', matrix2[1], '\t\n', matrix2[2], '\n')
for i in range(0, len(matrix1)):
    for j in range(0, len(matrix1[0])):
        print(matrix1[i][j]+matrix2[i][j], end=' '),
    print('\n')
