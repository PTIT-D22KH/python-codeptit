def result(a, res):
    count = 0
    x = int(''.join(map(str, a)))
    y = str(x)
    n = len(y)
    for c in y:
        if c == '2':
            count += 1
    if count > (n // 2):
        res.append(x)
        
def Try(i, n, a, res):
    for j in range(0, 3):
        a[i] = j
        if i == 9:
            result(a, res)
        elif i < 9:
            Try(i + 1, n, a, res)

def main():
    # Read the number of test cases
    for _ in range(int(input())):
        n = int(input())
        # print(n)
        a = [0] * 10
        res = []
        Try(0, n, a, res)
        res.sort()
        for i in range(n):
            print(res[i], end=' ')
        print()

if __name__ == '__main__':
    main()