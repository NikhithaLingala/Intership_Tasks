
# Python Task 04
# Q8. What's Your Name?
# HackerRank:
# https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    print(f"Hello {full_name}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
