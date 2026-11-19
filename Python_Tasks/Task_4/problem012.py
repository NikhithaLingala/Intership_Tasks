# Python Task 04
# Q12. Introduction to Sets - Average
# HackerRank:
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    array = set(array)
    array_sum = sum(array)
    total_count = len(array)
    result = array_sum / total_count
    result = round(result, 3)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
