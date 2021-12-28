# BUNCO program
# 6 rounds
# Each roudn we role till we get to 21 points or till a roll produces 0 points
# If all dice are equal and they equal the round number then +21 points
# If all dice are equal and they don't equal round number then +5 points
# Else for every dice that matches the round number +1 points

# EXAMPLE RUN

# ROUND -> 1
# DICE ONE: 1 DICE TWO: 1 DICE THREE: 1 -> +21 points -> ROUND OVER

# ROUND -> 2
# DICE ONE: 1 DICE TWO: 1 DICE THREE: 1 -> +5 points -> ROLL AGAIN IF TOTAL < 21

# ROUND -> 3
# DICE ONE: 3 DICE TWO: 1 DICE THREE: 3 -> +2 points -> ROLL AGAIN IF TOTAL < 21

# ROUND -> 4
# DICE ONE: 2 DICE TWO: 6 DICE THREE: 5 -> +0 points -> ROUND OVER

# ROUND -> 5
# DICE ONE: 2 DICE TWO: 6 DICE THREE: 5 -> +1 points -> ROLL AGAIN IF TOTAL < 21

# ROUND -> 6
# DICE ONE: 2 DICE TWO: 6 DICE THREE: 5 -> +1 points -> ROLL AGAIN IF TOTAL < 21

# TOTAL POINTS -> 21 + (5 + ... + n) + (2 + ... + n) + 0 + (1 + ... + n) + (1 + ... + n)

# END OF PROGRAM
import random

total = 0

for round in range(1,7):
    round_points = 0
    
    
#========FIRST ROLL====================================================================================
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    
    if dice1 == dice2 and dice2 == dice3 and dice1 == round:
        round_points += 21
    elif dice1 == dice2 and dice2 == dice3:
        round_points += 5
    else:
        if dice1 == round:
            round_points += 1
        if dice2 == round:
            round_points += 1
        if dice3 == round:
            round_points += 1


#=============EVERY OTHER ROLL IF THE FIRST ROLE WAS GREATER THAN ZERO AND LESS THAN 21================= 
    while round_points > 0 and round_points < 21: # Keep Rolling until we roll zero points, or our round points are greater than 21
        
        previous_points = round_points
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        if dice1 == dice2 and dice2 == dice3 and dice1 == round:
            round_points += 21
        elif dice1 == dice2 and dice2 == dice3:
            round_points += 5
        else:
            if dice1 == round:
                round_points += 1
            if dice2 == round:
                round_points += 1
            if dice3 == round:
                round_points += 1
#====CHECKING TO SEE IF OUR CURRENT ROLL PRODUCED ZERO, ZERO == END OF ROUND=============================
        if previous_points == round_points:
            break
#=====IF WE DON'T BREAK WE LOOP BAKC UP TO THE WHILE LOOP FOR A NEW DICE ROLL============================
#+====IF WE DID BREAK, WE ARE DONE WITH WHILE LOOP AND ROUND IS OVER=====================================
            
    total += round_points
    print('ROUND NUMBER: {}\nPOINTS EARNED: {}'.format(round, round_points))
    print()
        
print('TOTAL POINTS EARNED: {}'.format(total))
