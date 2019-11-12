import turtle

bob = turtle.Turtle()
bob.speed(0)

def tile(c):
    polygon(4, 200,c)
    for times in range(4):
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        polygon(3,100,"black")
        bob.forward(100)
        bob.left(90)
        

def square(distance):
 for times in range(4):
   bob.forward(distance)
   bob.left(90)
  


def triangle(distance):
 for times in range(3):
   bob.forward(distance)
   bob.left(120)



def pentagon(distance):
 sides = 5
 angle = 360 / sides
 for times in range(sides):   
     bob.left(angle)


def polygon(sides,distance, c):
 bob.color( c )
 angle = 360 / sides
 bob. begin_fill()
 for times in range(sides):
      bob.forward(distance)
      bob.left(angle)


def jump(x,y):

 bob.penup()
 bob.goto(x,y)
 bob.pendown()

def star(distance, c):
 bob.color(c)
 bob,beginfill()
 for times in range (5):
    bob.forward(distance)
    bob.left(144)
    bob.end_fill()


def figure1(distance,colr):
 bob.begin_fill()
 bob.color( color )
 bob.circle(50)
 bob.forward( distance )
 bob.circle(50)
 bob.left(45)
 bob.forward(distance)
 bob.right(90)
 bob.forward(distance)
 bob.left(45)
 bob.circle(size)
 bob.forward(distance)
 bob.end_fill()

def fadingTriangle():
    turtle.colormode(255)
    turtle.bgcolor("black")
    bob.speed(0)
    for times in range(50):
         c = (250- times * 5, 250 - times *5, 0)
         polygon(3, 450 - times * 8, c)

def spike(distance):
    for times in range(20):
        c = times * 6
        bob.color(c,c,c)
        bob.width(times * 2)
        bob.forward(distance)
        bob.left(10)

def spikeFlower(distance):
    for times in range(11):
        spike(distance)
        bob.penup()
        bob.home()
        bob.pendown()
        bob.left(times* 36)

def codeofart1(distance):
    bob.speed(0)
    bob.width(5)
    turtle.bgcolor("black")
    bob.color("white")
    for times in range(50):
        bob.circle(900 - times *1 )
        bob.left(5)

def festival(distance):
    bob.speed(0)
    bob.width(5)
    turtle.bgcolor("black")
    bob.color("red")
    for times in range(72):
        bob.circle(900 - times *1)
        bob.left(5)
    bob.color("yellow")
    for times in range(72):
       bob.circle(850 - times *1)
       bob.left(5)
    bob.color("blue")
    for times in range(73):
        bob.circle(800 - times *1)
        bob.left(5)





