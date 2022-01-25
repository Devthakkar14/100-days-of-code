from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {"+":add,"-":subtract,"*":multiply,"/":divide}

def calculator():
  print(logo)
  done = False
  while not done:
    for I in operations:
      print(I)
    operation = input("Enter a symbol : ")
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    func = operations[operation]
    answer = func(num1,num2)
    print("Answer is",answer)
    cont = input("Do you want to continue, yes or no? ")
    if cont=="yes":
      continue
    else:
      done = True

calculator()
