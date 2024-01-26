# Constants for pricing and discounts
PIZZA_PRICE = 12  
TUESDAY_DISCOUNT = 0.5
DELIVERY_CHARGE = 2.50
APP_DISCOUNT = 0.25

# Input Functions 

def get_pizza_count():
  """ 
  Get number of pizzas ordered from user
  
  Parameters: None
  
  Returns:
    - count: Total number of pizzas ordered (integer)
  """

  count = input_number("How many pizzas ordered? ")  
  return count

def input_number(prompt):
  """
  Get valid integer number input from user
  
  Parameters:
    - prompt: Text prompt for user
  Returns: 
    - num: Integer number entered by user
  """
  while True:
    try:
      num = int(input(prompt))
      if num > 0: 
        return num
      print("Enter positive number!")
    except ValueError:
      print("Invalid input!")

def confirm(question):
  """
  Get yes/no input from user for a question
  
  Parameters:
    - question: Question text to display
  
  Returns:
    - value: True for Yes, False for No 
  """
  
  while True:
    reply = input(question).lower()
    if reply[0] == 'y':
      return True
    elif reply[0] == 'n':
      return False
    else:
      print("Enter Yes or No!")

# Calculation  

def calculate_price(count, tuesday, delivery, app):
  """
  Calculate total order price after discounts and fees
  
  Parameters:
    - count: Number of pizzas 
    - delivery: True if delivery wanted, False otherwise
    - tuesday: True if Tuesday, False otherwise  
    - app: True if mobile app is 4used, False otherwise
  
  Returns:
    - total: Price after discounts and charges rounded to 2 decimals 
  """

  total = count * PIZZA_PRICE

  # Apply discount logic  
  if tuesday:  
    total *= (1 - TUESDAY_DISCOUNT)

  if delivery:
    # Check free delivery
    if count < 5:
       total += DELIVERY_CHARGE

  if app:
    total *= (1 - APP_DISCOUNT)

  return round(total, 2)
  
# Main Code  
"""Main function to run the pizza price calculator."""
print("BPP Pizza Price Calculator")
print("=" *26)

num_pizzas = get_pizza_count() 
is_delivery = confirm("Is delivery required? (Y/N): ")
is_tuesday = confirm("Is it Tuesday? (Y/N): ")  
used_app = confirm("Did the customer use the app? (Y/N): ")

price = calculate_price(num_pizzas, is_tuesday, is_delivery, used_app)
print(f"\nTotal Price: £{price}")