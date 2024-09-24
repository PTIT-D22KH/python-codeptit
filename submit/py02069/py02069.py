# py02056.py
import math
def isPalindrome(n):
    x = str(n)
    y = x[::-1]
    return len(x) > 1 and x == y
def main():
    # Write your code here
    n, m = [int(i) for i in input().split()]
    a = []
    for i in range(n):
        x = [int(i) for i in input().split()]
        a.append(x)
    max_value = -1
    for i in range(n):
        for j in range(m):
            if isPalindrome(a[i][j]) and a[i][j] > max_value:
                max_value = a[i][j]
    if (max_value == -1):
        print("NOT FOUND")
        return
    print(max_value)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_value:
                print(f"Vi tri [{i}][{j}]")
    
    

if __name__ == '__main__':
    main()
