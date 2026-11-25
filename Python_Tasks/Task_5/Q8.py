```python
# Python Task 08
# Q8. Set .add() - Distinct Country Stamps
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem

s = int(input())
country = set()
for i in range(s):
    name = input()
    country.add(name)
print(len(country))
```
