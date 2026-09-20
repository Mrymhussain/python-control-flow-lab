# Exercise 0: Example
def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")
print_greeting()

# Exercise 1: Vowel or Consonant
def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ")

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input.")
    elif letter.lower() in "aeiou":
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

check_letter()


# Exercise 2: Old enough to vote?
def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        voting_age = 18

        if age < 0:
            print("Invalid age.")
        elif age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")

    except ValueError:
        print("Please enter a valid age.")

check_voting_eligibility()

# Exercise 3: Calculate Dog Years
# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    age = int(input("Input a dog's age: "))

    if age <= 2:
        dog_years = age * 10
    else:
        dog_years = 20 + (age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")

calculate_dog_years()