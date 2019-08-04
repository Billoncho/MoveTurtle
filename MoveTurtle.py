# MoveTurtle
# Billy Ridgeway
# Draws with a large turtle shaped pen.

import turtle               # Imports the turtle library.
screen = turtle.Screen()    # Sets the screen to the turtle screen.
pen = turtle.Pen("turtle")  # Makes the pen look like a turtle.
pen.pencolor("yellow")      # Sets the pen's color to yellow.
pen.shapesize(3,3)          # Sets the pen's size.
pen.width(10)               # Sets the pen's width to 10.
turtle.bgcolor("blue")      # Sets the background color to blue.
penspeed = 20               # Sets the pen's speed to 20.
turnspeed = 10              # Sets the turning speed of the pen to 10.

def forward():              # Defines the function forward.
  pen.forward(penspeed)

def backward():             # Defines the function backward.
  pen.backward(penspeed)

def left():                 # Defines the function left.
  pen.left(turnspeed)

def right():                # Defines the function right.
  pen.right(turnspeed)

screen.onkey(forward, "Up")     # Moves the pen forward when the up arrow is pressed.
screen.onkey(backward, "Down")  # Moves the pen down when the down arrow is pressed.
screen.onkey(left, "Left")      # Moves the pen left when the left arrow is pressed.
screen.onkey(right, "Right")    # Moves the pen right when the right arrow is pressed.
screen.listen()                 # Listens for key presses.
