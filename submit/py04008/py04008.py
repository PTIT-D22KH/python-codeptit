# py04008.py
class Matrix:
    def __init__(self, rows, columns, matrix) -> None:
        self.rows = rows
        self.columns = columns
        self.matrix = matrix

    def multiplyTranposeMatrix(self):
        t = []
        for i in range(self.columns):
            x = []
            for j in range(self.rows):
                x.append(self.matrix[j][i])
            t.append(x)
        res = [[0 for _ in range(self.rows)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.rows):
                for k in range(self.columns):
                    res[i][j] += self.matrix[i][k] * t[k][j]
        return res
    
def main():
    # Write your code here
    t = int(input())
    ip = []

    while True:
        try:
            ip.extend([int(i) for i in input().split()])
        except: 
            break
    curr = 0
    for x in range(t):
        n, m = ip[curr], ip[curr+1]
        curr += 2
        a = []
        for i in range(n):
            a.append([0] * m)
        while (len(ip) - curr < n * m):
            ip.append(0)
        for i in range(n):
            for j in range(m):
                a[i][j] = ip[curr + j]
        mat = Matrix(n, m, a)
        result = mat.multiplyTranposeMatrix()
        for row in result:
            print(" ".join(map(str, row)))     


if __name__ == '__main__':
    main()
