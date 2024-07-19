import math
g = 10
v = int(input('Enter velocity = '))
x = int(input('Enter angle in degree  = '))
x = math.radians(x)
timeMaxHeight = v * math.sin(x)/g
print(timeMaxHeight)
