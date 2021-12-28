import turtle

ethan = turtle.Turtle()
ethan.speed(100)
ethan.pensize(0.5)
turtle.bgcolor('black')

col = ['red', 'orange', 'yellow', 'green', 'blue']
for direction in range(8):
    ethan.left(45)
    ethan.color('white')
    for b in range(25):
        #ethan.color(col[b % 5])
        ethan.circle(b * 5)
    

turtle.done()