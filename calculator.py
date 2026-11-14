import re

def calculator(expression):
  numbers = re.split(r"\s*[+-/%*]\s*", expression)
  operators = re.split(r"\s*[0-9]\s*", expression)
  result = 0
  count = 0

  for operator in operators:
    if operator == "%":
      if count >= 1:
        numbers[0] = result
        numbers[1] = numbers[1 + count]
        result = percent(numbers[0], numbers[1])
        
      result = percent(numbers[0], numbers[1])
      count += 1
      
    if operator == "/":
      if count >= 1:
        numbers[0] = result
        numbers[1] = numbers[1 + count]
        result = division(numbers[0], numbers[1])
        
      result = division(numbers[0], numbers[1]) 
      count += 1
      
    if operator == "*":
      if count >= 1:
        numbers[0] = result
        numbers[1] = numbers[1 + count]
        result = multiplication(numbers[0], numbers[1])

      result = multiplication(numbers[0], numbers[1])
      count += 1
      
    if operator == "+":
      if count >= 1:
        numbers[0] = result
        numbers[1] = numbers[1 + count]
        result = addition(numbers[0], numbers[1])
        
      result = addition(numbers[0], numbers[1])
      count += 1
      
    if operator == "-":
      if count >= 1:
        numbers[0] = result
        numbers[1] = numbers[1 + count]
        result = subtration(numbers[0], numbers[1])
        
      result = subtration(numbers[0], numbers[1])
      count += 1

  return result

def addition(first_value, second_value):
  return int(first_value) + int(second_value)

def subtration(first_value, second_value):
  return int(first_value) - int(second_value)

def multiplication(first_value, second_value):
  return int(first_value) * int(second_value)

def division(first_value, second_value):
  return int(first_value) / int(second_value)
  
def percent(first_value, second_value):
  return int(first_value) % int(second_value)



def app():
  key = True
  while key == True:
    expression = input("Qual calculo deseja: ")
    if expression == "exit":
      key = False
      break
      
    print(f"Resultado: {calculator(expression)}")

app()
    

