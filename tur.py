import turtle 

wn = turtle.Screen() # Make a window
wn.setup(width = 800,height =800) #choose it size
wn.bgcolor("black") # choose it bakcground color
wn.tracer(1) # update the screen automatically
wn.title("Pong") # choose the name of the window

#Making the players

paddle_a = turtle.Turtle() # Make a turtle object that will hold the first player
paddle_a.shape("square") # Choose the shape of the object
paddle_a.color("white") # choose the color of the object
paddle_a.speed(0) # the speed at which the object is drawn
paddle_a.penup() # do not draw line with the shape
paddle_a.goto(-360,0)# set the object in window(it position )
paddle_a.shapesize(stretch_wid=5,stretch_len=1)# Choose the size of the shape 

#Player 2

paddle_b = turtle.Turtle() # Make a turtle object that will hold the first player
paddle_b.shape("circle") # Choose the shape of the object
paddle_b.color("white") # choose the color of the object
paddle_b.speed(0) # the speed at which the object is drawn
paddle_b.penup() # do not draw line with the shape
paddle_b.goto(360,0)# set the object in window(it position )
paddle_b.shapesize(stretch_wid=5,stretch_len=1)# Choose the size of the shape 

#Make the ball

ball = turtle.Turtle() # Make a turtle object that will hold the first player
ball.shape("triangle") # Choose the shape of the object
ball.color("white") # choose the color of the object
ball.speed(0) # the speed at which the object is drawn
ball.penup() # do not draw line with the shape
ball.goto(0,0)# set the object in window(it position )
ball.dx = 9 # Speed of the ball in the x axis
ball.dy = 2 # Speed of the ball in the y axis

def paddle_a_up():
    y = paddle_a.ycor() #Extract the coordinate of the paddle_a in the y axis
    y+= 20
    paddle_a.sety(y) # Set the new coordinate of the paddle_a in the y axis
def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)
def paddle_b_up():
    y =paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)
def paddle_b_down():
    y =paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)

wn.listen() #Set up an event for "wn" window to respond to the user input
wn.onkeypress(paddle_a_up,"w") #when the "w" key is pressed launch the paddle_a_up function
wn.onkeypress(paddle_a_down,"s") 
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down") 


while(1):
    wn.update()
    #Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Collision with borders management
    if(ball.ycor()> 290):
        ball.sety(290) # Set the new position for the ball in yaxis
        ball.dy *=-1 #Move to the opposite side in the y axis
    if(ball.ycor()< -290):
        ball.sety(-290)
        ball.dy *= -1
    if(ball.xcor() >390):
        ball.goto(0,0)#Set the initial position for the ball when it pass paddle_b
        ball.dx *= -1
    if(ball.xcor()< -390): #same but for paddle_a
        ball.goto(0,0)
        ball.dx *= -1
    #COllision with the paddle
    #if the ball has reached paddle_b then it go to the opposite direction
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ) :
        ball.setx(340) # Set the ball in a position in the x axis
        ball.dx *= -1
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ) :
        ball.setx(-340)
        ball.dx *= -1