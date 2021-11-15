import random

def enter_input():    
  '''
  function for user to insert his/her input.
  ''' 
  while True:
      user_input = input()
      if user_input.isdigit():
          return int(user_input)
      else:
          print("Enter a number or digit")

def generate_random_numbers():    
  ''' 
  function for getting a random number from a range specified by user.
  '''
  print("Enter the rangepoint: ")
  endpoint = enter_input()
  random_number = random.randrange(1, endpoint)
  return random_number

def generate_score(guesses_taken):
  ''' 
  function to return the score of the User
  '''
  initial_score = 6
  score = initial_score - guesses_taken
  return score

print("I am thinking of a number.")
print("Take a guess:")

guesses_taken = 0
comp_number = generate_random_numbers()
while guesses_taken < 5:
  guess = enter_input() 
  guesses_taken += 1
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
      print(f"Yeah you\"ve got it, this is your score: {generate_score(guesses_taken)}")
      break