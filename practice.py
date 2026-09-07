
# list stores multiple values in a single  variable its heterogenous(takes different data types in a list),it is ordered 
# indexing is a numerical location of an item in a list.
# it is mutable.



# print(lt)
# lt[1]='ayan' 

# lt.append('faheem')
# lt.insert(2,'seerat')
# lt.remove('ishan')
# lt.pop(0)
# print(lt)

# fruits = ["Apple","Mango","Banana","grapes","pear"]
# print(fruits[1])
# print(fruits[-1])
# fruits[2]="kiwi"
# print(fruits)
# fruits.append("orange")
# print(fruits)
# fruits.remove("Apple")
# print(fruits)
# print(len(fruits))
# fruits.append("kiwi")
# print(fruits)
# fruits.insert(2,"watermelon")
# print(fruits)
# fruits.insert(0,"cherry")
# print(fruits)
# fruits.insert(4,"papaya")
# print(fruits)
# fruits.remove("kiwi")
# print(fruits)
# fruits.remove("watermelon")
# fruits.remove("pear")
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.pop(1)
# print(fruits)
# removed_fruit= fruits.pop(1)
# print(removed_fruit)
# fruits.append("mango")
# print(fruits)
# fruits.remove("mango")
# print(fruits)
# fruits.insert(3,"kiwi")
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.remove('cherry')
# print(fruits)
# fruits.append('strawberry')
# print(fruits)
# fruits.insert(0,'guava')
# print(fruits)
# fruits.remove('grapes')
# print(fruits)




# lt=[['arsalan','muzammil','ayat','ishan','sabtain',2,4,6,8],["Apple","Mango","Banana","grapes","pear"]]
# lt[0].append('arsii')
# print(lt)



# lt=[['arsii','wasiq','wani'],[1,2,3],[True,False,9]]
# lt[0].append('ayan')
# lt[2].pop(2)
# lt[0][2]=('athar')
# print(lt)
# print(lt[0][1])
# lt = [["Ali","Sara"],["Apple","Mango"]]
# print(lt[0][1])
# lt[1].append('Banana')
# lt[0][0]='Arsalan'
# lt[1].pop(1)
# print(lt)
# lt = [
#     ["Ali","Sara","John"],
#     [10,20,30],
#     [True,False]
# ]
# lt[1][1]=25
# lt[1].append(40)
# lt[2].pop(1)
# print(lt[0][2])
# print(lt[2][0])
# # print(lt)
# lt = [
#     ['arsii','wasiq','wani'],
#     [10,20,30],
#     [True,False]
# ]

# [
#  ['Arsalan','Wasiq','Athar','Ayan'],
#  [10,20,30,40],
#  [True]
# ]
# lt[0][0]='Arsalan'
# lt[0][2]='Athar'
# lt[0].append("Ayan")
# lt[1].append(40)
# lt[2].pop(1)
# print(lt)+
# lt=[[['arsii','athar','wasiq'],[12,13,True]],
#     [['faheeem','ayan','iqra'],[31,76,False]],
#     [['falak','iq','nocki'],['t24','zhuis','spower']]]
# print(lt[2][0][0])
# lt[1][1][0]='arsiii'
# print(lt[1][1][0])
# lt[1][1].insert(1,'athar')
# lt[1][0].append('maryam')
# del (lt[0][1][2])
# print(lt[0])
# print(lt[1])



# dt={
#     "Name":{
#         "FirstName":"Arsalan",
#         "LastName":"wani"
#     },

#     "Address":{
#         "state":"kashmir",
#         "pincode":"192121"
#     }
# }
# dt["occuption"]= {"designation":"jr assistant","employ-code":"1903"}
# dt["Address"]["pincode"]="192122"
# del dt["Address"]["pincode"]
# # print(dt)
# print(dt["occuption"]["employ-code"])
# print(dt["Address"]["state"])


# student ={
#     "name":{
#         "firstname":"imaad",
#         "lastname":"bhat"
#     },
#     "address":{
#         "state":"kupwara",
#         "pincode":"192121"
#     },
#     "education":{
#         "course":"datascience",
#         "year":"2026"
#     }
# }



# students={
#     "1":{
#     "name":{
#         "firstname":"imaad",
#         "lastname":"bhat"
#         },

#     "address":{
#         "state":"kashmir",
#         "pincode":"192121"
#     }
#     },
#     "2":{
#         "name":{
#             "firstname":"ubaid",
#             "lastname":"khan"
#         },
#         "address":{
#             "state":"kashmir",
#             "pincode":"192121"
#         }

#     }
#         }
    
# print(students)
# print(students["1"]["address"]["pincode"])
# print(students["2"]["name"]["lastname"])





# grade = int(input("enter your number:-"))

# if grade == 98:
#     print("Topper")
# elif grade >= 50:
#     print("Good")
# elif grade >= 30:
#     print("Average")  
# else:
#     print("Fail");




# age = int(input("enter your age :- "))


# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are a minor👶👶")







