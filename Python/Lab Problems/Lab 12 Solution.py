import random
fruits = ['APPLE', 'PEAR', 'ORANGE', 'BANANA', 'KIWI', 'PINEAPPLE']
states = ['NEBRASKA', 'KANSAS', 'IOWA', 'CALIFORNIA', 'TEXAS', 'FLORIDA', 'NEW HAMPSHIRE']
categories = ['Fruits', 'States']
wheel = [50, 50, 50, 50, 100, 100, 100, 100, 200, 200, 300, 300, 400, 400, 500, 500, 600, 700, 800, 900]

vowels = 'AEIOU'
rounds = 2

def generate_puzzle():
    cat = random.randint(0, len(categories) - 1)
    puzzle = ''
    blank = ''
    if cat == 0:
        puzzle = fruits[random.randint(0, len(fruits) - 1)]
    elif cat == 1:
        puzzle = states[random.randint(0, len(states) - 1)]
    for i in range(len(puzzle)):
        if puzzle[i] == ' ':
            blank += ' '
        else:
            blank += '-'
    return blank, puzzle, categories[cat]

def spin_wheel():
    return wheel[random.randint(0, len(wheel) - 1)]

def get_num_players():
    num_players = input('Enter the number of players (1-3): ')
    while num_players.isdigit() == False or (num_players < '1' or num_players > '3'):
        num_players = num_players = input('Enter the number of players (1-3): ')
    num_players = int(num_players)
    return num_players

def guess_letter(unsolved, solved_puzzle, point_value, player_points, guessed):
    letter = input("Enter the letter to guess (vowels cost 250): ").strip().upper()
    while not letter.isalpha() or len(letter) > 1 or (letter in vowels and player_points < 250) or has_guessed(letter, guessed):
        if letter in vowels and player_points < 250:
            print("Not enough points to buy a vowel.")
        elif has_guessed(letter, guessed):
            print(f"{letter} has already been guessed.")
        else:
            print("Incorrect value entered.")
        letter = input("Enter the letter to guess (vowels cost 250): ").strip().upper()
    guessed += letter
    num_letters = 0
    if letter in solved_puzzle:
        num_letters = solved_puzzle.count(letter)
        pos = -1
        for times in range(num_letters):
            pos = solved_puzzle.find(letter, pos+1)
            unsolved = unsolved[:pos] + letter + unsolved[pos+1:]
    
    if num_letters > 0 and letter not in vowels:
        player_points += (point_value * num_letters)
    elif num_letters > 0 and letter in vowles:
        player_points -= 250
    
    return unsolved, player_points, guessed, num_letters > 0

def has_guessed(letter, guessed):
    return letter in guessed


if __name__ == '__main__':
    num_players = get_num_players()
    players = []
    round_scores = []
    for i in range(num_players):
        players.append(0)
        round_scores.append(0)
    print(players)
    round = 1
    player = 0
    while round <= rounds:
        solved = False
        for i in range(num_players):
            round_scores[i] = 0
        guessed = ''
        unsolved, solved_puzzle, category = generate_puzzle()
        while not solved:
            print('\n\n|{}|\n|{}|\n'.format(unsolved, category))
            print('Player {}\'s turn.'.format(player + 1))
            print('Player {} score: {}'.format(player + 1, round_scores[player]))
            
            value = spin_wheel()
            print('The wheel landed on {}'.format(value))
            unsolved, round_scores[player], guessed, correct = guess_letter(unsolved, solved_puzzle, value, round_scores[player], guessed)
            
            if correct:
                print('Player {} guessed correctly!'.format(player+1))
            else:
                print('Player {} guessed incorrectly!'.format(player+1))
                player += 1
                player %= num_players
                print('Now it is Player {} turn!'.format(player + 1))
            if unsolved == solved_puzzle:
                solved = True
                print('Player {} solved the puzzle!'.format(player + 1))
                player += 1
                player %= num_players
                print('\nTotal scores after Round {}: '.format(round))
                for i in range(num_players):
                    players[i] += round_Scores[i]
                    print('Player {}: {}'.format(i+1, player[i]))
                if round < rounds:
                    print('Player {} will start next round!'.format(player + 1))
        round += 1
        
    print('Game over!\nFinal Scores')
    for i in range(num_players):
        print('Player {}: {}'.format(i+1, player[i]))
