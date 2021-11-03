# def create_random_number(number):
# while True:
# print(create_random_number("number"))
import random
number = random.choice(range(1,20))
print("I am thinking of a number between 1 and 10."),
guess_taken = 0
while guess_taken < 5:
    guess = int(input("Take a guess\n:"))
    guess_taken = guess_taken + 1
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


 
