
# py01014.py
def inputTest():

    try:
        a, k, n = [int(i) for i in input().split()]
        if k == 0:
            raise Exception("k khong the bang 0")
        testCase(a, k, n)
    except Exception as e:
        print(e)
            
            # break
def testCase(a, k, n):
    i = k - (a % k)
    n -= a
    b = []

    while(i <= n):
        b.append(i)
        i += k
    if (len(b) == 0):
        print("-1")
    else:
        for i in b:
            print(i, end = " ")
def main():
    # Write your code here
    inputTest()
    
        

if __name__ == '__main__':
    main()
