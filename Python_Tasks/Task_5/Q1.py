# Python Task 05
# Q1. Find the Runner-Up Score
# HackerRank:
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    arr = sorted(arr)
    print(arr[-2])
