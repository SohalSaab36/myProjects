import math
def ask():
    global theta
    global A
    global B
    theta = math.radians(int(input('Enter angle btw vector = ')))
    A = int(input('Enter maginitude of A vector = '))
    B = int(input('Enter magnitude of B vector = '))
    return theta,A,B
def findResultant():
    t,a,b = ask()
    resultant = math.sqrt(A**2+B**2+2*A*B*math.cos(t))
    return resultant
print(findResultant())