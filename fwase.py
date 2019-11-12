from amao import*

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

