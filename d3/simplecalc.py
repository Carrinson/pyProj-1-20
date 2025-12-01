# A very simple calculator in python 
num1 = int(input("Enter num 1"))
num2 = int(input("Enter num2"))

opera = input("Enter Operator (+, -, *, /)")

if opera == "+":
    print(num1 + num2) 
elif opera == "-":
    print(num1-num2)
elif opera == "*":
    print(num1*num2)
elif opera == "/":
    print(num1/num2)
else:
    print("Invalid input try again")