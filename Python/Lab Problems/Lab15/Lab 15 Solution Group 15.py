states = {}
import math, csv

inputfile = 'Lab15-states2020Census.csv'
total_seats = 0
#'state_name':[population, priority, seats]
with open(inputfile, 'r') as csvfile:
    states_reader = csv.reader(csvfile) # comma is default
    for state in list(states_reader)[1:]:
        states[state[0]] = [int(state[1]), float(state[1]) / math.sqrt(2), 1]
        total_seats += 1


rs = 435 - total_seats

for i in range(rs):
    highest_state_name = ""
    highest_state_priority = 0
    
    for state in states:
        if states[state][1] > highest_state_priority:
            highest_state_priority = states[state][1]
            highest_state_name = state
    states[highest_state_name] = [states[highest_state_name][0], states[highest_state_name][0] / math.sqrt((states[highest_state_name][2] + 1) * (states[highest_state_name][2] + 2)), states[highest_state_name][2] + 1]

for state in states:
    print('{}: {}\n'.format(state, states[state]))
    
    
with open('output.txt', 'w') as file:
    file.write('{:15}  {:<2}\n'.format('STATE', 'SEATS'))
    for state in states:
        file.write('{:15}: {:<2}\n'.format(state, states[state][2]))
        
with open('oput.csv', 'w') as csvfile:
    states_writer = csv.writer(csvfile)
    states_writer.writerow(['STATE','SEATS'])
    for state in states:
        states_writer.writerow([state, states[state][2]])
        
        
    
    