# Python Task 04
# Q7. Python - Split and Join
# HackerRank:
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    result = line.split()
    result = "-".join(result)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
