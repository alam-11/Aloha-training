l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maximum = 0
j, k = 0, 0
for i in range(len(l)):
    temp = []
    for j in range(i, len(l)):
        temp.append(l[j])
        maximum = max(maximum, sum(temp))
print(maximum)
