'''print(9+8)
print("python" + "language")
print([1,+2] + [3,4])

concatenation
---------------
this is nothing but, a (+) behaviour..
case-1
-------
integers--- this will act as addtion for the int

case-2
-------
for other datatypes (we have to use same type)
this (+)act as concatenationk;=o-i0
print("deekshith" + [1,2])
output:print("deekshith" + [1,2])
TypeError: can only concatenate str (not "list") to str
tuple()--->
-------
is a collacation of different datatype and this is represented by (),separated by
(,)
eg...

thing = (1,"teja",[12,4],(6,7))

thing = (12,89,"deekshith",(23,"kanna",[67,"python is a language",(7,8)],[8,("python",[34,9])]))
print(thing)


num = 9
num_2 = 90
print(f"before swapping num ={num} and num_2 ={num_2}")
num, num_2 = num_2, num
print(f"after swapping num = {num} and num_2 = {num_2}")'''


leap_year = int(input("enter a leap year"))
if (leap_year % 4 == 0 and leap_year % 100 != 0)or leap_year % 400 == 0:
       print(f"yes, {leap_year} is a leap year")

else:
    print(f"no, {leap_year} is not leap_year")



















































