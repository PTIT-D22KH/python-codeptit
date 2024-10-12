def maximalSquare(matrix):
    if not matrix:
        return 0, []

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0
    squares = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
                    squares = [((i - max_side + 1, j - max_side + 1), (i, j))]
                elif dp[i][j] == max_side:
                    squares.append(((i - max_side + 1, j - max_side + 1), (i, j)))

    return max_side * max_side, squares

def maximalRectangle(matrix):
    if not matrix:
        return 0, []

    rows = len(matrix)
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0
    rectangles = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        area, coords = largestRectangleArea(heights, i)
        if area > max_area:
            max_area = area
            rectangles = coords
        elif area == max_area:
            rectangles.extend(coords)

    return max_area, rectangles

def largestRectangleArea(heights, row):
    stack = []
    max_area = 0
    heights.append(0)
    coords = []

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            area = h * w
            if area > max_area:
                max_area = area
                coords = [((row - h + 1, i - w), (row, i - 1))]
            elif area == max_area:
                coords.append(((row - h + 1, i - w), (row, i - 1)))
        stack.append(i)

    heights.pop()
    return max_area, coords

def main():
    n = int(input("Enter number of rows: "))
    m = int(input("Enter number of columns: "))
    matrix = []
    print("Enter the matrix row by row:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    square_area, square_coords = maximalSquare(matrix)
    print("Maximal Square Area:", square_area)
    for coord in square_coords:
        print("Top-left:", (coord[0][0] + 1, coord[0][1] + 1), "Bottom-right:", (coord[1][0] + 1, coord[1][1] + 1))

    rectangle_area, rectangle_coords = maximalRectangle(matrix)
    print("Maximal Rectangle Area:", rectangle_area)
    for coord in rectangle_coords:
        print("Top-left:", (coord[0][0] + 1, coord[0][1] + 1), "Bottom-right:", (coord[1][0] + 1, coord[1][1] + 1))

if __name__ == "__main__":
    main()