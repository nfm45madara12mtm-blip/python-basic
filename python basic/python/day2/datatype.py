#string 
a='hello he\'s'
a="hello he's"
a='''"hello 
he's 
world
1234"'''



print (a)

#intergers
i=89
print(i)
print(type(i))

#float
f=89.88
print(f)
print(type(f))


#boolean
a=True
b=False
print(b)

#none
n= None
print(n)
print(type(n))


#group datattype 
#list: []-used to define list , lost multiple datatype, ordered , mutable
my_list=["hello , 50 , 1.11, True"]
print(my_list)
print(type(my_list))

#tuple : ()-used to define tuple , hold mustiple data and datatypes, immutable , ordered
my_tuple=("hello , 50 , 1.11, True")
print(my_tuple)
print(type(my_tuple))

#set : {}- used to define set , hold mustiple data and datatypes , unordered , does not accept duplicate datas
my_set={"hello" , 50 , 50, 1.11, "True"}
print(my_set)
print(type(my_set))


#dictionary: {}-used to define dictionary , key: value pair
my_dict={1:"name" ,
         2:"ram"}
print(my_dict)
print (type(my_dict))