'''
Variables -->Variables is basically named storage location that is used to hold data in
the memory,to make it simple it is the lebel which points out to a value --> storage placeholders

rules for defining variables
-->A-Z,a-z,0-9
-->start with uppercase,lowercase letters,even with a underscore _
-->but you cannot start with symbols (@,#,$....),even numbers also

Better preferable way is go with general purpose --> you want to store
your details name,email_id,accout_number...

'''
'''a=1
b=5
a=33
#Python is dynamically typed,you need not define the datatype and also
#only the recent value to the value to the variable with same name is pointed

print(a)
print(b)

#1a23 = 25 #Syntax Error

#@werf = 4.5 #Syntax Error

#$dsf = 12 #Invalid Syntax

#store your personal details

name = "Codegnan"
location = "Visakhapatnam"
email_id = "mdk@gmail.com"
age = "22"
print(name,location,age,email_id)

#How to assign multiple values to a variables
deekshith,sunny,vamsi = 22,21,22
print(deekshith)
print(sunny)
print(vamsi)

#assign same value to multiple variables

x = y = z = 21
print(x,y,z)

#keywords are reserved words which will have specific usage
#There are 35 keywords in python
#never use keywords as identifiers

#if = 23
#lamda = 'deekshith'
#False = #cannot assign

#python is case sensitive
false = 21

#Identifiers are names given to variables,functions,classes,objects...

#Literals are fixed values to a identifier
name=25
name =("deekshith")
#name is Identifier,25 is literal

#Built-in Identifiers,25 is literal

#Single line comments --> #
#Multi line comments -->  #start end with triple quotes
'''
#built-in Datatypes -->int,float,complex
#int -->count,values,quantities
#float -->temperature,percentage,price
#complex --> specific conversions (real and imaginary)
#implicit as python follows dynamic type
'''count = 40
print(count)
print(type(count))

price = 175.77
print(price)
print(type(price))

j3 = 30
value = 2+j3
print(value)
print(type(value))'''

 #Typecasting -->converting one type to anaother

#int -->float,complex

'''age=22
print(type(age))
b = float(age)
print(b)
print(type(b))
c = complex(age)
print(C)
print(type(c))'''

#float, complex

#boolean datatype -->validation--> true/false
'''a= True
print(a)
print(type(a))

#typeconversion of bool
b = int(a)
print(b)
c = float(a)
print(c)
d = complex(float(int(False)))
print(d)
print(type(d))'''


#Input -->input()/ output -->print()
'''a = 5
print(a)

a=input("enter the number")
print(a)
print(type(a))

a = int(input("enter the number")) #only integer input
print(a)
print(type(a))

b = float(input("enter the value"))
print(b)
print(type(b))
'''

#now lets work on a simple case study using -->fee caluculator

#details of the student
name = input("enter the student name:")
print("------------")
admission_fees = int(input("enter the admission_fees:"))
tution_fees = int(input("enter the tuition_fees:"))
hostel_fees = int(input("enter the hostel_fees:"))
total_fees = admission_fees + tution_fees + hostel_fees
print("----------------")
print("student name :",name)
print("admission fees is :",admission_fees)
print("tution fees is :",tution_fees)
print("hostel fees is :",hostel_fees)
print("total fees is =:",total_fees)
print("--------------")
























    




























      






