# x=int(input("enter 1st number "))
# y=int(input("enter 2nd number "))
# z=int(input("enter 3rd number "))

# if x>y and x>z:
#     print(x," is greater ")
# elif y>x and y>z:
#     print(y," is greater ") 
# else:
#     print(z," is greater ")   
     

# num = int(input("enter your number"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")    


# num = int(input("enter your number "))
# if num > 0:
#     print("positive")
# elif num ==0:
#     print("neutral")    
# else:
#     print("negative")    




# username = input("enter your username ")
# password = input("enter your password ")
# if username =="Arsii":
#     if password =="1234":
#         print("login successful")
#     else:
#         print("wrong password")    
# else:
#     print("wrong username")


# try:
#     num1=int(input("enter the first number"))
#     num2=int(input("enter the second number"))
#     operation=input("what operation do you want to do")
#     if operation=="add":
#         print(num1+num2)
#     elif operation== "minus":
#         print(num1-num2)
#     elif operation=="division":
#         print(num1/num2)
#     elif operation=="multiplication":
#         print(num1*num2)   
#     else:
#         print("invalid operation")
# except ZeroDivisionError:
#     print("can't divide by zero")        


# boy = int(input("enter the boy's age :- "))
# girl = int(input("enter the girl's age :- "))

# if boy>=18 and girl >=18:
#     print("eligible")
# else:
#     print("Not eligible")
    
# boy = int(input("enter the boy's age :- "))
# girl = int(input("enter the girl's age :- "))

# if boy>=18 or girl >=18:
#     print("eligible")
# else:
#     print("Not eligible")
    

# try:
#     n1=int(input("enter the 1st number :-  "))
#     op = input("+,-,/,*  :- ")
#     n2=int(input("enter the 2nd number :-   "))
#     if op == "+":
#         print(n1+n2)
#     elif op == "-":
#         print(n1-n2)  
#     elif op == "/":
#         print("n1/n2")    
#     elif op == "*":
#         print(n1*n2)  
#     else:
#         print("invalid operation")   
# except ZeroDivisionError:
#     print("can't divide by zero")           


# for i in range(1,21,2):
#     print(i)
# for i in range(2,21,2):
#     print(i)

# table = int(input("enter the number for table :- "))
# for i in range(1,11):
#     x=table*i
#     print(table,"x",i,"=",x)




# res = int(input("Enter the number :- "))
# for i in range(1,11):
#     num=res*i
#     print(res,"x",i,"=",num)



# for i in range(1):
#     print("i am arsalan")

# for i in range(2,21):
#     if i%2==0:
#         print(i)



# for i in range(21):
#     if i ==3:
#         break
#     print(i)




# for i in range(21):
#     if i ==11:
#         continue
#     print(i) 




# for i in range(20):
#     if i%2 == 0:
#         print(i,"is even")
#     else:
#         print(i,"is odd")







# name="arsalan"
# age=23
# height=173.2
# is_student=True
# city="srinagar"
# print(name,age,height,is_student,city)



# i=25
# j=25.5
# print(type(j))
# print(type(True))



# num="100"
# num=int(num)
# print(type(num))




# fruits = ["Apple", "Mango", "Banana", "Grapes", "Pear"]
# print(fruits[0])
# print(fruits[-1])
# print(fruits[2])
# fruits[2]="Orange"
# fruits.append("kiwi")
# fruits.insert(1,"cherry")
# fruits.remove("Mango")
# fruits.pop()
# print(fruits)


# marks = (90, 85, 78, 90, 95, 90)
# print(marks[0])
# print(marks[-1])
# print(marks.count(90))
# print(marks.index(78))


# numbers = {1, 2, 2, 3, 3, 4}
# print(numbers)

# fruits = {"Apple", "Mango", "Banana"}
# # add() to add "Orange"
# fruits.add("orange")


# # update() to add "Kiwi" and "Cherry"
# fruits.update(["kiwi"],["cherry"])
# # remove() to remove "Apple"
# fruits.remove("Apple")
# # discard() to remove "Mango"
# fruits.discard("Mango")

# print(fruits)



# student = {
#     "Name": "Arsalan",
#     "Age": 23,
#     "City": "Srinagar"
# }
# print(student["Name"])
# print(student["Age"])
# student["course"]="Data Science"
# student["Age"]=24
# del student["City"]
# student.update({"country":"india"})
# print(student.keys())
# print(student.values())
# print(student.items())
# student.pop("Age")
# print(student)




# lt = [
#     ["Arsalan", "Wasiq", "Ayat"],
#     [10, 20, 30],
#     [True, False, True]
# ]
# Arsalan
# Ayat
# 20
# False

# print(lt[0][0])
# print(lt[0][2])
# print(lt[1][1])
# print(lt[2][1])
# lt[0].append("Ayan")
# lt[1].pop()
# lt[0][1]="umer"
# print(lt)


# Name
#  ├── FirstName → Ubaid
#  └── LastName → Khan

# Address
#  ├── State → Kashmir
#  └── Pincode → 190001


