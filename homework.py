import random
import math

def getInfo():
    # Get input for the first team
    team1 = input("Name of 1st football team: ")
    teamMatch1 = int(input("Number of matches played: "))
    teamWin1 = int(input("Number of wins: "))
    
    # Get input for the second team
    team2 = input("Name of 2nd football team: ")
    teamMatch2 = int(input("Number of matches played: "))
    teamWin2 = int(input("Number of wins: "))
    
    # Calculate losses for each team
    losses1 = teamMatch1 - teamWin1
    losses2 = teamMatch2 - teamWin2
    
    # Calculate loss ratio for each team
    loss_ratio1 = losses1 / teamMatch1
    loss_ratio2 = losses2 / teamMatch2
    
    # Calculate team strength (for demonstration purposes, using simple strength as before)
    teamStrength1 = 1 - loss_ratio1
    teamStrength2 = 1 - loss_ratio2
    
    # Print team strengths
    print(f"{team1} Strength: {teamStrength1}")
    print(f"{team2} Strength: {teamStrength2}")

    return team1, teamStrength1, team2, teamStrength2

def poisson_distribution(lambda_value):
    # Simulate Poisson distribution using inverse transform sampling
    L = math.exp(-lambda_value)
    k = 0
    p = 1.0
    
    while p > L:
        k = k + 1
        p = p * random.random()
    
    return k - 1

def predictScore(team1, strength1, team2, strength2):
    # Simulate match events using Poisson distribution for goals
    goals_team1 = poisson_distribution(strength1 * 3)  # Adjust the factor for more realistic scoring
    goals_team2 = poisson_distribution(strength2 * 3)  # Adjust the factor for more realistic scoring
    
    print(f"Predicted Score:\n{team1} {goals_team1} - {goals_team2} {team2}")

# Get team information
team1, strength1, team2, strength2 = getInfo()

# Predict and display the score
for klm in range(100):
    predictScore(team1, strength1, team2, strength2)
