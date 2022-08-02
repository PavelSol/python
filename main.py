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
    print(*mat[i])

