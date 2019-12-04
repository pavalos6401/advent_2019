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
        # List of possible passwords (none when starting)
        self.passwords = []

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

# Instance of the password cracker
password_cracker = PasswordCracker()
# Find all the possible passwords
password_cracker.find_passwords()
# Get the length of the list of possible passwords
print(len(password_cracker.passwords))