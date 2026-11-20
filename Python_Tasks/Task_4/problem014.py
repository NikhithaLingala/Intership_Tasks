# Python Task 04
# Q13. Sets - Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

A = int(input())
B = set(map(int, input().split()))
C = int(input())
D = set(map(int, input().split()))
E = B.difference(D)
F = D.difference(B)
G = sorted(E.union(F))
for num in G:
    print(num)
