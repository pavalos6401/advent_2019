# File directory for the data
FILE_DIR = 'day_3/data/wires.txt'

# Get the information for each wire
with open(FILE_DIR) as _file:
    (wire1, wire2) = _file.read().splitlines()

# Split the wire information from a string into a list
wire1 = wire1.split(',')
wire2 = wire2.split(',')

# All the relevant information for wire 1
wire1_info = {
    'h_lines': [],
    'v_lines': [],
    'steps': 0,
    'last_steps': 0,
    'pos': [0, 0],
    'last_pos': [0, 0]
}

# All the relevant information for wire 2
wire2_info = {
    'h_lines': [],
    'v_lines': [],
    'steps': 0,
    'last_steps': 0,
    'pos': [0, 0],
    'last_pos': [0, 0]
}

# A list of all the intersections
intersections = []

# Steps required to get to the intersections
steps = []

# Get the instructions from the wire
def get_instructions(wire):
    # Direction it moves
    direction = wire[0]
    # Distance it moves
    amount = int(wire[1:])
    # List of the instructions
    return [direction, amount]

instructions1 = []
instructions2 = []

# Get the instructions for wire 1 and 2
for elem in wire1:
    instructions1.append(get_instructions(elem))
for elem in wire2:
    instructions2.append(get_instructions(elem))

# Follow the wire with the info and instructions of it
def move(wire_info, instruction):
    # Direction it moves
    direction = instruction[0]
    # Distance it moves
    amount = instruction[1]
    # Original coordinates
    origin = wire_info['pos']

    # Move Right
    if direction == 'R':
        end = [wire_info['pos'][0] + amount, wire_info['pos'][1]]
        new_line = [origin, end]
        wire_info['h_lines'].append(new_line)
    # Move Left
    elif direction == 'L':
        end = [wire_info['pos'][0] - amount, wire_info['pos'][1]]
        new_line = [origin, end]
        wire_info['h_lines'].append(new_line)
    # Move Up
    elif direction == 'U':
        end = [wire_info['pos'][0], wire_info['pos'][1] + amount]
        new_line = [origin, end]
        wire_info['v_lines'].append(new_line)
    # Move Down
    else:
        end = [wire_info['pos'][0], wire_info['pos'][1] - amount]
        new_line = [origin, end]
        wire_info['v_lines'].append(new_line)
    
    # Update the end point of the wire
    wire_info['pos'] = end
    # Update the last known position of the wire
    wire_info['last_pos'] = origin

# Make every move for the wires
for instruction in instructions1:
    move(wire1_info, instruction)
for instruction in instructions2:
    move(wire2_info, instruction)

# Cycle throught the horizontal lines of one wire
# to check with the vertical lines of the other wire
for h_line in wire1_info['h_lines']:
    for v_line in wire2_info['v_lines']:
        # If the y value of the horizontal line is betweent the vertical line's y values
        # and the vertical line's x is between horizontal line's x values
        if ((h_line[0][1] <= max(v_line[0][1], v_line[1][1]) and
        h_line[0][1] >= min(v_line[0][1], v_line[1][1])) and
        (v_line[0][0] <= max(h_line[0][0], h_line[1][0]) and
        v_line[0][0] >= min(h_line[0][0], h_line[1][0]))):
            if (v_line[0][0] != 0 and h_line[0][1] != 0):
                # Add the intersection to the list
                intersections.append([v_line[0][0], h_line[0][1]])

# Invert the wires checked
for h_line in wire2_info['h_lines']:
    for v_line in wire1_info['v_lines']:
        # If the y value of the horizontal line is betweent the vertical line's y values
        # and the vertical line's x is between horizontal line's x values
        if ((h_line[0][1] <= max(v_line[0][1], v_line[1][1]) and
        h_line[0][1] >= min(v_line[0][1], v_line[1][1])) and
        (v_line[0][0] <= max(h_line[0][0], h_line[1][0]) and
        v_line[0][0] >= min(h_line[0][0], h_line[1][0]))):
            # If it is also not the origin
            if (v_line[0][0] != 0 and h_line[0][1] != 0):
                # Add the intersection to the list
                intersections.append([v_line[0][0], h_line[0][1]])

