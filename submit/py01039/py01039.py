# py01039.py
def testCase():
    n = input()
    num_dict = {i:0 for i in range(10)}
    for c in n:
        num_dict[int(c)] += 1
    count = 0
    for i, j in num_dict.items():
        if j != 0:
            count += 1
    if (count != 2):
        print("NO")
        return
    l = len(n)
    for i in range(l):
        if (i + 2 < l  and n[i] != n[i + 2]):
            print("NO")
            return
    print("YES")

    
def main():
    # Write your code here
    for t in range(int(input())):
        testCase()




if __name__ == '__main__':
    main()
