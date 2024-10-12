def maximalSquare(matrix):
    if not matrix:
        return 0, []

    rows = len(matrix)
    cols = len(matrix[0])
    dp = []
    for i in range(rows):
        dp.append([0] * cols)
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
                    squares = []
                    top_left = [i - max_side + 1, j - max_side + 1]
                    bottom_right = [i, j]
                    squares.append([top_left, bottom_right])
                elif dp[i][j] == max_side:
                    top_left = [i - max_side + 1, j - max_side + 1]
                    bottom_right = [i, j]
                    squares.append([top_left, bottom_right])

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
            if not stack:
                w = i
            else:
                w = i - stack[-1] - 1
            area = h * w
            if area > max_area:
                max_area = area
                coords = []
                top_left = [row - h + 1, i - w]
                bottom_right = [row, i - 1]
                coords.append([top_left, bottom_right])
            elif area == max_area:
                top_left = [row - h + 1, i - w]
                bottom_right = [row, i - 1]
                coords.append([top_left, bottom_right])
        stack.append(i)

    heights.pop()
    return max_area, coords

def main():
    n = int(input("Nhập số hàng: "))
    m = int(input("Nhập số cột: "))
    matrix = []
    print("Nhập ma trận:")
    for i in range(n):
        row = []
        row_input = input().split()
        for num in row_input:
            row.append(int(num))
        matrix.append(row)

    square_area, square_coords = maximalSquare(matrix)
    print(f"Diện tích hình vuông lớn nhất = {square_area}")
    for coord in square_coords:
        # print(coord)
        print([[coord[0][0] + 1, coord[0][1] + 1], [coord[1][0] + 1, coord[1][1] + 1]])

    rectangle_area, rectangle_coords = maximalRectangle(matrix)
    print(f"Diện tích hình chữ nhật lớn nhất = {rectangle_area}")
    for coord in rectangle_coords:
        # print(coord)
        print([[coord[0][0] + 1, coord[0][1] + 1], [coord[1][0] + 1, coord[1][1] + 1]])

if __name__ == "__main__":
    main()