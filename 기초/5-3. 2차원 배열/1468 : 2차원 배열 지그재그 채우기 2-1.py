a = int(input())

num = 1
matrix = []

for i in range(1,a+1):
    wip = []
    for j in range(num , num+a):
        wip.append(j)
        num += 1

    if i % 2 == 0:
        matrix.append(list(reversed(wip)))
        #print(list(reversed(wip)),end=' ')
    else:
        matrix.append(wip)
        #print(wip, end=' ')

for i in matrix:
    print(" ".join(map(str, i)))