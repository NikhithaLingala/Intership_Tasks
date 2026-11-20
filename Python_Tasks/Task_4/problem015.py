
# HackerRank - Task 4 - Q15: Word Order

n = int(input())
d = {}
for i in range(n):
    word = input()
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
print(len(d))
print(" ".join(map(str, d.values())))
