import random

num1 = random.randint(1, 100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]
while True:
    guess = int(input('Please enter the number you guessed: '))
    if guess < 1 or guess > 100:
        print("Please enter the number within the limits")
        continue

    if guess == num1:
        print(f"Your guess was correct in {len(guesses)} attempts")
        break

    guesses.append(guess)

    # if there is more than 1 number guessed by user then the code inside if statement will run
    # otherwise content inside else loop will be executed - when number is guessed for first time by the user.
    if guesses[-2]:
        if abs(num1 - guess) < abs(num1 - guesses[-2]):
            print("WARMER")
        else:
            print("COLDER")
    else:
        if abs(num1 - guess) <= 10:
            print("WARM")
        else:
            print("COLD")
