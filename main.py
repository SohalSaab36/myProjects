import random as rd

def fetchInfo():

    team1Name = input("Name of first team: ")
    team1Match = int(input("No. of match played: "))
    team1Win = int(input("No. of wins: "))

    team2Name = input("Name of second team: ")
    team2Match = int(input("No. of match played: "))
    team2Win = int(input("No. of wins: "))

    strenght1 = team1Win/team1Match
    strenght2 = team2Win/team2Match

    return team1Name,strenght1,team2Name,strenght2

# s1 = 0.3 s2 = 0.6 e = 0.4

def predictScore(tn1,s1,tn2,s2):
    score1 = 0
    score2 = 0
    minutes = 90
    print(s1,s2)
    for i in range(minutes):
        event = rd.uniform(s1-0.2, s2+0.2)
        print(event,end=" ")
        if s1>s2:
            if event < s1:
                score1 =+ 1
            elif event > s1:
                score2 =+ 1
            else:
                score =+ 0
        elif s1<s2:
            if event < s1:
                score1 =+ 1
            elif event > s1 and event<s2:
                score2 =+ 1
            else:
                score =+ 0
        elif s1==s2:
            if event < s1:
                score1 =+ 1
            elif event > s1 and event<s2:
                score2 =+ 1
            else:
                score =+ 0
        print(f'score {score1}-{score2}')
    print(f'final score is {score1}-{score2}')
t1,s1,t2,s2 = fetchInfo()
predictScore(t1,s1,t2,s2)
