#!/usr/bin/env python3

import turtle

def draw_border(Raphael, width, height,colour):
    # Draws a border around the canvas

    Raphael.pencolor(colour)
    Raphael.pensize(1)
    Raphael.penup()
    Raphael.setposition(0,0)
    Raphael.pendown()
    Raphael.goto(0,height)
    Raphael.goto(width,height)
    Raphael.goto(width,0)
    Raphael.goto(0,0)
    
def draw_lines (Raphael,lines, colour):
    # Draws several lines

    Raphael.pencolor(colour)
    for line in lines:
        start = line[0]
        end = line[1]
        Raphael.pensize(15)
        Raphael.penup()
        Raphael.setposition(start)
        Raphael.pendown()
        Raphael.goto(end)

def draw_rectangles (Raphael,rectangles, colour):
    # Draws several rectangles

    Raphael.color(colour)
    for rect in rectangles:
        Raphael.begin_fill()
        Raphael.pensize(1)
        Raphael.penup()
        Raphael.setposition(rect[0])
        Raphael.pendown()
        Raphael.goto(rect[1])
        Raphael.goto(rect[2])
        Raphael.goto(rect[3])
        Raphael.goto(rect[0])
        Raphael.end_fill()

def main():
    # Draw the composition

    horizontal_lines =[[(340,  50), (1090,   50)],
                       [(770, 290), (1090,  290)],
                       [( 10, 480), (1090,  480)],
                       [( 70, 770), (1070,  770)],
                       [( 10,1070), (1070,1070)]]

    verticle_lines = [[(  70, 480), (  70, 1190)],
                      [( 340,  10), ( 340, 1190)],
                      [( 490, 480), ( 490, 1190)],
                      [( 760,  10), ( 760, 1190)],
                      [( 800,  10), ( 800, 1190)],
                      [( 850,  50), ( 850, 1190)],
                      [( 950,  10), ( 950, 1190)],
                      [(1070, 480), (1070, 1190)]]

    red_rectangles = [[(  0,1200), (  70, 1200), (  70, 930), (  0,930)],
                      [(  0, 550), (  70,  550), (  70, 480), (  0,480)],
                      [(950, 640), (1070,  640), (1070, 560), (950,560)]]

    blue_rectangles = [[(340,1200), ( 490, 1200), ( 490,1070), (340,1070)],
                       [(950,  50), (1100,   50), (1100,   0), (950,   0)]]

    yellow_rectangles = [[(340, 770),(480, 770),(480, 480),(340, 480)]]

    turtle.screensize(1100,1200,"ivory2")
    turtle.setworldcoordinates(0,0,1100,1200)
    turtle.title("Composition in Red, Blue and Yellow: by Piet Mondrian (Dutch: 1872..1944)")
    
    Raphael = turtle.Turtle()
    Raphael.shape("turtle")

    draw_border(Raphael,1100,1200,"grey")
    draw_rectangles (Raphael,red_rectangles, "red")
    draw_rectangles (Raphael,blue_rectangles, "blue")
    draw_rectangles (Raphael,yellow_rectangles, "yellow")

    draw_lines (Raphael,horizontal_lines, "black")
    draw_lines (Raphael,verticle_lines, "black")

    Raphael.hideturtle()

    turtle.exitonclick()

main()