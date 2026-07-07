a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print(f"Result: {a + b}")
elif op == "-":
    print(f"Result: {a - b}")
elif op == "*":
    print(f"Result: {a * b}")
elif op == "/":
    if a != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator.")
    





