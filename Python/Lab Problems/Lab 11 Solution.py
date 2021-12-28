import turtle
import random

sc = turtle.Screen()
tr = turtle.Turtle()

who = 'X'
spots = ['-','-','-','-','-','-','-','-','-']
moves = 0

def process_mouse(x, y):
    global moves
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
    if -150 < x < -50 and 50 < y < 150: # TOP ROW
        if spots[0] == '-':
            tr.write(who, font=("Arial", 32))
            spots[0] = who
            switch_player()
            moves += 1
    elif -50 < x < 50 and 50 < y < 150:
        if spots[1] == '-':
            tr.write(who, font=("Arial", 32))
            spots[1] = who
            switch_player()
            moves += 1
    elif 50 < x < 150 and 50 < y < 150:
        if spots[2] == '-':
            tr.write(who, font=("Arial", 32))
            spots[2] = who
            switch_player()
            moves += 1
    elif -150 < x < -50 and -50 < y < 50: # MIDDLE ROW
        if spots[3] == '-':
            tr.write(who, font=("Arial", 32))
            spots[3] = who
            switch_player()
            moves += 1
    elif -50 < x < 50 and -50 < y < 50:
        if spots[4] == '-':
            tr.write(who, font=("Arial", 32))
            spots[4] = who
            switch_player()
            moves += 1
    elif 50 < x < 150 and -50 < y < 50:
        if spots[5] == '-':
            tr.write(who, font=("Arial", 32))
            spots[5] = who
            switch_player()
            moves += 1
    elif -150 < x < -50 and -150 < y < -50: # LAST ROW
        if spots[6] == '-':
            tr.write(who, font=("Arial", 32))
            spots[6] = who
            switch_player()
            moves += 1
    elif -50 < x < 50 and -150 < y < -50:
        if spots[7] == '-':
            tr.write(who, font=("Arial", 32))
            spots[7] = who
            switch_player()
            moves += 1
    elif 50 < x < 150 and -150 < y < -50:
        if spots[8] == '-':
            tr.write(who, font=("Arial", 32))
            spots[8] = who
            switch_player()
            moves += 1
    check_for_win()

def fill_board():
    global spots
    for i in range(len(spots)):
        if spots[i] == '-':
            spots[i] = '#'
            
            
def check_for_win():
    global moves
    if spots[0] == spots[1] == spots[2] != '-':# TOP ROW
        tr.penup()
        tr.goto(0, -300)
        tr.write(spots[0] + " wins!", font=("Arial", 32))
        fill_board()
    elif spots[3] == spots[4] == spots[5] != '-': # MIDDLE ROW
        tr.penup()
        tr.goto(0, -300)
        tr.write(spots[3] + " wins!", font=("Arial", 32))
        fill_board()
    elif spots[6] == spots[7] == spots[8] != '-': # BOTTOM ROW
        tr.penup()
        tr.goto(0, -300)
        tr.write(spots[6] + " wins!", font=("Arial", 32))
        fill_board()
    if spots[0] == spots[3] == spots[6] != '-': # LEFT COLOUMN
        tr.penup()
        tr.goto(0, -300)
        tr.write(spots[0] + " wins!", font=("Arial", 32))
        fill_board()
    elif spots[1] == spots[4] == spots[7] != '-': # MIDDLE COLOUMN
        tr.penup()
        tr.goto(0, -300)
        tr.write(spots[1] + " wins!", font=("Arial", 32))
        fill_board()
    elif spots[2] == spots[5] == spots[8] != '-': # RIGHT COLOUMN
        tr.penup()
        tr.goto(0, -300)
        tr.write(spots[2] + " wins!", font=("Arial", 32))
        fill_board()
    elif spots[0] == spots[4] == spots[8] != '-':
        tr.penup()
        tr.goto(0, -300)
        tr.write(spots[0] + " wins!", font=("Arial", 32))
        fill_board()
    elif spots[2] == spots[4] == spots[6] != '-':
        tr.penup()
        tr.goto(0, -300)
        tr.write(spots[2], " wins!", font=("Arial", 32))
        fill_board()
    elif moves == 9:
        tr.penup()
        tr.goto(0, -300)
        tr.write("Tie Game!", font=("Arial", 32))

def switch_player():
    global who
    if who == 'X':
        who = 'O'
    else:
        who = 'X'

def draw_grid():
    global spots
    lines = ( (-150, 50), (150, 50),
              (-150, -50), (150, -50),
              (-50, 150), (-50, -150),
              (50, 150), (50, -150))
    for i in range(0, len(lines), 2):
        tr.penup()
        tr.goto(lines[i][0], lines[i][1])
        tr.pendown()
        tr.goto(lines[i+1][0], lines[i+1][1])
    
tr.speed(15)
draw_grid()
sc.onclick(process_mouse)
sc.mainloop()