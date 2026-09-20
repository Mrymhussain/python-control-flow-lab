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

    is_cold = cold == "yes"
    is_raining = raining == "yes"

    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    elif not is_cold and not is_raining:
        print("Wear light clothing.")

weather_advice()

# Exercise 5: What's the Season?

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    day = int(input("Enter the day of the month: "))

    if month in ["Jan", "Feb"]:
        season = "Winter"

    elif month == "Mar":
        if day < 20:
            season = "Winter"
        else:
            season = "Spring"

    elif month in ["Apr", "May"]:
        season = "Spring"

    elif month == "Jun":
        if day < 21:
            season = "Spring"
        else:
            season = "Summer"

    elif month in ["Jul", "Aug"]:
        season = "Summer"

    elif month == "Sep":
        if day < 22:
            season = "Summer"
        else:
            season = "Fall"

    elif month in ["Oct", "Nov"]:
        season = "Fall"

    elif month == "Dec":
        if day < 21:
            season = "Fall"
        else:
            season = "Winter"

    print(f"{month} {day} is in {season}.")

determine_season()