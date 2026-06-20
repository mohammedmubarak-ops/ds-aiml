# example (OOPs)
# class Mohammed:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(self.name)      
# m = Mohammed("Hello")
# m.show()        


#example 1
# class Mohammed:
#     def __init__(self):
#         print("calling constructor")
#     def show(self):
#         print("show the name")
# m = Mohammed()
# m.show()


#example 2
# class Mohammed:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def getAge(self):
#         print("My age is",self.age)
#     def getName(self):
#         print("My name is",self.name)
# m = Mohammed("Mohammed",18)    
# m.getName()
# m.getAge()


#exmple 3
# class student:
#     def __init__(self,args):
#         print(type(args))
#         print(args)
#         self.name=args["name"]
#     def getstu(self):
#         print("My name is",self.name)
#         return self.name 
# s = student({"name":"Mohammed","age":18})
# t = s.getstu()
# print(t)


#example 4           
class Student:
    def __init__(self,*args):
        self.data=args
    def users(self):
        for i in self.data[0]:
            print(i)
    def details(self):
        for i in self.data[1]:
            print(self.data[1][i])
s=Student(["Dheeraj","kunal","harsh","praveen"],{"address":"kukas","college":"arya","loc":"jaipur"})
s.users()
s.details()