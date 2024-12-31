# pykt082.py
def calFinalScore(n):
    if n % 1 < 0.25:
        return int(n)
    if n % 1 >= 0.75:
        return int(n) + 1.0
    if n % 1 >= 0.25 and n % 1 < 0.75 :
        return int(n) + 0.5
def calScore(n):
    dict = {39:9.0, 37:8.5, 35:8.0, 33:7.5, 30:7.0, 27:6.5, 23:6.0, 20:5.5, 16:5.0, 13:4.5, 10:4.0, 7:3.5,5:3.0,3:2.5}
    for key,value in dict.items():
        if n >= key:
            return value
    return -1
def main():
    # Write your code here
    for _ in range(int(input())):
        a = input().split()
        read = int(a[0])
        listen = int(a[1])
        speak = float(a[2])
        write = float(a[3])
        readScore = calScore(read)
        listenScore = calScore(listen)
        score = (speak + write + readScore + listenScore) / 4.0
        finalScore = calFinalScore(score)
        print(finalScore)



if __name__ == '__main__':
    main()
