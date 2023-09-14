import turtle
lados = int(input("Quantidade de lados: "))
comp = int(input("Tamanho das laterais: "))
poly = turtle.Turtle()
 
num_lados = lados
side_length = comp
angle = 360.0 / num_lados
 
for i in range(num_lados):
    poly.forward(side_length)
    poly.right(angle)
     
turtle.done()
