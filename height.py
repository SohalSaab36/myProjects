import math

# Constants
g = 10  # Acceleration due to gravity in m/s^2

# User inputs
v = int(input('Enter velocity (m/s): '))
x = int(input('Enter angle in degrees: '))

# Convert angle from degrees to radians
x = math.radians(x)

# Calculate time to reach maximum height
timeMaxHeight = v * math.sin(x) / g

# Calculate maximum height
maxHeight = (v**2 * math.sin(x)**2) / (2 * g)

# Print the results
print(f'Time to reach maximum height: {timeMaxHeight} seconds')
print(f'Maximum height: {maxHeight} meters')
print('Time of flight : ' ,timeMaxHeight*2, ' seconds')
