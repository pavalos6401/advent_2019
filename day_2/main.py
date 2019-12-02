# Class for Day 2
class Day2:

    # Initiate the class
    def __init__(self):
        # Whether the operations are done or not
        self.done     = False
        # The list of all the codes in the data
        self.intcodes = list(map(int, open('day_2/data/intcodes.txt').readline().split(',')))

    # Part 1 of Day 2's challenge
    def part_1(self):
        # Replace the noun and verb with 12 and 2 respectively
        self.replace_noun_and_verb(12, 2)
        # Do the intcodes
        self.do_codes()
        # Return the final value of the 0th position
        return self.intcodes[0]

    # Part 2 of Day 2's challenge
    def part_2(self):
        # Goal for Part 2's challenge
        GOAL = 19690720

        # Brute force it: cycle through all the possible combinations for the noun and verb
        for i in range(100):
            for j in range(100):
                # Replace the noun and verb
                self.replace_noun_and_verb(i, j)
                # Calculate the codes
                self.do_codes()
                # If the code is the solution then return the answer
                if (self.intcodes[0] == GOAL):
                    return (100 * i + j)
                    break

    # Replace the noun and verb with the new values
    def replace_noun_and_verb(self, noun, verb):
        # Replace pos 1 with the new noun value
        self.intcodes[1] = noun
        # Replace pos 2 with the new verb value
        self.intcodes[2] = verb

    # Function to do the codes
    def do_codes(self):
        # Loop through the codes
        pos = 0
        while (pos <= (len(self.intcodes) - 1)) and (not self.done):
            if self.intcodes[pos] == 1:
                # Addition case
                self.opcode1(pos)
            else:
                if self.intcodes[pos] == 2:
                    # Multiplication case
                    self.opcode2(pos)
                else:
                    # End case
                    self.opcode99()
            # Move 4 positions forward
            pos += 4

    # Two numbers in the next two positions are added
    def opcode1(self, pos):
        self.intcodes[self.intcodes[pos + 3]] = self.intcodes[self.intcodes[pos + 1]] + self.intcodes[self.intcodes[pos + 2]]
        
    # Two numbers in the next two positions are multiplied
    def opcode2(self, pos):
        self.intcodes[self.intcodes[pos + 3]] = self.intcodes[self.intcodes[pos + 1]] * self.intcodes[self.intcodes[pos + 2]]
    
    # End the program
    def opcode99(self):
        self.done = True

# Initialize a new instance of the Day2 class
day_2 = Day2()

# Choose what part to solve
part = int(input("Part 1 or 2: "))
if part == 1:
    print("Final value of position 0: " + str(day_2.part_1())) # Part 1
else:
    print("100 * Noun + Verb: " + str(day_2.part_2()))         # Part 2