#loop
#while : conditional
# while condition:
#     statement
#     statement

# a= 5
# b= 0
# while a>b:
#     print("a is greater")
#     b+=1
# print("while loop end")


#break: breaks the loop
#if a is 3 end loop
# a= 8
# b= 0
# while a>b:
#     print("a is greater")
#     if b==3:
#         break
#     b+=1
# print("while loop end")

#conitnue : skips the current loop
a= 5
b= 0
while a>b:
    b+=1
    if b==3:
        continue
    print("a is greater" , b)
print("while loop end")

