import turtle
import random
Score=0
s=turtle.Screen()
s.setup(600,600)
s.title('بازي توپ و لاکپشت')
s.bgcolor('coral')
#ترسيم ديوار
wall=turtle.Turtle()
wall.up()
wall.goto(-275,275)
wall.down()
wall.width(4)
for i in range(4):
    wall.fd(550)
    wall.rt(90)
wall.ht()
#ايجاد شخصيت بازي
laki=turtle.Turtle()
laki.shape('turtle')
laki.color('dark green')
laki.shapesize(2)
laki.up()
#ايجاد شخصيت توپ
ball=turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.up()
ball.goto(random.randint(-260,260),random.randint(-260,260))
#چاپ امتياز
wr=turtle.Turtle()
wr.up()
wr.goto(-270,275)
wr.ht()
wr.color('navy')
wr.write('امتياز='+str(Score),font=('b Nazanin',12,'bold'))
#توابع حرکت لاکپشت با کيبورد
def move_right():
    laki.right(30)
def move_left():
    laki.left(30)
s.listen()
s.onkey(move_right,'Right')
s.onkey(move_left,'Left')
#حرکت مداوم
while True:
 laki.fd(1)
 if laki.xcor()>270 or laki.xcor()<-270 or laki.ycor()>270 or laki.ycor()<-270:
     laki.right(180)
     Score=Score-2
     wr.clear()
     wr.write('امتياز='+str(Score),font=('b Nazanin',12,'bold'))
 if laki.distance(ball)<15:
     ball.goto(random.randint(-260,260),random.randint(-260,260))
     Score=Score+10
     wr.clear()
     wr.write('امتياز='+str(Score),font=('b Nazanin',12,'bold'))
 if Score>=50:
     wr.goto(-75,0)
     wr.write('شما موفق شديد',font=('b Nazanin',25,'bold'))
     break

     
     
