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
               size = size + 5
               size += 5


sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
