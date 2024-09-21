# 1
# def multipl(a):
#     for i in range(1,11):
#         print(f"{a}*{i}={a*i}")
# a=int(input("From = "))
# b=int(input("To = "))
# for i in range(a,b+1):
#     multipl(a)
#     print(" ")
#     a+=1


# 2
# class Circle:
#     PI = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def get_area(self):
#         print(f"area = {2* self.PI * self.radius * self.radius}")
#     def get_diametr(self):
#         print(f"diametr = {2*self.radius}")
#     def get_circumference(self):
#         print(f"circumference = {2* self.PI * self.radius}")
#     def get_radius(self):
#         print(f"radius = {self.radius}")
# obj1 = Circle(float(input()))
# obj1.get_area()
# obj1.get_diametr()
# obj1.get_circumference()
# obj1.get_radius()


# 3
# class Calculator:
#     @staticmethod
#     def factorial(n):
#         mul=1
#         for i in range(1,n+1):
#             mul*=i
#         print(mul)
    
#     @staticmethod
#     def power(a,b):
#         print(a**b)

#     @staticmethod
#     def sqrt(n):
#         print(n**0.5)

# obj1=Calculator
# obj1.factorial(int(input())) 
# obj1.power(int(input()),int(input()))
# obj1.sqrt(int(input()))


# 4
# class Calculator:
#     def __init__(self,first,operation,second):
#         self.first = first
#         self.operation = operation
#         self.second = second
#     def Sum(self):
#         print(f"{self.first} + {self.second} = {self.first + self.second}")
#     def Subtract(self):
#         print(f"{self.first} - {self.second} = {self.first - self.second}")
#     def Multiplication(self):
#         print(f"{self.first} * {self.second} = {self.first * self.second}")
#     def Division(self):
#         print(f"{self.first} / {self.second} = {self.first / self.second}")

# while True:
#     obj1=Calculator(
#     float(input("The first number is: ")),
#     input("The operation is: "),
#     float(input("The second number is: "))
# )
#     match obj1.operation:
#         case "+":
#             obj1.Sum()
#         case "-":
#             obj1.Subtract()
#         case "*":
#             obj1.Multiplication()
#         case "/":
#             obj1.Division()
#         case _:
#             print("Enter only + - * / !")
#             break


# 5
# students=[]
# class Student:
#     id = 0
#     def __init__(self,name,surname,age,number,username):
#         self.id+=1
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.number = number
#         self.username = username
#         Student.id+=1
    
#     def __str__(self):
#         return f"{self.name} {self.surname} {self.age} {self.number} {self.username}"
# class StudentManager:
#     def Accept(self):
#         student = Student(
#             input("Enter the name: "),
#             input("Enter the surname: "),
#             input("Enter the age: "),
#             input("Enter the phone number: "),
#             input("Enter the username: ")
#         )
#         students.append(student)
#     def Display(self):
#         for student in students:
#             print(student)
#     def Search(self,username):
#         for student in students:
#             try:
#                 if student.username==username:
#                     print(student)
#             except:
#                 print("There is no student with this username!")
#     def Delete(self,id):
#         for student in students:
#             if student.id==id:
#                 students.remove(student)
#             else:
#                 print("There is no student with this id!")  
#     def Update(self,id):
#         for student in students:
#             if student.id==id:
#                 student.username = input("Enter new username: ")
#                 student.number = input("Enter new phone number: ")
#             else:
#                 print("There is no student with this id!") 
# student=StudentManager()
# while True:
#     match input("""
# 1-Accept
# 2-Display
# 3-Search
# 4-Delete
# 5-Updaate 
# 6-exit                                               
# """):
#         case "1":
#             student.Accept()
#         case "2":
#             student.Display()
#         case "3":
#             student.Search(input(
#                 "Enter username: "
#             ))
#         case "4":
#             student.Delete(int(input("Enter id: ")))
#         case "5":
#             student.Update(int(input("Enter id: ")))
#         case "6":
#             break


# 6
# list_of_users=[]
# class User:
#     id = 0
#     def __init__(self,first_name,last_name,username,password):
#         self.id+=1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.password = password
#         User.id+=1

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} {self.username} {self.password}"

# class UserManager:
#     def register(self):
#         user = User(
#             input("first name: "),
#             input("last name: "),
#             input("username: "),
#             input("password: ")
#         )
#         list_of_users.append(user)
    
#     def login(self):
#         username=input("username: ")
#         password = input("password: ")
#         for user in list_of_users:
#             if user.username==username:
#                 if user.password==password:
#                     print("Login successful!")
#                 else:
#                     print("password incorrect!")
#             else:
#                 print("username incorrect!")

#     def change_password(self):
#         username=input("username: ")
#         password = input("old password: ")
#         for user in list_of_users:
#             if user.username==username:
#                 if user.password==password:
#                     user.password = input("new password")
#                 else:
#                     print("password incorrect!")
#             else:
#                 print("username incorrect!")

#     def get_users(self):
#         for user in list_of_users:
#             print(user)

# user=UserManager()
# while True:
#     match input("""
# 1.register
# 2.login
# 3.change_password
# 4.get_users
# 5.exit
# """):
#         case "1":
#             user.register()
#         case "2":
#             user.login()
#         case "3":
#             user.change_password()
#         case "4":
#             user.get_users()
#         case "5":
#             break
#         case _:
#             print("only from 1 to 5")
        

# q1
# oop in yak nav`i paradigma ast ki as class va object iborat ast
# on codi moro ba guruhho yo sinfho taqsim mekjnad ki baroi fahmidani cod qulay ast
# 4 princip dorad
# 1-encapsulation: metavonem attributhoro obshedostupni, zashishonni va privatni kunem bo yori _ va __
# inheritence: metodu taghiryobandahoi yak klassro dar digar classi child istifoda burda metavonem
# polimorfizm: mnogofuncsionalnosti objectero meguyand yane yak object chand deystviyaro ijro karda metavonad
# abstraction: in yane yak metodro chunone mekunad da r clasi abstractni ki hangomi dar classi child ionro boyad owerwrite kunem va funcsional dihem


# q2
# `getter mo metavonem attributhoi privatni dostup paydo kunem yane return kunem
# setter onro ivaz karDA metavonem
# property yak rihi elegantnii getter va setter ast ki badan onro be qavs faryod karda metavonem


# q3
# `meshavand clas metod instance metod
# variablho niz hamchunon meshavand va boz variablhoi globalni dorem


# q4
# `constructor baroi soxtani object va desructor baroi udalit kardani on 
# constructor meshavad new va init 
# dar onho self hamchun ssilkae ast ki parametrhoro mesozad va dar xotiri on megirad
# destructor boshad del


# q5
# `globalro hamai funcsiyaho dida metavonand
# localro funcsiyahoe ki bo on dar yak nested joygirand 
# va nonloclal boshad baroi on local nest va onro namebinad yane atributhoi yak funcsiya baroi digarash nonlocal ast`
