#file handling: process of manipulating file programatically

#open the file
#f=open(file_path , mode)
#close
# f.close()

# f=open("day2\datatype.py", 'r')
# a=f.read()
# f.close()
# print(a)

#write(w)
# f=open("day1\day1.py", 'w')
# a=f.write("Hi")
# f.close()

#append(a) #new line are added without replacing the prev data
# f=open("day1\day1.py", 'a')
# f.write("OKAY")
# f.close()

#todo
#login/register ask user
#if choice is register get user name form user and store it in a file
#if login get usernbame from the user and check if the user name exist in the file

choice=input("Enter choice (login/register):")
users={"ace":"a123", "hmm":"h321"}
if choice == "register":
    f = open("day1.txt", "w")
    f.write(input("Enter new user: "))
    f.close()

elif choice=="login":
    username=input("Enter User:")
    print(username in users)
    
    
# Accounting(.txt, .json)
# login/register ask user
# if register: get username, password(optional) from user and store it in a file
# if login: get username, password(optional) from the user and check if the username exists in the file
# show 2  options: read balance, add balance
# if add: get the amount to add store it in a file in dict format({username: amount})
# if read: print out the balance of that user
    
choice=input("Enter choice (login/register):")
users={"ace":"a123", "hmm":"h321"}
if choice == "register":
    f = open("day1.txt", "w")
    f.write(input("Enter new user: "))
    f.close()

elif choice=="login":
    username=input("Enter User:")
    print(username in users)
option=input("balance(read/add)")
if option == "add":
        f=open("balance.txt" , "w")
        f.write(input({"usename":"amount"}))
        f.close()
elif option =="read":
        print("zero balance")
        