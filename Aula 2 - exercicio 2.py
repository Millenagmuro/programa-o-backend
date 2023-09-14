import turtle as t
t.color('red')
t.up()
t.backward(100)
t.down()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
