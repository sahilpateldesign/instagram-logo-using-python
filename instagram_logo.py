from turtle import *

bgcolor('black')
pencolor('#e95950')
width(23)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
 forward(250)
 circle(34,90)

penup()
goto(85,30)
pendown()
circle(80,360)
penup()
goto(110,130)
pendown()
circle(7,360)

width(5)
penup()
color('#fbad50')
goto(-140,-200)
pendown()
write("@sahilpatel3338",move=True,font=("Calibri",30,"bold"))
hideturtle()

done()