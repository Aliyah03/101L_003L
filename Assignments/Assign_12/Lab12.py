import turtle

class Point(object):

    def __init__(self, x, y, color):
        self.x=x
        self.y=y
        self.color=color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

p = Point(-100, 100, "blue")
p.draw()

class Box(Point):

    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color) #calling point
        #self.x=x, already assigned in Point
        #self.y=y, already assigned in Point
        self.width=width
        self.height=height
        #self.color=color, already assigned in Point

    def draw_action(self):
        turtle.color(self.color)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.up()
        
#d = Box(-100, 100, 150, 150, "blue")
#d.draw_action()

class Boxfilled(Box):

    def __init__(self, x, y, width, height, color, fill):
        Box.__init__(self, x, y, width, height, color) #calling box
        #self.x=x, already assigned in Point
        #self.y=y, already assigned in Point
        #self.width=width, already assigned in Box
        #self.height=height, already assigned in Box
        #self.color=color, already assigned in Point
        self.fill=fill

    def draw_action(self):
        turtle.pendown()
        turtle.fillcolor(self.fill)
        turtle.begin_fill()
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.end_fill()
        turtle.penup()

bf = Boxfilled(-100, 100, 150, 150, "blue", "gold")
bf.draw_action()

#---------------------------------------------------------------------------------------
# Call Point to draw Circle
p = Point(-250, -40, "purple")
p.draw()
turtle.pendown()

class Circle(Point):

    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color) #calling point
        #self.x=x, already assigned in Point
        #self.y=y, already assigned in Point
        self.radius=radius
        #self.color=color, already assigned in Point

    def draw_action(self):
        turtle.pendown()
        turtle.circle(self.radius)

#c = Circle(-250, -40, 75, "purple")
#c.draw_action()

class Circlefilled(Circle):

    def __init__(self, x, y, radius, color, filled):
        Circle.__init__(self, x, y, radius, color) #calling circle
        #self.x=x, already assigned in Point
        #self.y=y, already assigned in Point
        #self.radius=radius, already assigned in Circle
        #self.color=color, already assigned in Point
        self.filled=filled
    
    def draw_action(self):
        turtle.pendown()
        turtle.fillcolor(self.filled)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
    
cf = Circlefilled(-250, -40, 75, "purple", "pink")
cf.draw_action()
turtle.done()