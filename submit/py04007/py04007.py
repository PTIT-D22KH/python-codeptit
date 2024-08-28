# py04007.py
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
    for t in range(int(input())):
        n, m = [int(i) for i in input().split()]
        a = []
        for i in range(n):
            x = [int(j) for j in input().split()]
            a.append(x)
        mat = Matrix(n, m, a)
        result = mat.multiplyTranposeMatrix()
        for row in result:
            print(" ".join(map(str, row)))



if __name__ == '__main__':
    main()
