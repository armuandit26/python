#Andri 11.11.26

#rõngad
import turtle

aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Andri - olümpiarõngad")
##liigutan oigesse kohta
turtle.speed (0)
turtle.up()
turtle.goto(-150,50)
turtle.down()
##ring 1
turtle.pensize(6)
turtle.pencolor("blue")
turtle.circle(50)

turtle.up()
turtle.goto(-40,50)
turtle.down()

##ring 2
turtle.pensize(6)
turtle.pencolor("black")
turtle.circle(50)





turtle.done()

