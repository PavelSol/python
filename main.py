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
        print(mat)
    else:
        break
lengthj = len(mat)
print(lengthi, lengthj, sep = '\t')
