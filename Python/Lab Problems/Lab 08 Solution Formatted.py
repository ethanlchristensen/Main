import random

# This program simulates the game Bunco
# 1 player, Three Dice, Six Rounds
# Round = rolling three dice, continue rolloing while points are earned
# If points aren't earned, then new round.

total = 0

for i in range(1,7):
    round_points = 0
    roll = 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    print('===========================')
    print('=\t  ROUND {}\t  ='.format(i))
    print('===========================')
    print('|\t  ROll {}\t  |'.format(roll))
    roll += 1
    print('|\t  D-ONE:{}\t  |\n|\t  D-TWO:{}\t  |\n|\t  D-THR:{}\t  |'.format(dice1, dice2, dice3))
    
    if dice1 == dice2 and dice2 == dice3 and dice1 == i:
        print('|          BUNCO\t  |')
        round_points += 21
    elif dice1 == dice2 and dice2 == dice3:
        print('|        MINI BUNCO\t  |')
        round_points += 5
    else:
        if dice1 == i:
            round_points += 1
        if dice2 == i:
            round_points += 1
        if dice3 == i:
            round_points += 1
    print('|      ROLL POINTS:{}\t  |\n|\t\t\t  |'.format(round_points))
    if round_points != 0  and round_points != 21:
        croll = round_points
        while  croll > 0 and croll < 21:
            croll = 0
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dice3 = random.randint(1,6)
            print('|\t  ROll {}\t  |'.format(roll))
            roll += 1
            print('|\t  D-ONE:{}\t  |\n|\t  D-TWO:{}\t  |\n|\t  D-THR:{}\t  |'.format(dice1, dice2, dice3))
            if dice1 == dice2 and dice2 == dice3 and dice1 == i:
                print('|          BUNCO\t  |')
                croll += 21
            elif dice1 == dice2 and dice2 == dice3:
                print('|        MINI BUNCO\t  |')
                croll += 5
            else:
                if dice1 == i:
                    croll += 1
                if dice2 == i:
                    croll += 1
                if dice3 == i:
                    croll += 1
            round_points += croll
            print('|       ROLL POINTS:{}\t  |\n|\t\t\t  |'.format(croll))
        print('|      ROUND POINTS:{}\t  |'.format(round_points))
        print('|      ROUND {} OVER\t  |'.format(i))
        print('===========================\n')
        total += round_points
    else:
        print('|      ROUND POINTS:{}\t  |'.format(round_points))
        print('|      ROUND {} OVER\t  |'.format(i))
        print('===========================\n')
        total += round_points

print('===========================')
print('|     TOTAL POINTS: {}\t  |'.format(total))
print('|\tGAME OVER\t  |')
print('===========================')