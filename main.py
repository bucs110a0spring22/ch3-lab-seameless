import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.speed(1)
leonardo.speed(1)

## 5. your code goes here

##Race 1
x = random.randrange(1,100)
y = random.randrange(1,100)
leonardo.forward(x)
michelangelo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

##Race 2
for i in range(10) :
  a = random.randrange(1,10)
  b = random.randrange(1,10)
  leonardo.forward(a)
  michelangelo.forward(b)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
  
# Part B - complete part B here

for i in range(3) :
  a = 25
  b = (360 / 3)
  michelangelo.down()
  michelangelo.forward(a)
  michelangelo.right(b)
michelangelo.clear()

for i in range(4) :
  a = 25
  b = (360 / 4)
  michelangelo.forward(a)
  michelangelo.right(b)
michelangelo.clear()

for i in range(6) :
  a = 25
  b = (360 / 6)
  michelangelo.forward(a)
  michelangelo.right(b)
michelangelo.clear()

for i in range(9) :
  a = 25
  b = (360 / 9)
  michelangelo.forward(a)
  michelangelo.right(b)
michelangelo.clear()

for i in range(12) :
  a = 25
  b = (360 / 12)
  michelangelo.forward(a)
  michelangelo.right(b)
michelangelo.clear()
window.exitonclick()
