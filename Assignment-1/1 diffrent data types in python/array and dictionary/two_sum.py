# two sum problem is the problem where we need to return the index of the
# element which sums up to target


def two_sum(l, target):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == target:
                return [i, j]


data = [2, 3, 11, 7, 8, 4, 5, 9, 0, 2]
print(two_sum(data,8))
