# pykt080.py

def main():
    # Write your code here
    n, m = [int(i) for i in input().split()]
    a = []
    visited = []
    for _ in range(n):
        x = [int(i) for i in input().split()]
        y = [0 for i in range(m)]
        visited.append(y)
        a.append(x)
    res = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        new_i = i + x
                        new_j = j + y
                        if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m and visited[new_i][new_j] == 0:
                            visited[new_i][new_j] = 1
                            res += a[new_i][new_j]
    print(res)

if __name__ == '__main__':
    main()
