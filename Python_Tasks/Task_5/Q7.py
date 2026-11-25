# Python Task 07
# Q7. Set Symmetric Difference
# HackerRank: Set .symmetric_difference() Operation

A = int(input())
B = set(map(int, input().split()))
C = int(input())
D = set(map(int, input().split()))
E = B.difference(D)
F = D.difference(B)
G = sorted(E.union(F))
for num in G:
    print(num)
```
