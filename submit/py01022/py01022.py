# py01022.py
def solve(n):
    count = 0
    if count == 0 and len(n) == 1:
        return 1
    while (len(n) != 1):
        sum = 0
        for x in n:
            sum += ord(x) - 48
        n = str(sum)
        count += 1
    return count
def main():
    # Write your code here
    n = input()
    print(solve(n))

if __name__ == '__main__':
    main()