# student={
#  "name":{
#   "firstname":"ubaid"
#   "lastname":"khan"
#   },
#   "address":{
#   "state":"kashmir"
#   "pincode":"192121"
#     }
# }



# student = {
#     "name":{
#         "firstname":"ubaid",
#         "lastname":"khan"
#     },
#     "Address":{
#         "state":"kashmir",
#         "pincode":192121
#     }
# }
# print(student["name"]["firstname"])
# student["name"]["firstname"]="ayat"
# print(student)
# student["Address"]["state"]="srinagar"
# print(student["Address"]["state"])
# student["occupation"]={
#     "designation":"data analyst",
#     "salary":50000
# }
# print(student)


# fruits = ["Apple", "Mango", "Banana", "Grapes", "Pear"]
 
    
# for i in fruits:
#     if i=="Banana":
#         continue
#     print(i)

# for i in fruits:
#     if i=="Banana":
#         break
#     print(i)



# students = {
#     "1": {
#         "Name": {
#             "FirstName": "Ubaid",
#             "LastName": "Khan"
#         },
#         "Address": {
#             "State": "Kashmir",
#             "Pincode": 190001
#         }
#     },

#     "2": {
#         "Name": {
#             "FirstName": "Imaad",
#             "LastName": "Bhat"
#         },
#         "Address": {
#             "State": "Kupwara",
#             "Pincode": 192121
#         }
#     }
# }



# for i in students:
#     if i=="FirstName":
#         break
#     print(students)
    

# for student in students.values():
#     print(student["Name"]["FirstName"])
# # students["1"]["Address"].pop("Pincode")
# del students["1"]["Address"]["Pincode"] 
# students["2"]["Address"]["State"]="srinagar"
# print(students)              




# for student in students.values():
#     print(student["Name"]['FirstName'])


# for id,student in students.items():
#     if student =="2":
#         continue
#     print(student)    
    








# fruits = ["Apple", "Mango", "Banana", "Grapes", "Pear"]
# for fruit in fruits:
#     print(fruit)


# name = "Arsalan"  
# for i in name:
#     print(i)  





# for i in range(10,41,10):
#     print(i)


# fruits = ["Apple", "Mango", "Banana"]
# for fruit in fruits:
#     print("I like",fruit)


# numbers = [10, 20, 30]

# for number in numbers:
#     print(number,type(number))

# students = {
#     "Name": "Arsalan",
#     "Age": 23,
#     "City": "Srinagar"
# }

# for student in students:
#     print(student)
# for student in students.values():
#     print(student)
# for student,stu in students.items():
#     print(student,":",stu)    


# students = {
#     "1": "Ubaid",
#     "2": "Imaad",
#     "3": "Ayat"
# }

# for student in students.values():
#     print(student)

# for student,stu in students.items():
#     print(student,stu)    




# numbers = [1, 2, 3, 4, 5]


# for number in numbers:
#     if number == 3:
#         break
#     print(number)


# fruits = ["Apple", "Mango", "Banana", "Grapes"]
# for fruit in fruits:
#     if fruit =="Banana":
#         break
#     print(fruit)



# names = ["Ali", "Wasiq", "Arsalan", "Ayat"]    
# for name in names:
#     if "Arsalan" == name:
#         print("found")
#         break

# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     print(number)

#     if number == 30:
#         break



# numbers = [10, 20, 30, 40, 50]
# for number in numbers:
#     if number == 30:
#         continue
#     print(number)

# fruits = ["Apple", "Mango", "Banana", "Grapes"]
# for fruit in fruits:
#     if fruit =="Mango":
#         continue
#     print(fruit)
# names = ["Ubaid", "Imaad", "Arsalan", "Ayat"]    
# for name in names:
#     if name =="Arsalan":
#         continue
#     print(name)

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     if number == 3:
#         continue
#     print(number)


# fruits = ["Apple", "Mango", "Banana", "Grapes", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     if fruit =="Banana":
#         break
# numbers = [10, 20, 30, 40, 50, 60]
# for i in numbers:
#     if i ==30:
#         continue
#     elif i == 50:
#         break
#     print(i)



# names = ["Ubaid", "Imaad", "Ayat", "Arsalan", "Wasiq"]


# for name in names:
#     if name == "Imaad":
#         continue
#     elif name == "Arsalan":
#         break
#     print(name)


# student = {
#     "Name": "Arsalan",
#     "Age": 23,
#     "City": "Srinagar",
#     "Course": "Data Science"
# }


# for stu,stud in student.items():
#     if stu == "Age":
#         continue
#     print(stu,stud)







students={
    "1":{
        "Name":{
            "FirstName":"Ubaid",
            "LastName":"Khan"
        },
        "Address":{
            "state":"Kashmir",
            "Pincode":192121
        }
    },

    "2":{
        "Name":{
            "FirstName":"Imaad",
            "LastName":"Bhat"
        },
        "Address":{
            "state":"kupwara",
            "Pincode":190001
        }
    },

    "3":{
        "Name":{
            "FirstName":"Ayat",
            "LastName":"wani"
        },
        "Address":{
            "state":"srinagar",
            "pincode":190002
        }
    }
}    



