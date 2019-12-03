import linecache

FILE_DIR = 'day_3/data/wires.txt'

# Class for Day 3
class Day3:
    def part_1(self):
        # First wire
        wire1 = linecache.getline(FILE_DIR, 1).split(',')
        # Second wire
        wire2 = linecache.getline(FILE_DIR, 2).split(',')



        # Follow the wire instructions for wire 1
        coords1_list = day_3.follow_wire(wire1)

        # Follow the wire instructions for wire 2
        coords2_list = day_3.follow_wire(wire2)

        # Find the intersections
        i_coords_list = day_3.find_intersections(coords1_list, coords2_list)

        # Find the distances
        distances = day_3.find_distances(i_coords_list)

        # Find the shortest distance
        distance = day_3.find_shortest_distance(distances)

        # Find the taxicab distance
        return distance

    def follow_wire(self, wire):
        # Start the wire at the origin
        coords_list = [[0, 0]]

        # Find the coordinates of every move from the instructions
        for num, instruction in enumerate(wire):
            coords_list.append(self.do_instructions(instruction, coords_list[num][0], coords_list[num][1]))
        # Return the list of coordinates of the wire
        return coords_list

    # Do what the txt file says to form the wire
    def do_instructions(self, instruction, x, y):
        coords = []
        for i in range(int(instruction[1:])):
            # Move Right
            if instruction[0] == 'R':
                x += int(instruction[1:])
            # Move Left
            elif instruction[0] == 'L':
                x -= int(instruction[1:])
            # Move Up
            elif instruction[0] == 'U':
                y += int(instruction[1:])
            # Move Down
            else:
                y -= int(instruction[1:])
            # Return the end coordinates
            coords.append([x, y])
        return coords
    
    # Find all the intersections of the wires
    def find_intersections(self, coords1_list, coords2_list):
        # List of intersection points
        i_coords_list = []
        # Cycle through all the coordinates of the wires
        for i in range(len(coords1_list)):
            if coords1_list[i] in coords2_list:
                i_coords_list.append(coords1_list[i])
        # Return all the intersections except the origin itself
        return i_coords_list[1:]

    # Find the taxicab distances of every intersection
    def find_distances(self, i_coords_list):
        # List of distances
        distances = []
        # Find the taxicab distances to the origin
        for coords in i_coords_list:
            distances.append(abs(i_coords_list[0]) + abs(i_coords_list[1]))
        # Return the list of distances from the origin
        return distances
    
    # Find the shortest distance in the list of intersections
    def find_shortest_distance(self, distances):
        # Sort from lowest to highest
        distances.sort()
        # Return the shortest distance
        return distances[0]

day_3 = Day3()
print(day_3.part_1())