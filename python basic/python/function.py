#Function: like variable, block of code is defined to a function
# specific tasks 
# syntax:
# def fucntion_name():
#     function_statement

# def addiition (a , b ,add):
#     print(s)
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# s= a + b
# addiition(a , b , s)  #fucntion call

    
    
#keyword arguements
# def intro(name = None , age= None , address="default"):
#     print(f"my name is {name} and i am {age} years old and i live in {address}")
    

# intro(name = "Ace" , age= 35 , address= "KTM")
# intro(age= 35 , address= "KTM" , name = "Ace")
# intro("Ram" , 35 , "PKH")
# intro()
#default arguement



# local and global variable 
#global variable can be used to access anywhere in the program , to change use "global" keyword

# a= 15
# def addition(first):
#     global a    #in case global data has to be changed in side of the fucntion 
#     a+=5
#     b=5
#     print("local")
#     print(a)
#     print(b)
# addition(a)
# print("global")
# print(a)

# a = float(input("Enter first number: "))
# op = input("Enter operator (+, -, *, /): ")
# b = float(input("Enter second number: "))
    
# def calculator():  
   

#     if op == "+":
#         print(f"Result: {a + b}")
#     elif op == "-":
#         print(f"Result: {a - b}")
#     elif op == "*":
#         print(f"Result: {a * b}")
#     elif op == "/":
#         if b != 0:  
#             print(f"Result: {a / b}")
#         else:
#             print("Error: Cannot divide by zero.")
#     else:
#         print("Invalid operator.")

# calculator() 

