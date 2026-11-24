import turtle
import random
import colorgram



colors = colorgram.extract('img.jpg',20)
rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r, g, b))

number_of_dots = 100
tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")

tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = turtle.Screen()
screen.exitonclick()





