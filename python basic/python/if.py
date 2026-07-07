#if else : conditional statement
# condition must be true to execute if block

# syntax:
#     if condition
#     print("statement")

a=int(input("enter a number"))
b=int(input("enter anotehr number"))
# a=5
# b=5
if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print("Equal")
    
elif b>a:
    print(f"{a} is less than {b}")
# else :
#     print("Error")