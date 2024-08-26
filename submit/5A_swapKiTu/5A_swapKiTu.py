# 5A_swapKiTu.py

def main():
    # Write your code here
    s = input()
    t = input()
    for i in range(len(s)):
        if (s[i] != t[i]) :
            s = s[:i] + s[i:].replace(s[i], t[i]) 
            s = s[:i] + s[i:].replace(t[i], s[i])
            print(s)
    if (s == t):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