# List of distances
distances = []

# Find the taxicab distance
def find_distance(coords):
    # Return the list of distance from the origin
    return abs(coords[0]) + abs(coords[1])

# Cycle through the intersections
for intersection in intersections:
    distances.append(find_distance(intersection))

# Sort the distances from lowest to highest
distances.sort()

# Return the shortest distance
print(f"Answer to part 1: {distances[0]}")

# Restart for part 2

wire1_info = {
    'h_lines': [],
    'v_lines': [],
    'steps': 0,
    'last_steps': 0,
    'pos': [0, 0],
    'last_pos': [0, 0]
}

wire2_info = {
    'h_lines': [],
    'v_lines': [],
    'steps': 0,
    'last_steps': 0,
    'pos': [0, 0],
    'last_pos': [0, 0]
}

def check_intersections(wire_info):
    pos = wire_info['pos']
    last_pos = wire_info['last_pos']

    # If the last move made a vertical line
    if (pos[0] == last_pos[0]):
        x = pos[0]
        y_start = min(pos[1], last_pos[1])
        y_end = max(pos[1], last_pos[1])

        for sect in intersections:
            # Check if we intersect the intersection
            if (sect[0] == x and (sect[1] >= y_start and sect[1] <= y_end)):
                # Find the distance
                steps_to_intersection = abs(sect[1] - last_pos[1])
                # Check if the dictionary of intersections with the amounts/distances has these steps
                if (f"{sect[0]}|{sect[1]}" not in intersections_with_amount):
                    # If it is a new intersection, add it
                    intersections_with_amount[f"{sect[0]}|{sect[1]}"] = {'sect': sect, 'amount': wire_info['steps'] + steps_to_intersection}
                else:
                    # if it does, add the new amount of steps to the old rec's stepcount
                    intersections_with_amount[f"{sect[0]}|{sect[1]}"]['amount'] += wire_info['steps'] + steps_to_intersection
    # If the last move made horizontal line
    if (pos[1] == last_pos[1]):
        y = pos[1]
        x_start = min(pos[0], last_pos[0])
        x_end = max(pos[0], last_pos[0])

        for sect in intersections:
            # Check if we intersect the intersection
            if (sect[1] == y and (sect[0] >= x_start and sect[0] <= x_end)):
                # Find the distance
                steps_to_intersection = abs(sect[0] - last_pos[0])
                # Check if the dictionary of intersections with the amounts/distances has these steps
                if (f"{sect[0]}|{sect[1]}" not in intersections_with_amount):
                    # If it is a new intersection, add it
                    intersections_with_amount[f"{sect[0]}|{sect[1]}"] = {'sect': sect, 'amount': wire_info['steps'] + steps_to_intersection}
                else:
                    # if it does, add the new amount of steps to the old rec's stepcount
                    intersections_with_amount[f"{sect[0]}|{sect[1]}"]['amount'] += wire_info['steps'] + steps_to_intersection

intersections_with_amount = {}

# Cycle through instructions
for instruction in instructions1:
    move(wire1_info, instruction)
    check_intersections(wire1_info)
    wire1_info['steps'] += wire1_info['last_steps']
for instruction in instructions2:
    move(wire2_info, instruction)
    check_intersections(wire2_info)
    wire2_info['steps'] += wire2_info['last_steps']

# All the amounts of steps
amounts = []

# Add the amounts to the list
for key in intersections_with_amount:
    amounts.append(intersections_with_amount[key]['amount'])

# Sort the amounts from lowest to highest
amounts.sort()

# Answer is the lowest
print(f"Answer to part 2: {amounts[0]}")