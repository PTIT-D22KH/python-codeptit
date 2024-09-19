# py01026.py
def solve(s1, s2):
    d1 = {}
    d2 = {}
    for x in s1:
        if (x not in d1.keys()):
            d1[x] = 0
        else:
            d1[x] += 1
    for x in s2:
        if (x not in d2.keys()):
            d2[x] = 0
        else:
            d2[x] += 1
    for k,v in d1.items():
        if k not in d2.keys() or d2[k] != v:
            return "NO"
    return "YES"
def main():
    # Write your code here
    for t in range(int(input())):
        print(f"Test {t + 1}: ", end = '')
        s1 = input()
        s2 = input()
        print(solve(s1, s2))
        

if __name__ == '__main__':
    main()
