# Class for Day 1
class Day1():
    # Part 1
    def part_1(self):
        # Total fuel necessary
        total_fuel = 0
        # The file containing all the masses
        file_object = open('day_1/data/masses.txt')
        # The data from the file
        file_data = file_object.readlines()
        # Check each line
        for line in file_data:
            # The fuel formula, the total fuel is adding all the fuels
            total_fuel += (float(line) // 3) - 2
        # Return the fuel needed
        return total_fuel

    # Part 2
    def part_2(self):
        # Total fuel necessary
        total_fuel   = 0
        # Fuel needed for a mass
        mass_fuel    = 0
        # The fuel needed for the fuel of each mass
        current_fuel = 0
        # The file containing all the masses
        file_object = open('day_1/data/masses.txt')
        # The data from the file
        file_data = file_object.readlines()
        # Check each line
        for line in file_data:
            # The fuel for the mass
            mass_fuel    = (float(line) // 3) - 2
            # The total fuel includes the above fuel
            total_fuel += mass_fuel
            # Save the fuel needed for the mass as the current fuel mass
            current_fuel = mass_fuel
            # Keep finding the fuel needed for the fuel until the fuel needed is negligible
            while (float(current_fuel) // 3) - 2 > 0:
                current_fuel = ((float(current_fuel) // 3) - 2)
                # The total fuel includes the fuel needed for the fuel
                total_fuel += current_fuel
        # Return the total fuel needed
        return total_fuel

# Fuel needed
fuel = 0
# Create an instance of the Day1 class
day_1 = Day1()
# Ask the user what part of day 1 should be solved
part = int(input('Part 1 or 2: '))
if part == 1:
    fuel = day_1.part_1()
else:
    if part == 2:
        fuel = day_1.part_2()
# Print the total fuel needed
print(fuel)