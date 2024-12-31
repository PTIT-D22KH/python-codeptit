# pykt070.py
from datetime import datetime
class Course:
    def __init__(self, courseId, name, type):
        self.courseId = courseId
        self.name = name
        self.type = type
    def __str__(self):
        return self.name

class Schedule:
    count = 0
    def __init__(self, time, start, room):
        Schedule.count += 1
        self.id = f"C{Schedule.count:03d}"
        self.time = datetime.strptime(time, '%d/%m/%Y')
        self.start = datetime.strptime(start, '%H:%M')
        self.totalTime = datetime.strptime(time + " " + start, '%d/%m/%Y %H:%M')
        self.room = room
    def __str__(self):
        return datetime.strftime(self.time, '%d/%m/%Y') + " " + datetime.strftime(self.start, '%H:%M') + " " + self.room

class Timetable:
    def __init__(self, course, schedule, group, numStudents):
        self.course = course
        self.schedule = schedule
        self.group = group
        self.numStudents = numStudents
    def __str__(self):
        return str(self.schedule) + " " + str(self.course) + " " + self.group + " " + self.numStudents

def cmp(a):
    return (a.schedule.totalTime, a.schedule.id)

def main():
    # Write your code here
    a = []
    b = []
    c = []
    with open("MONTHI.in", 'r') as file:
        a = file.readlines()
    with open("CATHI.in", 'r') as file:
        b = file.readlines()
    with open("LICHTHI.in", 'r') as file:
        c = file.readlines()
    courses = []
    schedules = []
    timetables = []
    curr = 1
    n = int(a[0])
    for _ in range(n):
        courses.append(Course(a[curr].strip(), a[curr + 1].strip(), a[curr + 2].strip()))
        curr += 3
    curr = 1
    n = int(b[0])
    for _ in range(n):
        schedules.append(Schedule(b[curr].strip(), b[curr + 1].strip(), b[curr + 2].strip()))
        curr += 3
    curr = 1
    n = int(c[0])
    for _ in range(n):
        s = c[curr].split()
        id = s[0]
        courseId = s[1]
        course = None
        schedule = None
        for x in schedules:
            if x.id == id:
                schedule = x
                break
        for x in courses:
            if x.courseId == courseId:
                course = x
                break
        timetables.append(Timetable(course, schedule, s[2], s[3]))

        curr += 1
    timetables.sort(key = cmp)
    for x in timetables:
        print(str(x))

if __name__ == '__main__':
    main()
