print("It's a code for a basic calculator")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
c=input("Enter the operator:\n For addition press +\n For subtraction press -\n For multiplication press *\n For division press / ")
if c=="+":
    print(f"{num1}+{num2}={num1+num2}")
elif c=="-":
    print(f"{num1}-{num2}={num1-num2}")
elif c=="*":
    print(f"{num1}*{num2}={num1*num2}")
elif c=="/":
    try:
        print(f"{num1}/{num2}={num1/num2}")
    except ZeroDivisionError:
        print("Error: Division by zero is not possible")
else:
    print("Invalid operator")