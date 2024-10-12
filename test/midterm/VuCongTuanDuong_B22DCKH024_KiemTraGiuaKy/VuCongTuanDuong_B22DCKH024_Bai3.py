print("INPUT")
n = int(input("Nhập n: "))
endU = 1
endE = 1
endO = 1
endA = 1
endI = 1
endOthers = 21
res = 26

for i in range(2, n + 1):
    newEndU = endO + endI + endOthers
    newEndE = endA + endI + endOthers 
    newEndO = endI + endOthers
    newEndA = endE + endU + endI + endOthers
    newEndI = endE + endO + endOthers
    newEndOthers = res * 21
    newRes = newEndU + newEndE + newEndO + newEndA + newEndI + newEndOthers
    endU = newEndU
    endE = newEndE
    endO = newEndO
    endA = newEndA
    endI = newEndI
    endOthers = newEndOthers
    res = newRes
print("OUTPUT")
print(f"Tổng số chuỗi có độ dài {n} được tạo nên bởi quy luật trên: {res}")
