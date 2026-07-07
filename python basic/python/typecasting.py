# a=input("enter your 1 no:")  
# b=input("enter your 2 no:")
# print(type(a))
# print(type(b))
# print(a+b)
# print(a*3)


# #typecasting
# # convert string to interger

# n=int(a)
# c=int(b)
# print(type(n))
# print(type(c))
# print(n+c)
# print(n*3)

# #string to float

# n=float(a)
# c=float(b)
# print(type(n))
# print(type(c))
# print(n+c)
# print(n*3)

# #float to string
# n=str(a)
# c=str(a)
# print(type(n))
# print(type(c))
# print(n+c)
# print(n*3)

#convert to list()
fruits = {
    "Apple",
    "Banana",
    "Orange",
    "Strawberry",
    "Grapes",
    "Watermelon",
    "Pineapple",
    "Mango",
    "Peach",
    "Cherry"
}
print(type(fruits))
mylist=list(fruits)
print(mylist)
print(type(mylist))

#convert to tuple
mytup=tuple(mylist)
print(mytup)
print(type(mytup))

#convert to set
myset=set(mytup)
print(myset)
print(type(myset))

#convert to dictionary
a=[("name" , "ram"), ("age", 35), ("address", "KTM")]
mydict=dict(a)
print(mydict)
print(type(mydict))