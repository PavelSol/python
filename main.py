import copy
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
mat2 = copy.deepcopy(mat)
for i in range(0, lengthj):
    for j in range(0, lengthi):
        k = int(mat[i][j])
        if (i < lengthj - 1) and (j < lengthi - 1):
            mat[i][j] = int(mat2[i - 1][j]) + int(mat2[i + 1][j]) + int(mat2[i][j - 1]) + int(mat2[i][j + 1])
        elif (i == lengthj - 1) and (j < lengthi - 1):
            mat[i][j] = int(mat2[i - 1][j]) + int(mat2[0][j]) + int(mat2[i][j - 1]) + int(mat2[i][j + 1])
        elif (j == lengthi - 1) and (i < lengthj - 1):
            mat[i][j] = int(mat2[i - 1][j]) + int(mat2[i + 1][j]) + int(mat2[i][j - 1]) + int(mat2[i][0])
        elif (i == lengthj - 1) and (j == lengthi - 1):
            mat[i][j] = int(mat2[i - 1][j]) + int(mat2[0][j]) + int(mat2[i][j - 1]) + int(mat2[i][0])
for i in range(0, lengthj):
    print(*mat[i])


