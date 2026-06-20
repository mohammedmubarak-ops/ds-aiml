# class Address:
#     def __init__(self,city,state):
#         self.city=city
#         self.state=state
#     def show(self):     #method
#         print("the city is :",self.city)
#         print("the state is :",self.state)
# a=Address("jaipur","rajasthan")    # a --> object
# a.show()


#--------------------INHERITANCE-----------------------
# class Address:
#     def __init__(self,city,state):
#         self.city=city
#         self.state=state
#     def location(self):
#         return f"my location is {self.city} in {self.state}"

# class User(Address):
#     def __init__(self,name,age,city,state):
#         super().__init__(city,state)   
#         self.name=name
#         self.age=age
#         # self.city=city   ------>   #use super
#         # self.state=state ------>    #keyword
#     def userName(self):
#         print(f"my name is {self.name}")
#     def userDetails(self):
#         print(f"my name is {self.name} and my location is {self.city} in {self.state}")    

# u=User("Mohammed",18,"jaipur","rajasthan")
# u.userDetails()
# u.location()


#-------------------ENCAPSULATION-----------------------
# class Address:
#     def __init__(self,city,state):
#         self.__city=city   #private attribute
#         self.state=state
#     def location(self):
#         print(f"my location is {self.__city} in {self.state}")
#     def getCity(self):
#         return self.__city
        
# a=Address("jaipur","rajasthan")
# a.location()
# a.getCity()
# #print(a.__city)
# print(a.state)


#-------------------POLYMORPHISM-----------------------
# class Address:
#     def __init__(self,city,state):
#         self.city=city
#         self.state=state
#     def location(self):
#         print(f"my address location is {self.city} in {self.state}")

# class hometown:
#     def __init__(self,city,state):
#         self.city=city
#         self.state=state
#     def location(self):
#         print(f"my hometown location is {self.city} in {self.state}")        

# a=Address("jaipur","rajasthan")
# a.location()

# b=hometown("sikar","rajasthan")
# b.location()


#-------------------CLASS VARIABLES-----------------------
# class Withdraw:
#   total = 0 # class variable
#   def __init__(self,city,state):
#     self.city = city
#     self.state = state
#     Withdraw.total += 1
 
#   def location(self):
#     print("location")
 
# a = Withdraw("jaipur","rajasthan")
 
# b = Withdraw("bhilwara","rajasthan")
 
# a.total
 

#-------------------OVERLOADING AND OVERRIDING-----------------------
#overriding
class Address:
    def __init__(self,city,state):
        self.city=city
        self.state=state
    def location(self):
        print("address")

class User(Address):
    def __init__(self,name,age,city,state):
        super().__init__(city,state)
        self.name=name
        self.age=age
    def location(self):      #overriding
        print("user location")

u=User("Mohammed",18,"jaipur","rajasthan")                
u.location()