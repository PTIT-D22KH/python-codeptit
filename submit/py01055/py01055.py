# py01055.py
def check(n):
    l = len(n)
    if (l % 2 == 0):
        return False
    if (n[0] == n[1]):
        return False
    x = n[0]
    for i in range(2, l, 2):
        if (n[i] != x):
            return False
    return True
def main():
    # Write your code here
    for t in range(int(input())):
        n = input()
        if (check(n)):
            print("YES")
        else:
            print("NO")
        
        

if __name__ == '__main__':
    main()
