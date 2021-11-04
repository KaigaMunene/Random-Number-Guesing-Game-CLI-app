# def create_random_number(number):
# while True:
# print(create_random_number("number"))
import random
number = random.choice(range(1,10))
print("I am thinking of a number between 1 and 10."),
guessses_taken = 0
while guessses_taken < 5:
    #print(str(number))   
    guess = int(input("Take a guess\n:"))
    guessses_taken = guessses_taken + 1
    if guess < number :
        print("Your geuss is too low")
    if guess > number :
        print("Your guess is too high")
    if number % 2 == 0:
        print("The number is a multiple of 2")
    if number % 3 == 0:
        print("The number is a multiple of 3")
    if number % 5 == 0:
        print("The number is a multiple of 5")
    if guess == number:
        print("correct")
        break

initial_score = 5
score = initial_score + 1
# if guess == number:
#     print(f"Your score is: {score}" )
# elif guess != number:
#     print(score - guessses_taken)
while guess == number:
    score = score - guessses_taken
    print(f"Your score is: {score}" )
    break






 
