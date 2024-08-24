# py02007.py
import sys
def main():
    # Write your code here
    input = sys.stdin.read
    data = input().split()
    a = [int(i) % 42 for i in data]
    res = set(a)
    print(len(res))

if __name__ == '__main__':
    main()
