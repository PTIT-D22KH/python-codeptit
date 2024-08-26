# py01025.py

def main():
    # Write your code here
    s = input()
    x = ""
    count = 0
    for i in range(len(s) - 1, 0, -1):
        # print(s[i], end = '')
        count += 1
        x += s[i]
        if (count == 3):
            x += ","
            count = 0
    x += s[0]
    res = x[::-1]
    print(res)

        

if __name__ == '__main__':
    main()
