#slicing

#start_index:inclusive -> reads
#end_index:exclusive -> no read (end letter ko no. bhanda +1 garni)
#syntax:variable[start_index:end_index+1]
#syntax:variable[start_index:end_index+1 : step]
# b="i am ( learning"
# print(b[0:5])
# print(b[7:5])
# print(b[7:15])
# a="python basic"
# print(a[0:6])
# print(a[0:12])


fruits=[  "Apple",
    "Banana",
    "Orange",
    "Strawberry",
    "Grapes",
    "Watermelon",
    "Pineapple",
    "Mango",
    "Peach",
    "Cherry"]
# print(fruits[-1:])
# print(fruits[0:7])
# print(fruits[0:5])
# print(fruits[0:6])
print(fruits[: -1 ])
# print(fruits[0: 4 : 2])

# print(fruits[1: : 2])


# b="i am ( learning python basic"
# print(b[0: : 1])
# print(b[0: : 1])
# print(b[0: : 1])