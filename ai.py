import random as rd

def fetchInfo():
    team1Name = input("Name of first team: ")
    team1Match = int(input("No. of matches played by the first team: "))
    team1Win = int(input("No. of wins by the first team: "))

    team2Name = input("Name of second team: ")
    team2Match = int(input("No. of matches played by the second team: "))
    team2Win = int(input("No. of wins by the second team: "))

    if team1Match <= 0 or team2Match <= 0:
        raise ValueError("Number of matches must be positive")

    strength1 = team1Win / team1Match
    strength2 = team2Win / team2Match

    return team1Name, strength1, team2Name, strength2

def predictScore(tn1, s1, tn2, s2):
    score1 = 0
    score2 = 0
    minutes = 90
    # Adjust these values to control the frequency of scoring events
    goal_probability = 0.02  # Adjust the base probability of a goal per minute

    for _ in range(minutes):
        event = rd.uniform(0, 1)
        if event < s1 * goal_probability:
            score1 += 1
        elif event < (s1 + s2) * goal_probability:
            score2 += 1

    return score1, score2

t1, s1, t2, s2 = fetchInfo()
for k in range(100):
    score1, score2 = predictScore(t1, s1, t2, s2)
    print(f'Final score: {t1} {score1} - {score2} {t2}')
