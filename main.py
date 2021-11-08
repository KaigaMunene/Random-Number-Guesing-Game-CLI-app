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