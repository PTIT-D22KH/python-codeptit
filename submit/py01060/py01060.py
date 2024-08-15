# py01060.py
def testCase():
    n = input()
    has0 = False
    sumEven = 0
    productOdd = 1
    for i in range(len(n)):
        if (i % 2 == 1):
            sumEven += int(n[i])
        else:
            if(n[i] != '0'):
                has0 = True
                productOdd *= int(n[i])
    # if (has0 == False):
    #     productOdd = 0
    print(productOdd, sumEven)

def main():
    # Write your code here
    for t in range(int(input())):
        testCase()

if __name__ == '__main__':
    main()
