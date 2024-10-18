# py04012.py
class Student:
    def __init__(self, id, name, className):
        self.id = id
        self.name = name
        self.className = className
        self.attendance = ""
    
    def __str__(self):
        return self.id + " " + self.name + " " + self.className + " " + self.result
    
    def calAttendanceScore(self):
        score = 10
        for x in self.attendance:
            if x == 'v':
                score -= 2
            elif x == 'm':
                score -= 1
        if score < 0:
            score = 0
        if score == 0:
            self.result = "0 KDDK"
        else:
            self.result = str(score)

        
        
def main():
    # Write your code here
    n = int(input())
    a = []
    for i in range(n):
        a.append(Student(input(), input(), input()))
    
    for i in range(n):
        temp = input().strip().split()
        id = temp[0]
        attendance = temp[1]
        for x in a:
            if x.id == id:
                x.attendance = attendance
                x.calAttendanceScore()
                break
    for x in a:
        print(str(x))           
    


if __name__ == '__main__':
    main()
