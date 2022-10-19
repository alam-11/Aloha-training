l1 = [1, 2, 4, 7, 89, 6, 95, 64, 4]
l2 = [4, 56, 2, 768, 6, 6, 8, 8]

ans = []
for i in l1:
    if i in l2:
        ans.append(i)
print(ans)