# for id,student in students.items():
    # if id == "2":
    #     continue
    # if id =="3":
    #     break
#     print(student["Name"]["FirstName"])
# for id,student in students.items():
#     print(student["Name"]["FirstName"])


# for student in students:
#     if student == "2":
#         continue
#     print(student)



# for student in students:
#     if student == "3":
#         break
#     print(student)





# for key,value in students.items():
#     if key == "2":
#         continue
#     elif key =="3":
#         break
#     print(value["Name"]["FirstName"])





# num = int(input("enter any number:- "))
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime") 



# x=int(input("enter any number:- "))
# if x<=1:
#     print("not prime")
# else:
#     for i in range(2,x):
#         if x%i ==0:
#             print("not prime")
#             break
#     else:
#         print("prime")    


# lt =[23,34,45,56,67,78,89]
# x = int(input("enter any number"))
# flag =0
# for num in lt:
#     if x == num:
#         flag=1
# if flag ==1:
#     print(x,"is in a list")  
# else:
#     print(x,"not in a list")   
# 
# 
# 
# 
# 
# 
# x=int(input("enter any number :- "))
# if x<=1:
#     print("not prime")
# else:
#     for i in range(2,x):
#         if x%i ==0:
#             print("not prime")
#             break
#     else:
#             print("prime")
           


# lt =[23,34,45,56,67,78,89,90,01.12]
# x=int(input("enter any number :-"))
# flag =0
# for num in lt:
#     if num ==x:
#         flag=1
# if flag ==1:
#     print(x,"is in a list")
# else:
#     print(x,"is not in a list")

# numbers = [12, 25, 37, 48, 59, 64, 75]
# x = int(input("enter any number  :- "))
# flag =0
# for num in numbers:
#     if num ==x:
#         flag =1
# if flag == 1:
#     print("number found")
# else:
#     print("number not found")



# names = ["Ali", "Wasiq", "Imaad", "Arsalan", "Ayat"]
# x= input("enter any name:-")
# flag =0
# for name in names:
#     if x==name:
#         flag =1
#         break
# if flag ==1:
#     print(x,"is in a list")
# else:
#     print(x,"is not in a list")


# numbers = [10, 20, 30, 40, 50, 60]
# for i in numbers:
#     if i == 30:
#         continue
#     elif i == 50:
#         break
#     print(i)

# numbers = [11, 12, 13, 14, 15, 16, 17, 18]
# for i in numbers:
#     if i%2==0:
#         continue
#     print(i)



# word=input("enter a word:-")
# rev=""
# for ch in word:
#     # rev=ch+rev
#     rev=ch+rev
# if word==rev:
#     print(word,"is palindrome")
# else:
#     print(word,"is not palindrome")



    






# x=input("enter a word:-  ")
# st=''
# for ch in x:
#     st=ch+st
# if x==st:
#     print(x,"is palindrome")
# else:
#     print(x,"is not palindrome")



# Write a Python program that takes a word from the user and counts how many times each character appears in the word.


# user=input("enter a word:-")
# x={}
# for i in user:
#     if i in x:
#         x[i]=x[i]+1
#     else:
#         x[i]=1
# print(x)


# word=input("Enter the senstence:-")
# word.split()
# print(len(word.split()))


# lt=[12,23,34,45,67,78,89,90]
# lt.sort(reverse=True)
# print(lt[4])



# i=0
# while i <=30:
#     i=int(input("enter any number:- "))
#     print(i)


# i=int(input("number :- "))
# while True:
#     if i%2==0:
#         print("even")
#         break
#     else:
#         print("odd")
#         break
        
 
# try:
#     lt =[12,34,56]
#     print(lt[3])
# except IndexError:
#     print("index isn't in the list")


# try:
#     print(arsalan)
# except NameError:
#     print("arsalan is not defined")

# try:
#     dt={
#         "name":"arsalan"
#     }
#     print(dt["email"])
# except KeyError:
#     print("key not found")


# try:
#     name="arsalan"
#     name.append(20)
#     print(name)
# except AttributeError:
#     print("cannot use this method")    


# try:
#     a=10  
#     n=a/0
#     print(n)
# except ZeroDivisionError:
#     print("can't divide by zero")


# try:
#     age=int("hello")
#     print("age")
# except ValueError:
#     print("value error")



# i=1
# while i<=5:
#     print(i)
#     i+=1



# i=5
# while i<=5:
#     if i==0:
#         break
#     print(i)
#     i=i-1



# i=2
# while  i%2==0:
#     if i >20:
#         break
#     print(i)
#     i= i+2

# u=1
# i=int(input("enter the number :- "))
# while u<=i:
#     print(u)
#     u=u+1

# while True:
#     i=int(input("enter a number ;- "))
#     if i == 0:
#         break
#     print("you entered",i)



# while True:
#     i=int(input("Enter the Number:-"))
#     if i==0:
#         break
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")
   
