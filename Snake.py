#The game snake using Turtle 

import turtle 
import time #for delay
import random



#global vals
score=0
scores=[0]
delay=0.1 #in seconds
segments=[]
r=0

#setting up the game window

win=turtle.Screen() 
win.title('Snake')
win.bgcolor('Black')
win.setup(width=800,height=800)
win.tracer(0)

#setting up the snake
snk=turtle.Turtle()
snk.shape('square')
snk.color('White')
snk.penup()
snk.goto(0,0)
snk.direction='stop'


#food spawn 

food=turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randint(-350,350),random.randint(-350,350))



def score_p(scores,score=0,run=0):
     pen.write(f'''Run no:{run}, High score:{max(scores)}, current score:{score}''')

pen=turtle.Turtle()
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0,380)
score_p(scores)

#movement

def mov():
    if snk.direction=='up':
        snk.sety(snk.ycor()+20)
    if snk.direction=='down':
        snk.sety(snk.ycor()-20)
    if snk.direction=='left':
        snk.setx(snk.xcor()-20)
    if snk.direction=='right':
        snk.setx(snk.xcor()+20)

#to set direction of movemnt
def mov_up():
    if snk.direction!='down':
      snk.direction='up'
def mov_dwn():
    if snk.direction!='up':
      snk.direction='down'
def mov_lft():
    if snk.direction!='right':
      snk.direction='left'
def mov_rgh():
    if snk.direction!='left':
      snk.direction='right'

win.listen()
win.onkeypress(mov_up,'w')
win.onkeypress(mov_dwn,'s')
win.onkeypress(mov_lft,'a')
win.onkeypress(mov_rgh,'d')





while True:
    win.update()

    if snk.distance(food)<20:
        food.goto(random.randint(-350,350),random.randint(-350,350))
        score+=1
        pen.clear()
        score_p(scores,score,r)
        body=turtle.Turtle()
        body.shape('square')
        body.color('grey')
        body.penup()
        segments.append(body)

    if len(segments)>0:
        x=snk.xcor()
        y=snk.ycor()
        segments[0].goto(x,y)
        

    for i in range(len(segments)-1,0,-1):
        segments[i].goto(segments[i-1].xcor(),segments[i-1].ycor())


    if snk.xcor()>390 or snk.xcor()<-390 or snk.ycor()>390 or snk.ycor()<-390:
        scores.append(score)
        r+=1
        snk.goto(0,0)
        pen.clear()
        score_p(scores,score,r)
        time.sleep(1)
        #need to do this teribleness else the segment still shows up
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

    mov()

    for segment in segments:
        if segment.distance(snk)<20:
              scores.append(score)
              r+=1
              snk.goto(0,0)
              pen.clear()
              score_p(scores,score,r)
              time.sleep(1)
              for segment in segments:
                segment.goto(1000,1000)
              segments.clear()

    time.sleep(delay)
