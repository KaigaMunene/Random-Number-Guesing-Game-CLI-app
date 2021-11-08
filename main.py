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
  endpoint = enter_input()
  random_number = random.randrange(1, endpoint)
  return random_number