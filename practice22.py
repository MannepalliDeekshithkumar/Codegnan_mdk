'''a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a
print(id(b))
print(id(c))

num =int(input("enter the number:"))
sum_ = 0
for i in range(1, num + 1):
    if num % i == 0:
        sum_ += 1
if sum_ == 2:
   print("it is prime")
else:
   print("it is not prime")
'''

num = int(input("enter number:"))

n1 = 0
n2 = 1
for i in range(num+1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)

























































   
        
        
