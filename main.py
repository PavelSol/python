lst = []
for i in input().split():
    lst1 = input().split()
    for i in range(len(lst1)):
        thr[i] = int(lst1[i])
    lst.append(lst1)
    if input() == "end":
        print(lst)