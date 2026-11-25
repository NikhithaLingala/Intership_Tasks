# Python Task 04
# Q19. Collections.Counter()
# HackerRank:
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
n = int(input())
shoe_sizes = list(map(int, input().split()))
shoe_count = Counter(shoe_sizes)
customers = int(input())
earnings = 0
for i in range(customers):
    requested_size, price = map(int, input().split())
    if requested_size in shoe_count:
        if shoe_count[requested_size] > 0:
            shoe_count[requested_size] -= 1
            earnings += price
print(earnings)
