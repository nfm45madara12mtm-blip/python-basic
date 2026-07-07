# todo: implementing while loop
# get two numbers from user(a,b)
# check the greater number and print it out
# if a is greate than b print a statement {a} is greater than {b}
# if a is less than b
# if a and b are equal
# ask if they want to continue: yes: interate the code, no: terminate the loop

# while True:
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     if a>b:
#         print("A is greatest")
#     else:
#         print("B is greatest")
#     choice=input("Do you want to coninue(y/n):")
#     if choice !="y":
#         print("Goodbye!")
#         break

# simple calculator
# get two numbers from user and a operator(+,-,*,/)
# if the operator is +, print the sum of two number
# if the operator is -, print the subtraction of two number
# if the operator is *, print the multiple of two number
# if the operator is /, print the division of two number
# ask if they want to continue: yes: interate the code, no: terminate the loop

# while True:


    # a = float(input("Enter first number: "))
    # op = input("Enter operator (+, -, *, /): ")
    # b = float(input("Enter second number: "))

    # if op == "+":
    #     print(f"Result: {a + b}")
    # elif op == "-":
    #     print(f"Result: {a - b}")
    # elif op == "*":
    #     print(f"Result: {a * b}")
    # elif op == "/":
    #     if a != 0:
    #         print(f"Result: {a / b}")
    #     else:
    #         print("Error: Cannot divide by zero.")
    # else:
    #     print("Invalid operator.")
            
    # choice = input("Do you want to continue? (y/n): ")
    # if choice != "y":
    #     print("Goodbye!")
    #     break


# get user's exam marks
# if the mark is greater than 100 and less than 0, print a statment
# if the mark is greater than 90 and less then 100, print a statment("Excekllent")
# if the mark is greater than 80 and less than 90 , print a statement
# if the mark is greater than 70 and less than 80 , print a statement
# if the mark is greater than 60 and less than 70 , print a statement
# if the mark is greater than 50 and less than 60 , print a statement
# if the mark is greater than 40 and less than 50 , print a statement
# if the mark is less than 40, print a statment
# ask if they want to continue: yes: interate the code, no: terminate the loop

# while True:
#     marks=float(input("enter marks:"))
#     if marks>=100 and marks<=0:
#         print("pass")
#     elif marks>=90 and marks<=100:
#         print("excellent")
#     elif marks>=80 and marks<=90:
#         print("very good")
#     elif marks>=70 and marks<=80:
#         print("good")
#     elif marks>=60 and marks<=70:
#         print("Average")
#     elif marks>=50 and marks<60:
#         print("below average")
#     elif marks<=40:
#         print("meh")
#     choice = input("Do you want to continue? (y/n): ")
#     if choice != "y":
#         print("Goodbye!")
#         break


# define a dictionary username as key and password as value
# get the username and password from the user
# check if the username exists in the dictioney
# if yes: check if the password is correct(if yes: print Valid or Verified user, if no: print password incorrect)
# if no: print the statement(eg: Invalid username)
# ask if they want to continue: yes: interate the code, no: terminate the loop


while True:
    users={"ace":"a123",
       "aalice":"b456",
       "yuna":"c321"}

    username=input("enter a username:")
    passw=input("enter password:")

    if username in users:
        if users[username] == passw:
            print("valid user")
        else:
            print("invalid password")
    else :
        print("invalid user")
    choice = input("Do you want to continue? (y/n): ")
    if choice != "y":
        print("Goodbye!")
        break




