# d = {"name": "Hello" }
# d.update({"name": "World"})
# d["name"] = "World new"
# print(d['name'])
# del d['name']
# print(d)

# l=[20,10]
# print(l[0])


#NESTED DICTIONARY
# d = {"address": {"address1":{"city": "Kukas city", "district": "Jaipur"},
#                  "address2":{"city": "gapalpura", "district": "arya mains"}
#                 }
#     }
# print(d['address']['address1']['city'])
# print(d['address']['address1']['district'])
# print(d['address']['address2']['city'])
# print(d['address']['address2']['district'])






#SLICING IN LIST
# l1=[1,2,3,4,5]
# print(l1[-1:3])




# #map (2 arguments)
# from numpy import square


# l = [10,20,30]
# l1 = list(map(square,l))    
# print(l1)

# #example
# #map (2 arguments)
# l = [10,20,30]
# l1 = list(map(lambda x: x*x, l))
# print(l1)

# #alternative | without in built function
# l1 = []
# for i in range(len(l)):
#     l1.append(l[i]*l[i])
# print(l1)    





# #filter 
# def hello(x):
#     return x.startswith('a')

# l = ['apple', 'banana', 'cat', 'dog']
# l1 = list(filter(hello, l))
# print(l1)

# #example | alternative of filter
# l1 = []
# for i in l:
#     if 'a' == i[-1]:
#         l1.append(i)
# print(l1)

# #print list in upper case 
# l1 = list(map(lambda x: x.upper(), l))
# print(l1)






#try except
try:
    num1=10
    num2=5
    print(num1/num2)
except:
    print ("hello except")

#try except
try:
    num1=10
    num2=0
    print(num1/num2)
except:
    print ("hello except")

#try except and final
try:
    num1=10
    num2=5
    print(num1/num2)
except:
    print ("hello except")            
finally:
    print("hello finally divide")