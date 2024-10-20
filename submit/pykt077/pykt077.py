# pykt077.py
from datetime import datetime
class Course:
    course_dict = {}
    def __init__(self, courseId, name):
        self.courseId = courseId
        self.name = name
        Course.course_dict[courseId] = name
    
class Section:
    count = 0
    def __init__(self, inputString):
        Section.count += 1
        self.id = f"T{Section.count:03d}"
        a = inputString.strip().split(" ")
        self.courseId = a[0]
        self.courseName = Course.course_dict[a[0]]
        self.dateString = a[1] + " " + a[2]
        self.date = datetime.strptime(self.dateString, "%d/%m/%Y %H:%M")
        self.group = a[3]
        # datetime.strftime
        
    def __str__(self):
        return self.id + " " + self.courseId + " " + self.courseName + " " + self.dateString + " " + self.group

def cmp(a):
    return (a.date, a.id)
        
def main():
    # Write your code here
    n, m = [int(i) for i  in input().split()]
    courses = []
    sections = []
    for i in range(n):
        courses.append(Course(input(), input()))
    for i in range(m):
        sections.append(Section(input()))
    sections.sort(key = cmp)
    for x in sections:
        print(str(x))

if __name__ == '__main__':
    main()
