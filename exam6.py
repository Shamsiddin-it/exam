# class Employee:
#     def __init__(self,name,salary,id):
#         self.name=name
#         self._salary=salary
#         self.__id=id
# class Person(Employee):
#     def show(self):
#         print(self.name)
#         print(self._salary)
#         print(self.__id)
# obj1=Person("shams",1000,12)
# obj1.show()
# hangomi zapusk funcsiyai show oshibka medihad,
#  name, salary nishon medihad va bad oshibkae ki attributero nameyobad(id nameyobad)

# 2
# class BankAccount:
#     def __init__(self,balance,pin):
#         self._balance=balance
#         self.__pin=pin
# class Person(BankAccount):
#     def show(self):
#         print(self._balance)
#         print(self.__pin) 
# obj1=Person(345621,1234)
# obj1.show()
# # dar injo ham protective balancero nishon medihad ammo pinro ne chunki pin private hast



# 3(a)
# class BankAccount:
#     def __init__(self,balance,pin):
#         self._balance=balance
#         self.__pin=pin
#     def set_info(self):
#         if int(self._balance)>0:
#             self._balance="1000"
#         else:
#             print("balance can`t be <0")
#     def show(self):
#         print(self._balance)
# obj1=BankAccount(input(),1234)
# obj1.set_info()
# obj1.show()

# 3(b)
# class Employee:
#     company="SoftClub"
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(self.name)
#         print(Employee.company)
# class Person(Employee):
#     def show(self):
#         print(self.name)
#         Employee.company="Rio"
#         print(Employee.company)
# obj1=Employee("Salom")
# obj1.show()
# obj2=Person("Salom")
# obj2.show()
# dar objecti duyum company ivaz meshavad



# 4
# class Animal:
#     def speak():
#         print("No sound")
# class Dog(Animal):
#     def speak():
#         print("Gaf-gaf-gaf")
# class Puppy(Dog):
#     def speak():
#         print("guf-guf")
# obj1=Puppy
# obj1.speak()


# 5
# class Person:
#     def __init__(self,name,country,birthday):
#         self._name=name
#         self.__country=country
#         self.birthday=birthday
#     def age(self):
#         print(2024-self.birthday)
# obj1=Person("salom","Tajikistan",2006)
# obj1.age()



# 6
# class Nobel:
#     def __init__(self,category,year,winner):
#         self.categ=category
#         self.yer=year
#         self.winr=winner
#     def category(self):
#         return str(self.categ)
#     def year(self):
#         return str(self.yer)
#     def winner(self):
#         return str(self.winr)
# np2005=Nobel("Peace",2005,"Muhammad Yunus")
# np2005.category=np2005.category()
# np2005.year=np2005.year()
# np2005.winner=np2005.winner()
# print(np2005.category,np2005.year,np2005.winner)



# 7
# def letter(a):
#     cntu=0
#     cntl=0
#     cnts=0
#     a=list(a)
#     for j in a:
#         j=str(j)
#         if j.isalpha()==False:
#             cnts+=1
#             a.remove(j)
#     for i in a:
#         i=str(i)
#         if i.isupper():
#             cntu+=1
#         else:
#             cntl+=1
#     if cntu==len(a) and cntl==0:
#         print("upper")
#     elif cntu==0 and cntl==len(a):
#         print("lower")
#     else:
#         print("mixed")
# a=input()
# letter(a)


# 8
a=int(input())
i=1
n=1
cnt=0
while cnt<=a:
    n+=1 



# 9
# a=int(input())
# i=1
# while i<=a//2:
#     print((str(i)+" ")*i)
#     i+=1
# cnt=i
# while cnt>=0:
#     print((str(i)+" ")*cnt)
#     cnt-=1
#     i+=1

        
#  10
# class IceCream:
#     def __init__(self, flavor, num_sprinkles):
#         self.flavor = flavor
#         self.num_sprinkles = num_sprinkles
#     def sladosti(self):
#         self.sladost=[]
#         if self.flavor=="Plain":
#             self.sladost.append(0+int(self.num_sprinkles))
#         elif self.flavor=="Vanilla":
#             self.sladost.append(5+int(self.num_sprinkles))
#         elif self.flavor=="ChocolateChip":
#             self.sladost.append(5+int(self.num_sprinkles))
#         elif self.flavor=="Strawberry":
#             self.sladost.append(10+int(self.num_sprinkles))
#         elif self.flavor=="Chocolate":
#             self.sladost.append(10+int(self.num_sprinkles))
#     def show(self):
#         print(max(self.sladost))
# ice1=IceCream("Chocolate",13)
# ice2=IceCream("Vanilla",0)

        
    
