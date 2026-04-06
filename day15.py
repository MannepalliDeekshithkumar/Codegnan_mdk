'''functions()
-------------

---> this is a block of code which is reusabale.

---> two types 1. Built-in or In-build
               2. User define

1.Built-in or in-build
----------------------
--->They comes with program and those are already defined...
eg..
------   print(), sum(), map().......

2.User define
-------------
---> this is created by person who is developing or using for
development

note
----
---> it's starts with def keyword followed by func names
--->And it has calling function........

    def func_name(): #inside paranthesis are called parameters 
    --------------
      --------
      ------
      =-------
    function name()#inside function are  (arguments).

a = 6
def even_odd (a):
    if a%2 ==0:
        print("even")
    else:
        print("not even")
even_odd(a=2)

prime_num = 7
count = 0
def prime_check(num,k):
    for j in range(1,num+1):
        if num % j == 0:
           k += 1
    if k == 2:
        print("prime")
    else:
        print("not prime")
        
prime_check(prime_num,count)
'''
num = 7
n1 = 0
n2 = 1
def fibanacci_1(num,n1,n2):
    for i in range(num+1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)
fibanacci_1(num,n1,n2)

































    





               
