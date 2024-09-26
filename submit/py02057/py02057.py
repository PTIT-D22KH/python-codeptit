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
    max_value = 0
    min_value = 1e5
    for i in range(n):
        max_temp = max(a[i])
        min_temp = min(a[i])
        max_value = max(max_temp, max_value)
        min_value = min(min_temp, min_value)
    lucky_number = max_value - min_value
    for i in range(n):
        for j in range(m):
            if a[i][j] > max_value:
                max_value = a[i][j]
    
    
    ok = False
    for i in range(n):
        if lucky_number in a[i]:
            ok = True
            break
    if not ok:
        print("NOT FOUND")
        return

    print(lucky_number)
    for i in range(n):
        for j in range(m):
            if a[i][j] == lucky_number:
                print(f"Vi tri [{i}][{j}]")
                ok = True
    
    
    

if __name__ == '__main__':
    main()
