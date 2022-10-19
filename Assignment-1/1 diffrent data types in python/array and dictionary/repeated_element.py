from collections import Counter

data = [1, 2, 2, 7, 44, 51, 1, 4, 4, 55, 3, 7, 78, 8, 9, 9, 666, 66, 555, 5]

freq = dict(Counter(data))
print(freq)

for k, v in freq.items():
    if v > 1:
        print(k, end=",")
