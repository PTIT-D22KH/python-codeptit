# pykt096.py
class Team:
    team_dict = {}
    count = 0
    def __init__(self, teamName, school):
        Team.count += 1
        self.teamId = f"Team{Team.count:02d}"
        self.teamName = teamName
        self.school = school
        Team.team_dict[self.teamId] = self
    

class Contestant:
    count = 0
    def __init__(self, name, teamId):
        Contestant.count += 1
        self.id = f"C{Contestant.count:03d}"
        self.name = name
        self.teamName = Team.team_dict[teamId].teamName
        self.school = Team.team_dict[teamId].school

    def __str__(self):
        return self.id + " " + self.name + " " + self.teamName + " " + self.school

def cmp(a):
    return (a.name)
        
def main():
    # Write your code here
    n = int(input())
    a = []
    for i in range(n):
        a.append(Team(input(),input()))
    b = []
    m = int(input())
    for i in range(m):
        b.append(Contestant(input(), input()))
    b.sort(key = cmp)
    for x in b:
        print(str(x))

if __name__ == '__main__':
    main()
