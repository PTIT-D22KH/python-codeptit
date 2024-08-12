# py01002.py

def main():
    # Write your code here
    s = input()
    l = s.split(" ")
    a = int(l[0])
    b = int(l[2])
    c = int(l[4])
    if (a + b == c):
        print("YES")
    else:
        print("NO")
    
if __name__ == '__main__':
    main()
