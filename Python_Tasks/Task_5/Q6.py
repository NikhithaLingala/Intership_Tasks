# Python Task 06
# Q6. Average
# HackerRank: Mean, Median, and Mode

def average(array):
    array = set(array)
    array_sum = sum(array)
    total_count = len(array)
    average = array_sum / total_count
    average = round(average, 3)
    return average
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
```
