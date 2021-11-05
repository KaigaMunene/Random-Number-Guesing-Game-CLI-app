import random

def enter_input():
    while True:
        user_input = input()
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Enter a number or digit")

def enter_random_numbers():
    endpoint = enter_input()
    random_number = random.randrange(1, endpoint)
    return random_number

def generate_score(guessses):
  score = 5
  score = score - guessses
  return score

print("I am thinking of a number between 1 and 20.")
print("Take a guess\n:")
guessses_taken = 0
comp_number = enter_random_numbers()

while guessses_taken < 5:
    guess = enter_input()
    guessses_taken = guessses_taken + 1
    if guess < comp_number :
        print("Your geuss is too low")
    if guess > comp_number :
        print("Your guess is too high")
    if comp_number % 2 == 0:
        print("The comp_number is a multiple of 2")
    if comp_number % 3 == 0:
        print("The comp_number is a multiple of 3")
    if comp_number % 5 == 0:
        print("The comp_number is a multiple of 5")
    if guess == comp_number:
        print("correct")
        break

# initial_score = 5
# score = initial_score + 1
# while guess == comp_number:
#     score = score - guessses_taken
#     print(f"Your score is: {score}" )
#     break

# def check_input(input):
#     if input.isdigit():
#         return  True
#     return False

def  difference_btwn_input_actual():
    num1 = input()
    num2 = comp_number
    if num2 > num1:
        return num2 - num1
    elif num2 < num1:
        print(num1 - num2)













 
