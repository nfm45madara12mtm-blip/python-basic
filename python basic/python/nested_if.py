a = int(input("enter a age: "))

if a >= 18:
    print("you are eligible for voting")
    card = input("do you have voting card (y/n): ")
    
    if card == "y":
        print("okay")
    elif card == "n":  # Changed = to ==
        create = input("do you want to create one (y/n): ")
        
        if create == "y":  # Changed = to ==
            print("visit the site")
        elif create == "n":  # Changed = to ==
            print("bye")
        else:
            print("not valid choice")
    else :
        print("not valid ")
else:
    print("you are not eligible to vote") 