# i=1 
# while i<=10:
#     if i == 5:
#         i=i+1
#         continue
#     print(i)
#     i=i+1


# numbers = [10, 20, 30, 40, 50]
# flag=0
# i=int(input("Enter the Number"))
# if i in numbers:
#     flag=1
# else:
#     print(i,"is not in the list")
# if flag ==1:
#     print(i,"is in the list")



# total = 0

# while True:
#     i = int(input("Enter the number: "))

#     if i == 0:
#         break

#     total = total + i

# print("Total =", total)


# while True:
#     x=int(input("enter the number :- "))
#     if x==0:
#         break
#     elif x < 0:
#         continue
#     # if x%2 ==0:
#     #     print("even")
#     # else:
#     #     print("odd")
#     print("even" if x%2==0 else "odd")

# from practice2 import even_odd

# x=int(input("enter a number"))
# even_odd(x)

# def hello():
#     print("hello")
# hello()
# def greet(name):
#     print("Hello",name)
# greet("arsalan")



# def square(x):
#     print(x*x)
# x=int(input("enter any number:-"))
# square(x)

# def sum(a,b):
#     print(a+b)
# sum(10,20)
# sum(5,7)

# def mul(a,b):
#     print(a*b)
# mul(2,7)
# mul(3,8)


# def check_number(x):
#     if x>0:
#         print("positive")
#     else:
#         print("negative")
# # x=int(input("enter any number:-"))
# check_number(10)
# check_number(-5)


# def greater(a,b):
#     if a>b:
#         print(a,"is greater")
#     else:
#         print(b,"is greater")
# a=int(input("enter any number:-"))
# b=int(input("enter any number:-"))
# greater(a,b)

# def calculator(a,b,operator):
#     if operator == "+":
#         print(a+b)
#     elif operator =="*":
#         print(a*b)
#     elif operator=="-":
#          print(a-b)

# calculator(10,20,"-")


# lt=[2,3,4,5]
# sq=list(map(lambda x:x*x,lt))
# print(sq)
# print(type(sq))



# add=lambda x,y:x+y
# print(add(10,20))


# even_odd=lambda x:"even" if x%2==0 else "odd"
# print(even_odd(2))

# lt=["1","2","3","4","5"]
# sq=list(map(int,lt))
# print(sq)

 
# names=["ARSALAN","ATHAR","WASIQ","EESHAAN","MUZZAMIL"]
# name=list(map(lambda x:x.lower(),names))
# print(name)

# sq=['arsalan', 'athar', 'wasiq', 'eeshaan', 'muzzamil']
# sqq=list(map(lambda x:x.upper(),sq))
# print(sq)

# q=['arsalan', 'athar', 'wasiq', 'eeshaan', 'muzzamil']
# n=list(map(str.capitalize,q))
# print(n)


# listt=[1,2,3,4,5,-3,-4,-5,-6,-7]
# n=list(filter(lambda x:x<0,listt))
# print(n)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sq=list(filter(lambda x:x%2==0,numbers))
# print(sq)

# numbers = [-5, 3, -2, 8, -1, 10, -7, 4]
# sq=list(filter(lambda x:x>0,numbers))
# print(sq)

# numbers = [2, 7, 4, 9, 1, 6, 3, 10]
# sq=list(filter(lambda x:x>5,numbers))
# print(sq)

# words = ["cat", "apple", "dog", "banana", "sun", "mango"]
# sq=list(filter(lambda x:len(x)>4,words))
# print(sq)

# numbers = [3, 7, 9, 12, 14, 15, 20, 21, 25]
# sq=list(filter(lambda x:x%3==0,numbers))
# print(sq)


# file=open('file.txt','w')
# file.write('i am arsalan')
# file.close()


# file=open('file.txt','r')
# f=file.read()
# print(f)



# file=open('file.txt','a')
# file.write(' i am data analyst')
# file.close()


# file=open('file.txt','x')
# file.write()
# file.close()

# f = open('fil.txt','x')
# f.close()


# files=open(r'C:\Users\Arsalan Wani\OneDrive\Desktop\sick\arsii.txt','w')
# files.write("hello")
# files.close()


# with open('arsii.txt','w') as f:
#     f.write("60053737")

# file = open('ayan.txt','x')
# file.write("dbhdshnv")
# file.close()



# i=int(input("enter a number :- "))
# if i > 0:
#     print("positive")
# else:
#     print("Negative")

# i=int(input("enter any number:-"))
# if i%2==0:
#     print("even")
# else:
#     print("odd")


# i=int(input("enter ist number :- "))
# j=int(input("enter 2nd number :- "))
# if i>j:
#     print(i,"is greater")
# else:
#     print(j,"is greater")


# marks=int(input("enter any number:-"))
# if marks >= 90:
#     print("A GRADE")
# elif marks >=75:
#     print("B GRADE") 
# elif marks >=60:
#     print("C GRADE")
# else:
#     print("D GRADE")



