print("Welcome to the SmartCalculator 9000")
while True:

    n1 = input("Enter the first number:   ")
    n1 = float(n1)

    operator = input("Enter the operator:")

    n2 = input("Enter the second number:   ")
    n2 = float(n2)

    if operator == "/" and n2 == 0:
        print("I don't want to do this sum because it is impossible.")


    if operator == "+":
        result = n1+n2  
    elif operator == "-":
        result = n1-n2
    elif operator == "*":
        result = n1*n2
    elif operator == "/":
        if n2 != 0:
            result = n1/n2
    else:
        print("You typed the wrong symbol")
        quit(0)

    if operator != "/" or n2 != 0:
        print("The result is",result)
    if input("Would you like to use the calculator again? ")== "no":
        quit(0)
