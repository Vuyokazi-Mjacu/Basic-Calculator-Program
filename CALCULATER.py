num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
operation = input("enter operation:")

if operation == "+" : 
    result = num1 + num2
elif operation == "-" :
    result = num1 - num2
elif operation == "*" :
    result = num1 * num2
elif operation == "/" :
    if num2 == 0 : 
        print("division by zero is not allowed.")
    else: 
        result = num1 / num2
else: 
    print("invalid operation. Please enter +, -, *, or /.")
    exit()

print(f"{num1} {operation} {num2} = {result}")