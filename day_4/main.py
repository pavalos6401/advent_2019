# Directory of the data file
FILE_DIR = 'day_4/data/range.txt'

# Minimum and Maximum
GIVEN_RANGE = list(map(int, open(FILE_DIR).readline().split('-')))

class PasswordCracker():
    def __init__(self):
        # Min and Max constraints
        self.min = GIVEN_RANGE[0]
        self.max = GIVEN_RANGE[1]
        # Size constraint of password
        self.size = 6
        # Whether or not the 'twin' requirement is met
        self.twin = False
        # Whether or not the ascending requirement is met
        self.ascending = False
        # List of possible passwords (none when starting) - part 1
        self.passwords = []
        # List of real passwords (none when starting) - part 2
        self.real_passwords = []

    # Part 1
    def find_passwords(self):
        for guess in range(self.min, self.max):
            # Reset requirements
            self.twin = False
            self.ascending = False

            # List of digits of the current guess
            guess_digits = [int(digit) for digit in str(guess)]
            
            # Check if there is at least one pair of twins
            for i in range(len(guess_digits) - 1):
                if (guess_digits[i] == guess_digits[i + 1]):
                    self.twin = True
            # Check for the ascending requirement
            if sorted(guess_digits) == guess_digits:
                self.ascending = True
            # Save the guess in the paswords
            if self.twin and self.ascending:
                self.passwords.append(guess)

    # Part 2
    def find_real_passwords(self):
        for password in self.passwords:
            # Only requirement to check now is the new real twin requirement
            self.twin = False

            # List of digits of the current password
            password_digits = [int(digit) for digit in str(password)]

            # List of all the pairs
            repeats_list = []

            # Find all the pairs of twins
            for i in range(len(password_digits) - 1):
                if (password_digits[i] == password_digits[i + 1]):
                    repeats_list.append(password_digits[i])

            # Sort them highest to lowest
            repeats_list.sort(reverse=True)

            # If the highest twin is unique, then save the password
            if repeats_list.count(repeats_list[0]) == 1:
                self.real_passwords.append(password)
                    

# Instance of the password cracker
password_cracker = PasswordCracker()
# Find all the possible passwords
password_cracker.find_passwords()
# Get the length of the list of possible passwords
print(f"Possible Passwords for Part 1: {len(password_cracker.passwords)}")
password_cracker.find_real_passwords()
# Get the lengths of the list of real passwords
print(f"Possible Real Passwords for Part 2: {len(password_cracker.real_passwords)}")