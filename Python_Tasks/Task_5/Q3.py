# Python Task 05
# Q3. Mutate String
# HackerRank:
# https://www.hackerrank.com/challenges/python-mutate-string/problem

def mutate_string(string, position, character):
    s_new = list(string)
    s_new[position] = character
    return "".join(s_new)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
