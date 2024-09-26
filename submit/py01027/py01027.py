# py01027.py
def check(s):
    count = 0
    for c in s:
        if c != '6' and c != '8':
            return False
        if c == '8':
            count += 1
        else:
            count = 0
        if count == 3:
            return False
    return True
        

def main():
    # Write your code here
    s = input()
    if (check(s)) :
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
