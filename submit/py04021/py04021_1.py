from datetime import datetime
class Gamer:
    def __init__(self, id, name, timeIn, timeOut):
        self.id = id
        self.name = name
        self.timeIn = datetime.strptime(timeIn, '%H:%M')
        self.timeOut = datetime.strptime(timeOut, '%H:%M')
        self.time = self.timeOut - self.timeIn
    def __str__(self):
        totalMins = self.time.total_seconds() // 60
        hours = int(totalMins // 60)
        mins = int(totalMins - hours * 60)
        return self.id + " " + self.name + " " + f"{hours} gio {mins} phut"

def cmp(a) :
    return (-a.time)
a = []
for _ in range(int(input())):
    a.append(Gamer(input(), input(), input(), input()))
a.sort(key = cmp)
for x  in a:
    print(str(x))

        