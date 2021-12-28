import csv, math

file_name = 'Lab15-states2020Census.csv'
states = {}

with open(file_name, 'r') as csvfile:
    states_reader = csv.reader(csvfile, delimiter=',')
    first_row = True
    total_states = 0
    for state in (states_reader):
        if first_row:
            first_row = False
        else:
            total_states += 1
            states[state[0]] = [int(state[1]), float(state[1]) / math.sqrt(2), 1]
        

open_seats = 435 - total_states

for i in range(open_seats):
    highest_state = ""
    highest_val = 0
    for state in states:
        # state -> key, states -> dictionary
        # states[state] -> list[1] -> priority value
        # state -> name or key value
        if states[state][1] > highest_val:
            highest_state = state
            highest_val = states[state][1]
    states[highest_state] = [states[highest_state][0], states[highest_state][0] / math.sqrt((states[highest_state][2] + 1) * (states[highest_state][2] + 2)) , states[highest_state][2] + 1]
    
with open('outputData.txt', 'w') as file:
    file.write('STATE\t\t\t\tSEATS\n')
    for state in states:
        file.write('{}:\t\t\t\t{}\n'.format(state, states[state][2]))
            
with open('outputData.csv', 'w') as csvfile:
    states_writer = csv.writer(csvfile)
    for state in states:
        states_writer.writerow([state, states[state][2]])