# num1 = int(input("enter 1st number :- "))
# num2=  int(input("enter 2nd number :- "))
# operator = input("enter any operator :- ")
# if operator == "+":
#     print(num1+num2)
# elif operator == "/":
#     print(num1/num2)
# elif operator =="*":
#     print(num1*num2)
# elif operator =="-":
#     print(num1-num2)
# elif operator =="%":
#     print(num1%num2)
# else:
#     print("invalid operation")


# fruits = ["Apple", "Mango", "Banana", "Grapes", "Pear"]
# print(fruits[0])
# print(fruits[2])
# print(fruits[4])
# fruits[2]="orange"
# print(fruits[2])

# fruits = ["Apple", "Mango", "Banana"]
# fruits.append("kiwi")
# print(fruits)
# fruits.insert(1,"orange")
# fruits.pop(2)
# fruits.remove("Mango")
# print(fruits)


# numbers = (10, 20, 30, 40, 50)
# print(numbers[0])
# print(numbers[2])
# print(numbers[4])



# set={"Apple", "Mango", "Banana", "Apple", "Mango"}
# print(set)

# fruits = {"Apple", "Mango", "Banana"}
# fruits.add("Grapes")
# fruits.update(["kiwi","cherry"])
# print(fruits)

# numbers = {10, 20, 30, 40}
# numbers.remove(20)
# numbers.discard(100)
# print(numbers)


# student ={
#     "Name":"Arsalan",
#     "Age":24,
#     "City":"Pulwama"
# }

# student["Age"]=23
# student["City"]="Delhi"
# student["Course"]="Data Analytics"
# rv=student.pop("Age")
# print(rv)
# student = {
#     "Name": "Arsalan",
#     "Age": 22,
#     "Course": "Data Analytics"
# }
# for key,value in student.items():
#     print(key,value)
# lt = [
#     ["Arsalan", "Wasiq", "Ayat"],
#     [10, 20, 30],
#     [True, False, True]
# ]
# print(lt[0][1])
# print(lt[1][1])
# print(lt[2][1])


# lt[0][2]="ishaan"
# lt[1][1]=25
# print(lt)


# lt = [
#     ["Ali", "Wasiq"],
#     [10, 20]
# ]
# lt[0].append("Arsalan")
# print(lt)

# student = {
#     "Name": {
#         "FirstName": "Arsalan",
#         "LastName": "Wani"
#     },
#     "Address": {
#         "State": "Kashmir",
#         "Pincode": 190001
#     }
# }
# print(student["Name"]["FirstName"])
# print(student["Address"]["State"])
# print(student["Address"]["Pincode"])


# student["Name"]["FirstName"]="Ayat"
# del student ["Address"]["Pincode"]
# student["Address"]["Country"]="India"
# print(student)


# numbers = [10, 20, 30, 40, 50]
# for i in numbers:
#     print(i)

# numbers = [11, 12, 13, 14, 15, 16, 17, 18]
# for i in numbers:
#     if i%2==0:
#         print(i)
# numbers = [10, 20, 30, 40, 50, 60]
# for i in numbers:
#     if i == 30:
#         continue
#     print(i)


# numbers = [10, 20, 30, 40, 50, 60]
# for i in numbers:
#     if i == 50:
#         break
#     print(i)


# numbers = [23, 34, 45, 56, 67, 78, 89]
# flag=0
# h=int(input("enter a number :- "))
# for i in numbers:
#     if i == h:
#         flag=1
#         break

# if flag ==1:
#     print("exists")
# else:
#     print("doesnt exist")

# i =1
# while i<=5:
#     print(i)
#     i=i+1
# i =5
# while i>=1:
#     print(i)
#     i=i-1

# while True:
#     i=int(input("enter a numbers:-"))
#     if i ==0:
#         break
#     print(i)


# while True:
#     i=int(input("enter a number:-"))
#     if i==0:
#         break
#     elif i%2==0:
#         print("even")
#     else:
#         print("odd")


# total=0
# while True:
#     i= int(input("enter a number:-"))
#     if  i ==0:
#         break
#     total=total+i
# print(total)


# def hello():
#     print("hello")
# for i in range(3):
#     hello()

# def square():
#     x=int(input("enter a number:-"))
#     x=x*x
#     print(x)
# square()

# def even_odd(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")
# x=int(input("enter a number:-"))
# even_odd(x)

# numbers = [1, 2, 3, 4, 5]

# sq=list(map(lambda x:x*x,numbers))
# print(sq)

# numbers = [10, 15, 20, 25, 30, 35, 40]
# g=list(filter(lambda x:x>20,numbers))
# print(g)



# with open("arsii.txt",'x'):
#     print("file created")


# with open('arsii.txt','w') as file:
#     file.write("arsalan")
#     file.write("\ndata analytics")


# with open('arsii.txt','r') as file:
#     data=file.read()
#     print(data)

# with open('arsii.txt','a') as file:
#     file.write('\npython')

# import os 
# os.remove('arsii.txt')



# class ils:
#     def greet(self):
#         print("hello from ils")
#     def bye(self,a,b):
#         print(a+b)
#         print("bye from ils")

