#oop
#object : data created using class
#class: structures 
 #syntax: 
#  class class_name:
#      attributes: variable
#      methods:function

# class person:
#     name=None
#     age=None
#     address=None
#     gender=None
#     def get_info(self , name , age , address, gender):
#         self.name=name
#         self.age=age
#         self.address=address
#         self.gender=gender
#     def intro(self):
#         print(f"""Name:{self.name}
# age:{self.age}
# address:{self.address}
# gender:{self.gender}""")
        
# ram=person()
# ram.get_info("ram", 35 , "KTM", "Male")
# ram.intro()

    
# sita=person()
# sita.get_info("sita", 25 , "KTM", "Female")
# sita.intro()

# class car:
#     brand=None
#     model=None
#     color=None
#     def cars(self ):
#         print("""brand:{self.brand}
#               model:{self.model}
#               color:{self.color}""")
# bw=car()

# bw.cars("bmw" ,"M4" , "black")


# mer=car()
# mer.brand="Mercedes-Benz"
# mer.model="G-Class"
# mer.color="white"
# print(mer.brand)
# print(mer.model)
# print(mer.color)


#inheritance:

# class Vehicle:
#     brand=None
#     model=None
#     color=None
#     def get_info(self,brand,model,color ):
#         self.brand=brand
#         self.model=model
#         self.color=color
#     def intro(self):
#         print("""brand:{self.brand}
#               model:{self.model}
#               color:{self.color}
#               capacity:{self.capacity}""")
# class ev(Vehicle):
#     capacity = None
# def get_capacity(self , cap):
#     self.capacity=cap
# ev1=ev()
# ev1.get_info ("brand","model" , "color") 
# ev1.intro()
# ev1.get_capacity("6")
# print(ev1.capacity)        



# inheritance:


# todo:
# create animal class, atteibutes: eye, ears, legs, .....
# methods: get_info(), show_info()
# child class
# create dog class, attributes: name,...., method: get_info(), show_info(), move(), sound()
# create bird class, attributes": name, methods: move(), sound()

# create a object of each child class

# class Animal:
#     eyes = None
#     ears = None
#     legs = None
    
#     def get_info(self, eyes, ears, legs):
#         self.eyes = eyes
#         self.ears = ears
#         self.legs = legs
        
#     def show_info(self):
#         print(f"Eyes: {self.eyes}, Ears: {self.ears}, Legs: {self.legs}")


# class Dog(Animal):
#     name = None
    
#     def get_info(self, name, eyes, ears, legs):
#         self.name = name
#         self.eyes = eyes
#         self.ears = ears
#         self.legs = legs
        
#     def show_info(self):
#         print(f"Name: {self.name}, Eyes: {self.eyes}, Ears: {self.ears}, Legs: {self.legs}")
        
#     def move(self):
#         print(f"{self.name} is running!")
        
#     def sound(self):
#         print(f"{self.name} says Woof!")


# class Bird(Animal):
#     name = None
    
#     def move(self):
#         print(f"{self.name} is flying!")
        
#     def sound(self):
#         print(f"{self.name} says Chirp!")

# dog1 = Dog()
# dog1.get_info("Buddy", "2", "2", "4")
# dog1.show_info()
# dog1.move()
# dog1.sound()


# bird1 = Bird()       
# bird1.get_info("sky" ,"2", "2", "2")  
# bird1.show_info()         
# bird1.move()
# bird1.sound()

        
    
            
# Polymorphism
#different classes have same method name 
# fucntionality depends on the object it is classed         



#encapsulation
# class login:
#     _username = None
#     _password = None
    
#     def get_info(self, username, password):
#         self._username = username 
#         self._password = password
        
#     def _show(self):
#         print(f"""username:{self._username}
# password:{self._password}""")
#     def calls(self):
#         self._show()


# p1 = login()
# p1.get_info("Ace", "ace123")
# p1.calls()





# create class Bank
# attributes: username, accountnumber, accountbalance
# methods to get the userinfo, show them to the user,.....
# create private attributes and methods to restrict direct calls
class bank:
    _username= None
    _aaccno=None
    _accbal=None
    
    def get_info(self , username , accno, accbal):
        self._username=username 
        self._accno=accno
        self._accbal=accbal
        
    def _show(self):
        print(f"""username":{self._username}
              accno:{self._accno}
              accbal:{self._accbal}""")
    def calls(self):
        self._show()
        
        
b1=bank()
b1.get_info("ace", "123456" , "1234567890")
b1.calls()