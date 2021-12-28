# Calculation  V / sqrt(s * (s + 1))
# where V is population and s is the number of seats
# the state has so far

states = {}

import csv, math

inputfile = 'Lab15-states2020census.csv'

with open(inputfile, 'r') as csvfile:
    states_reader = csv.reader(csvfile, delimiter=',')
    row_num = 0
    for row in states_reader:
        if row_num > 0:
            print('Row #{}:'.format(row_num), row) # here row is an array containing two stirngs, the state name and population
            # in our state dictionary, we are going to have a key of
            # row[0] -> state name, which will have an
            # int(row[1]) - > pop
            # float(row[1]) / math.sqrt(2) -> priority
            # 1 -> the seat every state gets
            states[row[0]] = [int(row[1]), float(row[1]) / math.sqrt(2), 1]
            row_num += 1
        else:
            row_num += 1
available_seats = 435 - row_num - 1
print('Available Seats: {}\n\n'.format(available_seats))

for state in states:
    print('{}: {}, {}, {}'.format(state, states[state][0], states[state][1], states[state][2]))

while available_seats > 0:
    highest = '' # state with highest priority
    highest_val = 0 # the priority value of the state
    for state in states: # for each seat, we will loop through the states to find who gets the next seat . . .
        if highest_val < states[state][1]: # if the priority at the state is higher than the current highest then we need to switch this
            highest = state
            highest_val = states[state][1]
        states[highest] = [states[highest][0], (states[highest][0] / math.sqrt((states[highest][2] + 1) * (states[highest][2] + 2))), states[highest][2] + 1] # update that state to have same pop, updated priority, and add one to the seat
        available_seats -= 1
for state in states:
    print(f"{state}: {states[state][0]}, {states[state][1]}, {states[state][2]}")


# Writing to txt and csv files using with as file. . .
with open('stateHouseResults.txt', 'w') as file:
    for state in states:
        file.write(f"{state}: {states[state][0]}, {states[state][1]}, {states[state][2]}\n")
with open('stateHouseResults.csv', 'w') as file:
    state_writer = csv.writer(file)
    for state in states:
        state_writer.writerow([state, states[state][2]])