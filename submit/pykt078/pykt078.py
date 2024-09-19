# pykt078.py
def solve(a, n, m):
    max_val = max(a)
    index = a.index(max_val)
    a.insert(index, m)

    negatives = [x for x in a if x < 0]
    non_negatives = [x for x in a if x >= 0]

    new_arr = negatives + non_negatives
    return new_arr


def main():
    # Write your code here
    for _ in range(int(input())):
        n, m = [int(i) for i in input().split()]
        a = [int(i) for i in input().split()]
        res = solve(a, n, m)
        for x in res:
            print(x, end = ' ')
        print()

if __name__ == '__main__':
    main()
