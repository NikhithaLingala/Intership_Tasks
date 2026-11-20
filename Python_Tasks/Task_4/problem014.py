# Python Task 04
# Q14. Set .add() - Introduction
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem

s = int(input())
country = set()
for i in range(s):
    name = input()
    country.add(name)
print(len(country))
