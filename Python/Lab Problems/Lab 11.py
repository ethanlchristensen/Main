import turtle
import random

sc = turtle.Screen()
tr = turtle.Turtle()
tr.ht()

spots = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
player = 'X'
moves = 1

def process_mouse(x, y): # TOP ROW
    global moves
    if -150 < x < -50 and 50 < y < 150:
        if spots[0] == '-':
            tr.penup()
            tr.goto(-115, 75)
            tr.pendown()
            spots[0] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
    elif -50 < x < 50 and 50 < y < 150:
        if spots[1] == '-':
            tr.penup()
            tr.goto(-15, 75)
            tr.pendown()
            spots[1] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
    elif 50 < x < 150 and 50 < y < 150:
        if spots[2] == '-':
            tr.penup()
            tr.goto(85, 75)
            tr.pendown()
            spots[2] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
    elif -150 < x < -50 and -50 < y < 50: # MIDDLE ROW
        if spots[3] == '-':
            tr.penup()
            tr.goto(-115, -25)
            tr.pendown()
            spots[3] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
    elif -50 < x < 50 and -50 < y < 50:
        if spots[4] == '-':
            tr.penup()
            tr.goto(-15, -25)
            tr.pendown()
            spots[4] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
    elif 50 < x < 150 and -50 < y < 50:
        if spots[5] == '-':
            tr.penup()
            tr.goto(85, -25)
            tr.pendown()
            spots[5] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
    elif -150 < x < -50 and -150 < y < -50: # BOTTOM ROW
        if spots[6] == '-':
            tr.penup()
            tr.goto(-115, -125)
            tr.pendown()
            spots[6] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
    elif -50 < x < 50 and -150 < y < -50:
        if spots[7] == '-':
            tr.penup()
            tr.goto(-15, -125)
            tr.pendown()
            spots[7] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
    elif 50 < x < 150 and -150 < y < -50:
        if spots[8] == '-':
            tr.penup()
            tr.goto(85, -125)
            tr.pendown()
            spots[8] = player
            tr.write(player, font=("Arial", 32))
            switch_player()
            moves += 1
            
            
def fill_board():
    global spots
    for i in range(len(spots)):
        if spots[i] == '-':
            spots[i] = '#'
            
def switch_player():
    global player
    global spots
    global moves
    
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    
    if spots[0] == spots[1] == spots[2] != '-': # TOP ROW
        tr.penup()
        tr.goto(0, -300)
        tr.pendown()
        tr.write(spots[0] + " Wins!", font=("Arial", 32))
        fill_board()
    elif spots[3] == spots[4] == spots[5] != '-': # MIDDLE ROW
        tr.penup()
        tr.goto(0, -300)
        tr.pendown()
        tr.write(spots[3] + " Wins!", font=("Arial", 32))
        fill_board()
    elif spots[6] == spots[7] == spots[8] != '-': # BOTTOM ROW
        tr.penup()
        tr.goto(0, -300)
        tr.pendown()
        tr.write(spots[6] + " Wins!", font=("Arial", 32))
        fill_board()
    elif spots[0] == spots[3] == spots[6] != '-': # LEFT COL
        tr.penup()
        tr.goto(0, -300)
        tr.pendown()
        tr.write(spots[0] + " Wins!", font=("Arial", 32))
        fill_board()
    elif spots[1] == spots[4] == spots[7] != '-': # MIDDLE COL
        tr.penup()
        tr.goto(0, -300)
        tr.pendown()
        tr.write(spots[1] + " Wins!", font=("Arial", 32))
        fill_board()
    elif spots[2] == spots[5] == spots[8] != '-': # RIGHT COL
        tr.penup()
        tr.goto(0, -300)
        tr.pendown()
        tr.write(spots[2] + " Wins!", font=("Arial", 32))
        fill_board()
    elif spots[0] == spots[4] == spots[8] != '-': # DIAG
        tr.penup()
        tr.goto(0, -300)
        tr.pendown()
        tr.write(spots[0] + " Wins!", font=("Arial", 32))
        fill_board()
    elif spots[2] == spots[4] == spots[6] != '-': # DIAG
        tr.penup()
        tr.goto(0, -300)
        tr.pendown()
        tr.write(spots[2] + " Wins!", font=("Arial", 32))
        fill_board()
    else:
        if moves == 9:
            tr.penup()
            tr.goto(0, -300)
            tr.pendown()
            tr.write("Tie Game", font=("Arial", 32))
    
            
def draw_grid():
    draw_line(-150, 50, 150, 50)
    draw_line(-150, -50, 150, -50)
    draw_line(-50, 150, -50, -150)
    draw_line(50, 150, 50, -150)
    

def draw_line(x1, y1, x2, y2):
    tr.penup()
    tr.goto(x1, y1)
    tr.pendown()
    tr.goto(x2, y2)
    
 
tr.speed(15)
draw_grid()
sc.onclick(process_mouse)
sc.mainloop()