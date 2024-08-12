# py01005.py

def main():
    # Write your code here
    n = input()
    count4 = 0
    count7 = 0
    for c in n:
        if (c == '4'):
            count4 += 1
        elif (c == '7'):
            count7 += 1
    if ((count4 + count7 == 4) | (count4 + count7 == 7)):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
