# imports
import turtle  # for the gui
import time  # to set delays and speed up snake after each time it gets food
import random  # to randomly place food on the wneen
from general_ui import App

delay = 0.1
# scores
score = 0
high_score = 0

# set up Screen
wn = turtle.Screen()  # GUI
wn.title("SNAKE GAME")  # game title
wn.bgcolor("Pink")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# snake food
food = turtle.Turtle()
food.speed(0)
colory=random.choice(["red","yellow"])
food.shape("circle")
food.color(colory)
food.penup()
food.goto(100, 100)
segments = []  # use this list to store body of snake

#negative snake food
food2 = turtle.Turtle()
food2.speed(0)
colorz=random.choice(["red","yellow"])

#colour checker
def color_checkr(colory,colorz):
    while True:
        if colorz == colory:
            colorz = random.choice(["red", "yellow"])
            continue
        else:
            break
    return colorz

colorz=color_checkr(colory,colorz)

food2.shape("circle")
food2.color(colorz)
food2.penup()
food2.goto(-100, 100)

#questions
ques = turtle.Turtle()
ques.speed(0)
ques.shape("square")
ques.color("blue")
ques.penup()
ques.hideturtle()
ques.goto(0, 200)

#Rules
str1 = ['RULES', '1) Use W,A,S,D to move the snake','2) Based on the question move the snake', 'to the food of given colour ', '<Y>-YELLOW', '<R>-RED']
draw1 = turtle.Turtle()
draw1.speed(0)
draw1.shape("square")
draw1.color("yellow")
draw1.penup()
draw1.hideturtle()
draw1.goto(0, 250)
for i in str1:
    draw1.write(i, align="center",
                font=("candara", 24, "bold"))
    time.sleep(3)
    draw1.clear()

# scoreboard
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("yellow")
sc.penup()
sc.hideturtle()
sc.goto(0, 250)
if colory=="red":
    sc.write("Pass Snake through red circle to start", align="center",
             font=("candara", 24, "bold"))
else:
    sc.write("Pass Snake through yellow circle to start", align="center",
             font=("candara", 24, "bold"))

# functions
def randomq(colory):
    randomqn=random.randint(1,10)
    if randomqn==1:
        if colory=="red":
            return "WHAT IS 150+20?  <R> 170   <Y> 137"
        else:
            return "WHAT IS 150+20?  <Y> 170   <R> 137"


    elif randomqn==2:
        if colory == "red":
            return "WHAT IS 15+20?   <R> 35    <Y> 37"
        else:
            return "WHAT IS 15+20?   <Y> 35    <R> 37"
    elif randomqn==3:
        if colory=="red":
            return "WHAT IS 3*4?     <R> 12    <Y> 8"
        else:
            return "WHAT IS 3*4?     <Y> 12    <R> 8"
    elif randomqn==4:
        if colory=="red":
            return "WHAT IS 15*2?    <Y> 10    <R> 30"
        else:
            return "WHAT IS 15*2?    <R> 10    <Y> 30"

    elif randomqn==5:
        if colory == "red":
            return "WHAT IS 15+2?    <Y> 13    <R> 17"
        else:
            return "WHAT IS 15+2?    <R> 13    <Y> 17"
    elif randomqn==6:
        if colory == "red":
            return "WHAT IS 15-5?    <R> 10    <Y> 30"
        else:
            return "WHAT IS 15-5?    <Y> 10    <R> 30"
    elif randomqn==7:
        if colory == "red":
            return "WHAT IS 15*0?    <R> 0     <Y> 30"
        else:
            return "WHAT IS 15*0?    <Y> 0     <R> 30"
    elif randomqn==8:
        if colory == "red":
            return "WHAT IS 15/3?    <Y> 5     <R> 3"
        else:
            return "WHAT IS 15/3?    <R> 5     <Y> 3"
    elif randomqn==9:
        if colory == "red":
            return "WHAT IS A VOWEL? <Y> B     <R> A"
        else:
            return "WHAT IS A VOWEL? <Y> A     <R> B"
    elif randomqn==10:
        if colory == "red":
            return "WHAT IS 15-2?    <Y> 10    <R>13"
        else:
            return "WHAT IS 15-2?    <R> 10    <Y>13"



def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keybindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# main game loop
while high_score<100:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:  # boundaries
        time.sleep(1)
        head.goto(0, 0)  # resets head position back to the start point
        head.direction = "Stop"  # resets head's direction so it doesnt move
        for segment in segments:  # reseting the body of snake
            segment.goto(2000, 2000)
        segments.clear()  # clearing the list that contained the body
        score = 0  # score reset
        delay = 0.1  # reset delay
        sc.clear()  # display game over msg essentially
        sc.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
        

    # collision of food with head
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 200)
        food.goto((x, y))
        x1 = random.randint(-270, 270)
        y1 = random.randint(-270, 200)

        food2.goto((x1, y1))

        colory=random.choice(["red","yellow"])
        food.color(colory)

        colorz = random.choice(["red", "yellow"])
        colorz=color_checkr(colory,colorz)
        food2.color(colorz)

        new_segment = turtle.Turtle()  # creating a body after snakes eats food
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("Black")
        new_segment.penup()
        segments.append(new_segment)  # adding length to the list which essentially acts as the body of the snake
        delay -= 0.001  # shortens time period so essentially speeds up game
        score += 10
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
        ques.clear()
        ques.write(randomq(colory), align="center", font=("candara", 20, "bold"))

    if head.distance(food2) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 200)

        food2.goto((x, y))
        x1 = random.randint(-270, 270)
        y1 = random.randint(-270, 200)

        food.goto((x1, y1))

        colory = random.choice(["red", "yellow"])
        food.color(colory)

        colorz = random.choice(["red", "yellow"])
        colorz = color_checkr(colory, colorz)
        food2.color(colorz)

        if len(segments)>0:
            a=segments.pop()  # adding length to the list which essentially acts as the body of the snake
            a.goto(1000,1000)
            delay += 0.001  # shortens time period so essentially speeds up game
            score -= 10
            if score > high_score:
                high_score = score
            sc.clear()
            sc.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
            ques.clear()
            ques.write(randomq(colory), align="center", font=("candara", 20, "bold"))
        else:
            time.sleep(2)
            head.goto(0, 0)  # resets head position back to the start point
            head.direction = "Stop"  # resets head's direction so it doesnt move
            continue




    for index in range(len(segments) - 1, 0, -1):  # moving body via index
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:  # start to the body follows the head
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    for segment in segments:
        if segment.distance(head) < 20:  # boundaries
            time.sleep(1)
            head.goto(0, 0)  # resets head position back to the start point
            head.direction = "Stop"  # resets head's direction so it doesnt move
            for segment in segments:  # reseting the body of snake
                segment.goto(2000, 2000)
            segments.clear()  # clearing the list that contained the body
            score = 0  # score reset
            delay = 0.1  # reset delay
            sc.clear()  # display game over msg essentially
            sc.write("Score : {} High Score : {} ".format(score, high_score), align="center",
                     font=("candara", 24, "bold"))
    time.sleep(delay)
else:
    time.sleep(3)
    ques.clear()
    food2.clear()
    food.clear()
    head.clear()
    new_segment.clear()
    sc.clear()  # display game over msg essentially
    sc.write("GAME OVER U WON!!!! ".format(score, high_score), align="center",
             font=("candara", 24, "bold"))
    time.sleep(3)

    wn.bye()

wn.mainloop()

