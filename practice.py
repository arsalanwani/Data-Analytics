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



students = {
    "1": {
        "Name": {
            "FirstName": "Ubaid",
            "LastName": "Khan"
        },
        "Address": {
            "State": "Kashmir",
            "Pincode": 190001
        }
    },

    "2": {
        "Name": {
            "FirstName": "Imaad",
            "LastName": "Bhat"
        },
        "Address": {
            "State": "Kupwara",
            "Pincode": 192121
        }
    }
}



# for i in students:
#     if i=="FirstName":
#         break
#     print(students)
    

for student in students.values():
    print(student["Name"]["FirstName"])
# students["1"]["Address"].pop("Pincode")
del students["1"]["Address"]["Pincode"] 
students["2"]["Address"]["State"]="srinagar"
print(students)              




for student in students.values():
    print(student["Name"]['FirstName'])


for id,student in students.items():
    if student =="2":
        continue
    print(student)    
    