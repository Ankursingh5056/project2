import turtle

t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(-2)
# t.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(150):
    t.pencolor(colors[i % 6])
    t.forward(i*5)
    t.right(1200)
    t.fd(50)
    t.rt(100.5)
    t.fd(i*4)
    t.fd(100)
    t.lt(160)

turtle.done()
      



