# py02050.py

def main():
    # Write your code here
    for t in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        st = []
        res = [1] * n
        for i in range(n):
            while (len(st) > 0 and a[i] >= a[st[-1]]):
                st.pop()
            if len(st) == 0:
                res[i] = i + 1
            else:
                res[i] = i - st[-1]
            st.append(i)
        for x in res:
            print(x, end = ' ')
        print()

if __name__ == '__main__':
    main()
