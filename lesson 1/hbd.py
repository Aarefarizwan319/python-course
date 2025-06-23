import turtle
import time

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Happy Birthday Flower")

# Tuples for colors and coordinates
flower_colors = ("red", "pink", "magenta", "purple")
leaf_color = "green"
stem_color = "darkgreen"
center = (0, -100)

# Draw flower petal
def draw_petal(t, radius, angle):
    t.color(flower_colors[angle % len(flower_colors)])
    t.begin_fill()
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)
    t.end_fill()

# Draw flower center
def draw_center(t):
    t.penup()
    t.goto(center)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# Draw stem
def draw_stem(t):
    t.penup()
    t.goto(0, -100)
    t.setheading(-90)
    t.pendown()
    t.color(stem_color)
    t.pensize(8)
    t.forward(100)

# Draw leaves
def draw_leaf(t, direction):
    t.penup()
    t.goto(0, -50)
    t.setheading(direction)
    t.pendown()
    t.color(leaf_color)
    t.begin_fill()
    t.circle(30, 60)
    t.left(120)
    t.circle(30, 60)
    t.end_fill()

# Write "Happy Birthday"
def write_text(t):
    t.penup()
    t.goto(0, 150)
    t.color("darkred")
    t.write("🎉 Happy Birthday 🎉", align="center", font=("Arial", 24, "bold"))

# Main turtle
flower = turtle.Turtle()
flower.speed(1)

# Draw petals (in loop like animation)
for i in range(6):
    flower.penup()
    flower.goto(center)
    flower.setheading(i * 60)
    flower.forward(60)
    flower.setheading(i * 60 + 60)
    flower.pendown()
    draw_petal(flower, 60, i)
    time.sleep(0.3)

# Draw center, stem, leaves and text
draw_center(flower)
draw_stem(flower)
draw_leaf(flower, 240)
draw_leaf(flower, 300)
write_text(flower)

flower.hideturtle()
turtle.done()
