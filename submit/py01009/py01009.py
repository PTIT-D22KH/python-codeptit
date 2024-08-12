# py01009.py

def main():
    # Write your code here
    s = input()
    countUpper = 0
    countLower = 0
    for c in s:
        if (c >= 'a' and c <= 'z') :
            countLower += 1
        elif (c >= 'A' and c <= 'Z'):
            countUpper += 1
    if (countLower >= countUpper):
        print(s.lower())
    else:
        print(s.upper())
    

if __name__ == '__main__':
    main()
