mat = []
lst = input().split()
lengthi = len(lst)
mat.append(lst)
b = []
cl = 1
while cl == 1:
    b = input().split()
    if b[0] != "end":
        mat.append(b)
    else:
        break
lengthj = len(mat)
for i in range(0, lengthj):
    for j in range(0, lengthi):
        k = int(mat[i][j])
        mat[i][j] = int(mat[i - 1][j]) + int(mat[i + 1][j]) + int(mat[i][j - 1]) + int(mat[i][j + 1])
for i in range(0, lengthj):         #вывод матрицы
    print(*mat[i])


