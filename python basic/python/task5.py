# Licence
# get user age
# if user age < 18: 
#     print statment
#     ask if they can to get one(yes/no)
#     if yes: print a statement
#     if no: print a statement
#       one statement for invalid choice(optional)
# if user age >= 18:
#      print a stetement
#     ask if they have Licence:
#     if yes: print a statement:
#     if no: 
#        ask if you want to create one
#        if yes: print a statement
#        if no: print a statement
#        one statement for invalid choice(optional)
#     if not yes or no: a statement for the choice(optional)_

age=int(input("enter age:"))
if age <18:
    print("not eligible")
    que=input("Do you want to get license when eligible(y/n):")
    if que == "y":
            print("visit site")
    elif que=="n":
             print("okay")
    else:
        print("invalid choice")
elif age>=18:
    print("eligible")
    qu=input("do you have a license(y/n):")
    if qu=="y":
        print("great")
    elif qu=="n":
        q=input("do you want to create license(y/n):")
        if q=="y":
            print("visit gov.site")
        elif qu=="n":
            print("okay")
        else:
            print("invalid choice")





            
    
