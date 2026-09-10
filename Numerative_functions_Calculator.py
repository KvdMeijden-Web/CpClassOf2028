
def add(a,b):
    c = a + b
    return c
def minus(a,b):
    c = a - b
    return c
def multiply(a,b):
    c = a * b
    return c
def divide(a,b):
    c = a / b
    return c

operation = str(input("+,-,* or /?"))
firstNumber= int(input("what is the first number?"))
secondNumber= int(input("what is the second number?"))

if operation == "+":
    result = add(firstNumber,secondNumber)
elif operation == "-":
    result = minus(firstNumber,secondNumber)
elif operation == "*":
    result = multiply(firstNumber,secondNumber)
elif operation == "/":
    result = divide(firstNumber,secondNumber)
else:
    print("operation unkown")

print(result)