# i=ils()
# i.greet()
# i.bye(12,13)



# polymorphism is same functions different behaviour
# class animal:
#     def bark(self):
#         print("bow bow")
#     def cat(self):
#         print("meow meow")

# i=animal()
# i.bark()
# i.cat()

# # inheritance means when child class inherits parent class features
# class animal:
#     def bark(self):
#         print("meow meow")
# class animal:
#     def cat(animal):
#         print("meow meow")
# i=animal()
# i.bark()
# i.cat()


# class ils:
#     def __init__(self):
#         print("hello i am from constructor")
#         self.__bye()
#     def hello(self):
#         print("Hello from ils")
    
#     def _ok(self):
#         print("Hello from protected function")
    
#     def __bye(self):
#         print("This is private function!")
    

# i = ils()
# i.hello()
# i._ok()

# numbers = [12, -3, 0, 25, -7, 18, 25, 4, 0, 9, -1, 18]
# num=list(filter(lambda x:x>0,numbers))
# print(num)


# numbers = [12, -3, 0, 25, -7, 18, 25, 4, 0, 9, -1, 18]
# for num in numbers:
#     if num <0:
#         num.count
#         print(num.count())
#     else:
#         continue


# numbers = [4, 9, 12, 3, 15]
# for num in numbers:
#     if num > 10:
#         print(num)
#     else:
#         continue

# numbers = [4, 9, 12, 3, 15]
# count =0
# for n in numbers:
#     if n >10:
#         count = count +1
# print(count)


# x=int(input("enter a number :- "))
# x2=int(input("enter a number :- "))
# operator=input("enter an operator:- (+,-,*,/)")
# if operator == "+":
#     print(x+x2)
# elif operator == "-":
#     print(x-x2)
# elif operator == "*":
#     print(x*x2)
# elif operator == "/":
#     print(x/x2)
# else:
#     print("invalid operation")    



# Create a list of 10 numbers and print the first, last, and middle elements.
# num=[1,23,34,45,56,67,78,89,90,10]
# print(num[0])
# print(num[-1])
# print(num[4])
# Find the largest number in a list without using max().
# num=[1,23,34,45,56,67,78,89,90,10]
# largest = num[0]
# for n in num:
#     if n > largest:
#         largest =n
# print(largest)
# Find the smallest number in a list without using min().
# num=[1,23,34,45,56,67,78,89,90,10]
# smallest = num[0]
# for n in num:
#     if n < smallest:
#         smallest =n
# print(smallest)

# Count how many even and odd numbers are in a list.

# num=[1,23,34,45,56,67,78,89,90,10]
# even_count =0
# odd_count=0
# for n in num:
#     if n % 2==0:
#         even_count=even_count +1
#     else:
#         odd_count=odd_count +1
# print("even numbers",even_count)
# print("odd numbers",odd_count)
# Search for a number in a list using a flag variable and break.
# num=[1,23,34,45,56,67,78,89,90,10]
# flag =0
# x=int(input("enter a numbers:-"))
# if x in num:
#     flag =1
# if flag ==1:
#     print(x,"is in a list")
# else:
#     print(x,"is not in a list")


# Create a tuple of numbers and find its length and maximum value.
# tp=(1,23,45,56,67,78)
# print(len(tp))
# print(max(tp))
# Convert a tuple into a list, add an element, and convert it back to a tuple.
# tp=(1,23,45,56,67,78)
# my_list=list(tp)
# my_list.append(43)
# tp=tuple(my_list)
# print(tp)
# # Create two sets and find their union, intersection, and difference.
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print("union",set1.union(set2))
# print("intersection",set1.intersection(set2))
# print("difference",set1.difference(set2))
# # Given a list with duplicate values, use a set to remove duplicates.
# numbers = [10, 20, 10, 30, 20, 40, 30]
# un=set(numbers)
# print(un)
# Check whether a particular element exists in a set.
# numbers = {10, 20, 30, 40, 50}
# x=int(input("enter a number:-"))
# if x in numbers:
#     print(x,"is in a set")
# else:
#     print(x,"is not in a set")    


# Create a dictionary containing a student's name, age, marks, and city and print each value.
# dt={
#     "name":"arsalan",
#     "age":24,
#     "marks":100,
#     "city":"pulwama"
#     }
# print(dt["name"])
# print(dt["age"])
# print(dt["marks"])
# print(dt["city"])
# Loop through a dictionary and print all keys and values.
# dt={
#     "name":"arsalan",
#     "age":24,
#     "marks":100,
#     "city":"pulwama"
#     }
# for keys,values in dt.items():
#     print(keys,values)
# Find the student with the highest marks from:
# students = {
#     "Arsalan": 85,
#     "Wasiq": 92,
#     "Aman": 78,
#     "Rahul": 88
# }
# for keys,values in students.items():
#     print(max(students.items()))
#     break
# Count the frequency of each character in a word using a dictionary.
# x=(input("enter a word:-"))
# frequency={}
# for ch in x:
#     if ch in frequency:
#         frequency[ch]=frequency[ch]+1
#     else:
#         frequency[ch]=1
# print(frequency)


