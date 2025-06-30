"""
 This program simulates gravity acting on a ball.
 
 The ball starts off with a random velocity in the x
 direction, and 0 velocity in the y direction.

 With each tick in time, gravity increases the y velocity
 so that the ball is falling faster toward the ground.

 Try playing around with the GRAVITY_ACCELERATION constant
 to see what the ball bounces like with stronger and weaker
 gravitational force!
"""

from tkinter import *
import random
import time

WIDTH = 475
HEIGHT = 275
BALL_DIAMETER = 50
STARTING_Y = 50
STARTING_X = 50
GRAVITY_ACCELERATION = 4
ANIMATION_DELAY = 0.050

root = Tk()

screen = Canvas(root, width=WIDTH, height=HEIGHT, background="white")
screen.pack()

# Create Ball
ball = screen.create_oval(STARTING_X, STARTING_Y, \
    STARTING_X + BALL_DIAMETER, STARTING_Y + BALL_DIAMETER, fill="black")
    
# Initializes the velocity for the ball
velocity_x = random.uniform(1,5)
velocity_y = 0

# If the ball is going off the screen, this function bounces the
# ball back into the canvas.

def check_for_bounce():
    global velocity_x, velocity_y
    # Returns x1, y1, x2, y2
    ball_pos = screen.coords(ball)
    if ball_pos[2] >= WIDTH:
        velocity_x *= -1
        screen.coords(ball, WIDTH - BALL_DIAMETER, ball_pos[1], \
            WIDTH, ball_pos[3])
    if ball_pos[0] <= 0:
        velocity_x *= -1
        screen.coords(ball, 0, ball_pos[1], \
            BALL_DIAMETER, ball_pos[3])
    if ball_pos[3] >= HEIGHT:
        velocity_y = -1 * abs(velocity_y)
        screen.coords(ball,ball_pos[0], HEIGHT - BALL_DIAMETER, \
            ball_pos[2], HEIGHT)
        
    if ball_pos[1] <= 0:
        velocity_y *= -1
        screen.coords(ball,ball_pos[0], 0, \
            ball_pos[2], BALL_DIAMETER)
    screen.update()
    

# Represents one moment in time passing. Moves the ball
# according to the current velocity, and adds the gravity
# acceleration to the y velocity.

def move_ball():
    global velocity_x, velocity_y
    screen.move(ball,velocity_x, velocity_y)
    check_for_bounce()
    velocity_y += GRAVITY_ACCELERATION


while True:
    move_ball()
    screen.update()
    time.sleep(ANIMATION_DELAY)

mainloop()