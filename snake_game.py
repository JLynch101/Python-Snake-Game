
#Snake Game by Joe Lynch 10/11/2019
import turtle
import time
import random



delay = 0.1
#Score
score = 0
high_score = 0
#Window Setup
wn = turtle.Screen()
wn.title("Snake Game By Joe")
wn.bgcolor("white")
wn.setup(width=650, height=600)
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction ="stop"


#Snake Body
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.hideturtle()
pen.penup()
pen.goto(40,270)
pen.write("Score: 0   High Score: 0", align="left", font=("Arial", 16, "normal"))

#title
title=turtle.Turtle()
title.speed(0)
title.shape("square")
title.color("black")
title.penup()
title.hideturtle()
title.goto(-80,270)
title.write("Joe's Game of Snake", align="right", font=("Arial", 16, "normal"))


#functions
def go_up():
    if head.direction != "down":
        head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction="down"
def go_left():
    if head.direction != "right":
        head.direction="left"
def go_right():
    if head.direction != "left":
        head.direction="right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

#Keybinds
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



#GameLoop
while True:
    wn.update()

    #Check for collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #Hide Segments
        for segment in segments:
            segment.goto(1000,1000)

        #Clear Segments
        segments.clear()

        # reset delay
        delay = 0.1

        #reset score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Arial", 16, "normal"))

     # Move food to random spot
    if head.distance(food) < 20:
        x = random.randint(-270,270)
        y = random.randint(-270,250)
        food.goto(x,y)

        #Add Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        #increase score
        score += 10

        #Shorten delay
        delay -=0.001

        if score >high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Arial", 16, "normal"))


    #Move the end segment first in reverse
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
 #Move segment - to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()

    #Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide Segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear Segments
            segments.clear()

            #reset delay
            delay = 0.1

            #reset score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="left", font=("Arial", 16, "normal"))
    time.sleep(delay)

wn.mainloop()