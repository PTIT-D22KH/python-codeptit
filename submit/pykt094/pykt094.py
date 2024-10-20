# pykt094.py
class Department:
    dpt_dict = {}
    def __init__(self, s):
        a = s.strip().split(" ")
        self.departmentId = a[0]
        departmentName = ""
        for i in range(1, len(a)):
            departmentName += a[i] + " "
        self.departmentName = departmentName.strip()
        Department.dpt_dict[a[0]] = self.departmentName

class Employee:
    def __init__(self, id, name, basicSal, numDays):
        self.id = id
        self.name = name
        self.basicSal = int(basicSal)
        self.numDays = int(numDays)
        self.department = Department.dpt_dict[id[3:]]
        self.coefficient = self.calCoefficient(id[0], id[1:3])
        self.totalSalary = self.coefficient * self.basicSal * self.numDays * 1000

    def calCoefficient(self, a, b):
        numYears = int(b)
        if a == 'A':
            if numYears >= 16:
                return 20
            elif numYears >= 9:
                return 14
            elif numYears >= 4:
                return 12
            return 10
        elif a == 'B':
            if numYears >= 16:
                return 16
            elif numYears >= 9:
                return 13
            elif numYears >= 4:
                return 11
            return 10
        elif a == 'C':
            if numYears >= 16:
                return 14
            elif numYears >= 9:
                return 12
            elif numYears >= 4:
                return 10
            return 9
        else:
            if numYears >= 16:
                return 13
            elif numYears >= 9:
                return 11
            elif numYears >= 4:
                return 9
        return 8
    def __str__(self):
        return self.id + " " + self.name + " " + self.department + " " + str(self.totalSalary) 
    
def main():
    # Write your code here
    n = int(input())
    departs = []
    employees = []
    for i in range(n):
        departs.append(Department(input()))
    m = int(input())
    for i in range(m):
        employees.append(Employee(input(), input(), input(), input()))
    for x in employees:
        print(str(x))

if __name__ == '__main__':
    main()