# Print numbers from 1 to 50 using a for loop.
# for i in range(1,51):
#     print(i)
# # # Print numbers from 1 to 20 but skip multiples of 3 using continue.
# for i in range (1,20):
#     if i%3==0:
#         continue
#     print(i)
# # Print numbers from 1 to 100 and stop when you reach 57 using break.
# for i in range(1,101):
#     if i == 57:
#         break
#     print(i)
# Take numbers from the user continuously using while and stop when the user enters 0.
# while True:
#     x=int(input("enter a number:-"))
#     if x==0:
        # break
# # Take numbers from the user and keep printing whether each is even or odd until 0 is entered.
# while True:
#     x=int(input("enter a number:-"))
#     if x==0:
#         break
#     elif x%2==0:
#         print(x,"is even")
#     else:
#         print(x,"is odd")
        
# 1. Create a function hello() that prints "Hello Python".
# def hello():
#     print("Hello Python")
# hello()
# # 2. Create a function that prints your name.
# def name(name="arsalan"):
#     print("Hello",name)
# name()
# # 3. Create a function that prints your name and age.
# def nage(name="Arsalan",age=24):
#     print("my name is",name,"and my age is",age)
# nage()
# # 4. Create a function welcome() that prints "Welcome to Data Analytics".
# def welcome(DA="Data Analytics"):
#     print("welcome to",DA)
# welcome()
# # 5. Create a function that prints numbers from 1 to 10.
# def numbers():
#     for i in range(1,11):
#         print(i)
# numbers()
# # 6. Create a function that prints "Even".
# def even(x):
#     x=int(input("enter any number:-"))
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")
# even(2)
# # 7. Create a function that prints "Python is easy" five times.
# def py():
#     print("Pyhton is easy")
# py()
# py()
# py()
# py()
# py()
# Create a function that accepts a number and prints the number.
# def num(x):
#     print(x)
# num(2)
# 10. Create a function that accepts two numbers and prints them.
# def num(x,y):
#     print(x,y)
# num(2,3)
# 11. Create a function that accepts name and age and prints both.
# def nage(name="Arsalan",age=24):
#     print("my name is",name,"and my age is",age)
# 12 Create a function that accepts city and prints it.
# def city(city="srinagar"):
#     print("i live in",city)
# city()
# 13.create a function that accepts marks and prints them.
# def marks(x):
#     print(x)
# marks(100)
# 14. Create a function that accepts a number and prints whether it is positive or negative.
# def pos_neg(x):
#     if x>0:
#         print("positive")
#     elif x==0:
#         print("neutral")
#     else:
#         print("negative")
# pos_neg(-1)

# 15. Create a function that accepts a number and prints whether it is even or odd.
# def even(x):
#     x=int(input("enter any number:-"))
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")
# even(3)
# 16. Function that returns a number's square.
# def square():
#     x=int(input("enter a number:-"))
#     return x*x
# result=square()
# print(result)
# 17. Function that returns a number's cube.
# def cube():
#     x=int(input("enter a number:-"))
#     return x**3
# result=cube()
# print(result)
# 18. Function that returns double of a number.
# def double():
#     x=int(input("enter a number:-"))
#     return x + x
# result=double()
# print(result)
# 19. Function that returns half of a number.
# def half():
#     x=int(input("enter a number:-"))
#     return x/2
# result=half()
# print(result)
# 20. Function that returns the sum of two numbers.
# def sum():
#     x=int(input("enter a number:-"))
#     y=int(input("enter a number:-"))
#     return x+y
# result=sum()
# print(result)
# def sum(x,y):
#     return x+y
# result=sum(10,20)
# print(result)
# 21. Function that returns the difference of two numbers.
# def minus():
#     x=int(input("enter a number:-"))
#     y=int(input("enter a number:-"))
#     return x-y
# result=minus()
# print(result)
# def minus(x,y):
#     return x-y
# result=minus(10,20)
# print(result)
# 22. Function that returns the product of two numbers.
# def product():
#     x=int(input("enter a number:-"))
#     y=int(input("enter a number:-"))
#     return x,y,x*y
# x,y,result=product()
# print("The product of",x,"and",y,"is",result)
# 23. Function that returns the division of two numbers.
# def division():
#     x=int(input("enter a number:-"))
#     y=int(input("enter a number:-"))
#     return x/y,x,y
# result,x,y=division()
# print("The division of",x,"and",y,"is",result)
# 24. Function that returns the remainder of two numbers.
# def remainder():
#     x=int(input("enter a number:-"))
#     y=int(input("enter a number:-"))
#     return x%y,x,y
# result,x,y=remainder()
# print("The remainder of",x,"and",y,"is",result)
# 25. Function that returns the average of two numbers.
# def average():
#     x=int(input("enter a number:-"))
#     y=int(input("enter a number:-"))
#     return (x+y)/2,x,y
# result,x,y=average()
# print("The average of",x,"and",y,"is",result)
