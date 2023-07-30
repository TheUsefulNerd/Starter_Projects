import random    # random module here helps us select values randomly
import string    # string module helps us use deifferent letters numbers special chars etc

# First mistake....Intendation...python does not work if wrongly intended...spacing correctly is the key

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False    # intially here we assume all are false
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:   # here in python the countdown starts from 0..so due to indexing the given statement works
        new_char = random.choice(characters)  # . choice module helps us ranomly select values
        pwd += new_char

        if new_char in digits: # now through conditional statements we define if the variables are true or not
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = meets_criteria and has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length: "))
has_numbers = input("Should include numbers? (y/n)").lower() == "y"
has_special = input("Should include special characters? (y/n)").lower() == "y"

pwd = generate_password(min_length, has_numbers, has_special)
print("The Generated Password is:", pwd)

