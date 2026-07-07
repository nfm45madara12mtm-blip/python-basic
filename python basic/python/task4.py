# define a dictionary username as key and password as value
# get the username and password from the user
# check if the username exists in the dictioney
# if yes: check if the password is correct(if yes: print Valid or Verified user, if no: print password incorrect)
# if no: print the statement(eg: Invalid username)



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