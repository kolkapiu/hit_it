from turtle import *

class Sprite(Turtle):
    def __init__(self, x, y, step = 10, shape = 'circle', color = 'black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())


    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

zero = 0

t1 = Turtle()
t1.size = 5
t1.speed = 100
t1.penup()
t1.goto(-200, -200)
t1.pendown()

for i in range(4):
    t1.forward(390)
    t1.left(90)
t1.hideturtle

t2 = Turtle()
t2.penup()
t2.goto(-190, 170)
t2.pendown()
t2.write(zero, font=('Arial', 16, 'bold'))
t2.hideturtle()


player = Sprite(0, -190, 10, 'circle', 'orange')

enemy1 = Sprite(-192, -140, 10, 'square', 'blue')
enemy1.set_move(-192, -140, 192, -140)
enemy2 = Sprite(192, -80, 10, 'square', 'blue')
enemy2.set_move(192, -80, -192, -80)
enemy3 = Sprite(-192, -20, 10, 'square', 'blue')
enemy3.set_move(-192, -20, 192, -20)

goal = Sprite(0, 150, 10, 'triangle', 'green')

scr = player.getscreen()
scr.listen()

scr.onkey(player.move_up, 'w')
scr.onkey(player.move_down, 's')
scr.onkey(player.move_right, 'd')
scr.onkey(player.move_left, 'a')


total_score = 0
while total_score < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(goal):
        player.goto(0, -190)
        total_score += 1
        zero += 1
        t2.clear()
        t2.write(zero, font=('Arial', 16, 'bold'))

    if player.is_collide(enemy1):
        goal.hideturtle()
        t3 = Turtle()
        t3.speed = 100
        t3.penup()
        t3.goto(-70, 0)
        t3.pendown()
        t3.write('GAME OVER', font=('Arial', 16, 'bold'))
        t3.hideturtle()
        break
    
    if player.is_collide(enemy2):
        goal.hideturtle()
        t3 = Turtle()
        t3.speed = 100
        t3.penup()
        t3.goto(-70, 0)
        t3.pendown()
        t3.write('GAME OVER', font=('Arial', 16, 'bold'))
        t3.hideturtle()
        break

    if player.is_collide(enemy3):
        goal.hideturtle()
        t3 = Turtle()
        t3.speed = 100
        t3.penup()
        t3.goto(-70, 0)
        t3.pendown()
        t3.write('GAME OVER', font=('Arial', 16, 'bold'))
        t3.hideturtle()
        break

    if player.xcor() >= 192 or player.xcor() <= -192 or player.ycor() >= 192 or player.ycor() <= -192:
        player.goto(0, -190)

if total_score == 3:
    t4 = Turtle()
    t4.speed = 100
    t4.penup()
    t4.goto(-50, 0)
    t4.pendown()
    t4.write('YOU WIN', font=('Arial', 16, 'bold'))
    t4.hideturtle()

goal.hideturtle()
player.hideturtle()
enemy1.hideturtle()
enemy2.hideturtle()
enemy3.hideturtle()
t2.hideturtle()


