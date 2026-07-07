#Exception handling: exception that raise when executing a program
# try-except block
# try: block of code that raise exception areb placed in try box
# except: block of code that is to be executed when exception raises in try block
#finally : block of codce that is to be exceuted if exception raises or not 
# only one catch all except block is to be defined
# multiple error specidifc except blocks can be defined


# try:
#     a= int(input("enter a number:"))
#     print(a+20)
# except ValueError:
#     print("value error")
# except NameError:
#     print("name error")
# except:
#     print("any other exception")
while True:
    try:
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
            if b != 0:  # Note: Changed from 'a != 0' to check the denominator
                print(f"Result: {a / b}")
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid operator.")
            
    except ValueError:
        print("Value error")
    except NameError:
        print("NameError")
    
            
    choice = input("Do you want to continue? (y/n): ")
    if choice != "y":
        print("Goodbye!")
        break
        
        
        