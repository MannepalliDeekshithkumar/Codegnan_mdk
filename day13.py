'''break-->this is used to exit from the loops, we found the required value...
for j in range(1,10):
    print(j)
    if j == 5:
        break
lis_ = [1,2,3,4]
for n in lis_:
    print(n)
    if n == 1:
        break
#continue--->this is used to skip the particular loop

for j in range(1,10):
    if j == 5:
        continue
    print(j)
    
#pass--->this is called as space holder incase any statement like(if, for, else, elif..) this should be complete, if not we will get
#syntax error to avoid this we are using pass

for j in range(1,100):
    pass
print(j)

#else--->for
----------------
it will fall back to else block, when all loops are completed


for m in range(1,100):
    print(m)
else:
    print("else block")

num = 1
while num<5:
    print(num)

#while---<this is a combination for and if statements if we did not end the loop in proper way it will run upto the memory space in the become empty



user_in =int(input("Enter the limit:"))
num1 = 0
num2 = 1
print(num1,num2)
for v in range(user_in+1):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3,end=" ")'''






















    
