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

def calculate_dog_years():
    age = int(input("Input a dog's age: "))

    if age <= 2:
        dog_years = age * 10
    else:
        dog_years = 20 + (age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")

calculate_dog_years()

# Exercise 4: Weather Advice

def weather_advice():
    cold = input("Is it cold? (yes/no): ").lower()
    raining = input("Is it raining? (yes/no): ").lower()

    if cold not in ["yes", "no"] or raining not in ["yes", "no"]:
        print("Invalid input. Please enter yes or no.")
    elif cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

weather_advice()

# Exercise 5: What's the Season?

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    day = int(input("Enter the day of the month: "))

    if month == "Dec" and day >= 21 or month in ["Jan", "Feb"] or month == "Mar" and day <= 19:
        season = "Winter"
    elif month == "Mar" and day >= 20 or month in ["Apr", "May"] or month == "Jun" and day <= 20:
        season = "Spring"
    elif month == "Jun" and day >= 21 or month in ["Jul", "Aug"] or month == "Sep" and day <= 21:
        season = "Summer"
    else:
        season = "Fall"

    print(f"{month} {day} is in {season}.")

determine_season()

# Exercise 6: Number Guessing Game

def guess_number():
    target = 42

    for attempt in range(1, 6):
        if attempt == 5:
            print("Last chance!")

        guess = int(input("Guess a number between 1 and 100: "))

        if guess == target:
            print("Congratulations, you guessed correctly!")
            break
        elif guess < target:
            print("Guess is too low")
        else:
            print("Guess is too high.")

    else:
        print("Sorry, you failed to guess the number in five attempts.")

guess_number()