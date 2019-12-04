FILE_DIR = 'day_4/data/range.txt'

GIVEN_RANGE = list(map(int, open(FILE_DIR).readline().split('-')))

class PasswordCracker():
    def __init__(self):
        # Size requirement of password
        self.size = 6
        # Range of min to max
        self.constraint = range(GIVEN_RANGE[0], GIVEN_RANGE[1])
        print(GIVEN_RANGE)
        # Whether or not the 'twin' requirement is met
        self.twin = False
        # Whether or not the password is ascending
        self.ascending = False
        # List of possible passwords
        self.passwords = []
        # Number of passwords
        self.num_of_passwords = 0

    def find_passwords(self):
        for guess in self.constraint:
            # Reset requirements (easiest to check for twin and check for NOT ascending)
            self.twin = False
            self.ascending = True

            # List of digits of the current guess
            guess_digits = list(map(int, str(guess).split()))
            
            # Check if there is at least one pair of twins
            for i in range(len(guess_digits) - 1):
                if (guess_digits[i] == guess_digits[i + 1]):
                    print("Twin")
                    self.twin = True
            # Check if the 
            for i in range(len(guess_digits) - 1):
                if (guess_digits[i] > guess_digits[i + 1]):
                    print("Ascending")
                    self.ascending = False
            if self.twin and self.ascending:
                self.passwords.append(guess)
                print("Yes")

password_cracker = PasswordCracker()
password_cracker.find_passwords()
print(password_cracker.passwords)