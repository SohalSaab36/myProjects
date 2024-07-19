import random as rd
def getInfo():
    team1 = input("Name of 1st football team : ")
    teamMatch1 = int(input("Number of match played "))
    teamWin1 = int(input("Number of Wins : "))
    team2 = input("Name of 2nd football team : ")
    teamMatch2 = int(input("Number of match played "))
    teamWin2 = int(input("Number of Wins : "))
    d1 = teamMatch1-teamWin1
    d2 = teamMatch2-teamWin2
    v1 = d1 /teamMatch1
    v2 = d2 /teamMatch2
    teamStrength1 =  1 - v1
    teamStrength2 = 1 - v2
    print(teamStrength1,' ',teamStrength2)
    return team1, teamStrength1, team2, teamStrength2
def predictScore(t1,s1,t2,s2):
    score1 = 0
    score2 = 0

    events = 90


    for i in range(events):
        
        event = rd.random()
        if s2 < s1:
            if event < s1:
                if event > s2:
                    score1 += 1
            elif event < s2:
                score2 += 1
        elif s1 < s2:
            if event < s2:
                if event > s1:
                    score2 += 1
            elif event < s1:
                score1 += 1
        elif s1 == s2:
            if event < s1:
                if event > s2:
                    score1 += 0
            elif event < s2:
                score2 += 0
    print(f"your teams score are {score1} - {score2}")




