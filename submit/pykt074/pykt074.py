# pykt074.py

def main():
    # Write your code here
    n = int(input())
    for _ in range(n):
        s = input()
        index = 99
        while (index > 0 and index < len(s) and s[index] != ' '):
            index -= 1
        print(s[:min(index, len(s))])

if __name__ == '__main__':
    main()
