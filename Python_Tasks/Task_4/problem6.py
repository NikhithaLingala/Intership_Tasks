
# Python Task 04
# Q6. Finding the Runner-Up Score!
# HackerRank:
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr = set(arr)
    arr = sorted(arr)

    print(arr[-2])
