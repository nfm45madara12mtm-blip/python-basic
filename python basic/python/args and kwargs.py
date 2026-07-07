
# def addition(*args):
#     total=0 
#     for i in args:
#         total+=1
#         print(total)
# addition(4 ,5 ,6, 4)

#create a fucntion that print out the intro of the user name sent to it eg: i am 
# def intro(*intr):
#     for i in intr:
#         print(f"i am {i}")
# intro('Ace','b' , 'c')

#kwargs: keywords arguments , sent multiple keyword argument to a parameter

# def student(**kwargs):
#     # print(f"Name:{name}")
#     # print(f"rollno:{rollno}")
#     # print(f"grade:{grade}")
#     # print(f"address:{address}")
#     print(kwargs)
#     print(kwargs.items())
#     print(kwargs.keys())
#     print(kwargs.values())

#     for i, j in kwargs.items():
#         print(i)
#         print(j)
#         print(f"{i}:{j}")
        
# student(name="Ace" , age=25 ,grade= 5, address="KTM")


# fucntion based
# add two number
# get a number from the user and multiply it with the sum
while True:

    def addition(c ,d):
        c=int(input("enter a 1number:"))
        d=int(input("enter a 2number:"))
        add=c+d
        return add

    a= addition("c" , "d")

    
    b= int(input("enter a number3:"))

    print(a*b)
    choice=input("continue?:")
    if choice !="y":
        print("goodbye")
