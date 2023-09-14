import turtle
wn = turtle.Screen()
wn.bgcolor("white")
skk = turtle.Turtle()
skk.color("Blue")
#cor = ['red', 'blue', 'green', 'yellow']
skk.pensize(2)

def sqrfunc(size) :
       for i in range(4):
              #skk.color(cor[i % len(cor)])
               skk.fd(size)
               skk.left(90)
               size = size + 10
               size += 10


sqrfunc(15)
sqrfunc(25)
sqrfunc(35)
sqrfunc(45)
sqrfunc(55)
sqrfunc(65)
sqrfunc(75)
