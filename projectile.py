import turtle
import math
import tkinter as tk
from tkinter import ttk

# Planetary gravity constants (m/s^2)
planetary_gravity = {
    "Earth": 9.8,
    "Moon": 1.625,
    "Mars": 3.71,
    "Jupiter": 24.79
}

# Function to draw the projectile motion
def draw_projectile_motion(v0, angle, time_step, gravity, screen_width, screen_height):
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=screen_width, height=screen_height)
    screen.setworldcoordinates(0, 0, screen_width, screen_height)
    screen.bgcolor("white")
    
    # Set up the turtle
    projectile = turtle.Turtle()
    projectile.shape("circle")
    projectile.color("blue")
    projectile.penup()
    
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Initial position and velocity
    x = 0
    y = 0
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)
    
    # Simulation loop
    while y >= 0:
        # Update position
        x += vx * time_step
        y += vy * time_step
        
        # Update velocity
        vy -= gravity * time_step
        
        # Move the turtle to the new position
        projectile.goto(x, y)
        projectile.pendown()

    # Hide the turtle and display the screen
    projectile.hideturtle()
    screen.mainloop()

# Function to start the simulation with user input
def start_simulation():
    try:
        initial_velocity = float(velocity_entry.get())
        launch_angle = float(angle_entry.get())
        time_step = float(time_step_entry.get())
        planet = planet_combobox.get()
        
        gravity = planetary_gravity[planet]
        
        # Dynamically calculate screen size based on the initial velocity and gravity
        screen_width = 2 * (initial_velocity**2 * math.sin(2 * math.radians(launch_angle))) / gravity
        screen_height = (initial_velocity**2 * (math.sin(math.radians(launch_angle)))**2) / (2 * gravity)
        
        # Ensure minimum screen size for better visualization
        screen_width = max(screen_width, 800)
        screen_height = max(screen_height, 600)
        
        draw_projectile_motion(initial_velocity, launch_angle, time_step, gravity, screen_width, screen_height)
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Set up the main tkinter window
root = tk.Tk()
root.title("Projectile Motion Simulation")

# Create and place labels, entries, and buttons
ttk.Label(root, text="Initial Velocity (m/s):").grid(column=0, row=0, padx=10, pady=10)
velocity_entry = ttk.Entry(root)
velocity_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Launch Angle (degrees):").grid(column=0, row=1, padx=10, pady=10)
angle_entry = ttk.Entry(root)
angle_entry.grid(column=1, row=1, padx=10, pady=10)

ttk.Label(root, text="Time Step (seconds):").grid(column=0, row=2, padx=10, pady=10)
time_step_entry = ttk.Entry(root)
time_step_entry.grid(column=1, row=2, padx=10, pady=10)

ttk.Label(root, text="Select Planet:").grid(column=0, row=3, padx=10, pady=10)
planet_combobox = ttk.Combobox(root, values=list(planetary_gravity.keys()))
planet_combobox.grid(column=1, row=3, padx=10, pady=10)
planet_combobox.set("Earth")  # Default selection

start_button = ttk.Button(root, text="Start Simulation", command=start_simulation)
start_button.grid(column=0, row=4, columnspan=2, padx=10, pady=20)

result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=5, columnspan=2)

# Run the tkinter event loop
root.mainloop()
