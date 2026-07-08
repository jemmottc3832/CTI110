# Christopher Jemmott
# 7-7-2026
# p4Lab1
# A turtle graphics program that draws a house.

import turtle

# Set up the window and background color
win = turtle.Screen()
win.bgcolor("lightblue")

# Create the turtle object and set its color
t = turtle.Turtle()
t.color("green")
t.pensize(3)
t.shape("turtle")

#-------------------------------------------------
# Draw the Square using a 'for' loop
#-------------------------------------------------
# A square has 4 sides, so we loop 4 times
for i in range(4):
    t.forward(100) 
    t.left(90) 

# Move the turtle to the top left corner of the square to start the roof
t.left(90)
t.forward(100)
t.right(90)

#-------------------------------------------------
# Draw the Triangle (roof) using a 'while' loop
#-------------------------------------------------
# A triangle has 3 sides, so we loop 3 times
sides_drawn = 0
while sides_drawn < 3:
    t.forward(100)
    t.left(120)
    sides_drawn += 1

# Hide the turtle after drawing is complete
t.hideturtle()

# Keep the window open until the user clicks it
win.mainloop()






