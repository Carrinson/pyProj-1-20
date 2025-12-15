# A number comparison application

print("Guess the number!!")

num1 = int(input("Enter a number "))

constNum = 212


if num1 == constNum:
    print("Number is correct")
elif num1 > constNum:
    print("go lower")
elif num1 < constNum:
    print("go higher")
else:
    print("try again")
