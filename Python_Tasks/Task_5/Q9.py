```python
# Python Task 09
# Q9. Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

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
```
