#operators
#different type of operators
#Conditional Statements -->if,elif,else,
"""
#Operators --> An operators is a symbol that performs an operation on one or more values
(operands) and produces a result

operators are primarily used :
-->caluculate values
-->compare values
-->make decisions
-->control the program flow

There are major seven categories of operators in python

-->Arthimetic operators
-->Assignment operators
-->Comparision operators
-->Membership operators(in,not in)
-->Identity operators(is,is,not)
-->Bitwise operators
-->Logical operators (and,or,not)
"""


#Arthimetic operators -->Arthimetic operators perform mathematical operators

#+-->Addition,- -->Substraction,* -->multiplication,/ -->division
# ** -->Exponent,% -->Modulus,//--> Interger division
"""
a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #returns the result in float values
print(a**b) #returns the exponential values

print(a % b)#Modulus division -->returns remainder
print(a // b) #Flooring / Integer dvision -->returns quotient discards floats
"""
'''
num1 = int(input("enter the first value:",))
num2 = float(input("enter the secondvalue:",))
result = (num1 + num2)*4
print("the result is",result) #standard notation

#f-string notation
print(f'the result is {result}')
print(f'the result of {num1} and {num2} is {result},{num1/num2}')
'''

#Assignment operators
#--> = Assign, += Addition assignment,
#-= -->substract assignment,*=,/=,%=,//,**=

#they are majorly used for code repetations in applications usage
'''
a = 4
b = 3
a +=2
print(a)
b += a
print(b)

#in similar work

b -= 3
print(b)
print(f' the updated values of a and b are {a} and {b}')
b *=a
print(b)
'''

#relational or comparision operators --> they always return the boolean
#values (true/false)

# == is equal to, !=not equal to
# < less than,> greater than ,>=,<=
'''
a  = int(input("enter the value:"))
b = int(input("enter the another value:"))
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
'''
#Membership operators -->They check for the existance of an object in a
#collection -->in,not in
'''
a = "deekshith"
print(type(a))
print('i' in a )
print('w' in 'deekshith')
print('w' not in 'deekshith')

b =[12,3,3,4]
c = int(input("enter the value"))
print(c in b)
print(c not in b)
'''

#Logical operators -->They are used to combine multiple conditons
#and,or,not
'''
age = int(input("enter the number"))
vote_right =  True

print(age>=18 and vote_right)
print(age<=18 or vote_right)
print(not vote_right)
'''
#IDENTITY OPERATORS -->ArithmeticError THEY CHECK THE MEMORY LOCATION AND VALIDATE
#WE USE #(ID) FUNCTION IT IS DIFFERENT FORM ==OPERATOR -> IS,IS,NOT

'''
a = [1,2,3]
b = [1,2,4]
print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

c = b
print(c)
print(id(c))
print(c is b)
'''

#BITWISE OPERATORS -->BITWISE AND &,BITWISE OR | PERFORM BITWISE OPERATORS
#WE GET THE RESULT (REMEMBER THE BINARY CONVERSION
print(5&3)
print(bin(5)) #returns binary number

















































































    
      


















































































