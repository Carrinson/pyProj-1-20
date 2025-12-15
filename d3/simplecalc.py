# A very simple calculator in python 
num1 = int(input("Enter num 1: "))

opera = input("Enter Operator (+, -, *, /): ")

num2 = int(input("Enter num2: "))


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